import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from journal_apps.authentication.authentication import JWTAuthentication
from journal_apps.tournaments.models import Tournament
from journal_apps.tournaments.serializers import TournamentSerializer
from journal_apps.common.permissions import IsOwner

User = get_user_model()

logger = logging.getLogger(__name__)


class TournamentDetailView(APIView):

    # authentication_classes = [JWTAuthentication]
    serializer_class = TournamentSerializer

    def get(self, request, slug):
        
        try:
            tournament = Tournament.object.get(slug=slug)
        except Tournament.DoesNotExist:
            NotFound("The tournament does not exist.")

        # this could change with users are allowed to change who can view
        user = request.user
        if tournament.user != user:
            if tournament.shareable == "private":
                raise PermissionDenied("You are not allowed to view this tournament.")
            elif tournament.shareable == "my coaches":
                pass # will need to handle coach confirmation here

        serializer = TournamentSerializer(tournament)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TournamentListView(generics.ListAPIView):

    # permission_classes = [JWTAuthentication]
    serializer_class = TournamentSerializer
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return Tournament.objects.filter(user=user)


class TournamentCreateView(generics.CreateAPIView):
    # permission_classes = [JWTAuthentication]
    serializer_class = TournamentSerializer

    def create(self, request):
        
        user = request.user
        data = request.data
        data["user"] = user.id
        serializer = self.serializer_class(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        logger.info(
            f"Tournament {serializer.data.get('name')} created by {user.email}"
        )


class TournamentUpdateView(APIView):

    
    # permission_classes = [JWTAuthentication, IsOwner]
    serializer_class = TournamentSerializer

    def patch(self, request, slug):
        try:
            tournament = Tournament.objects.get(slug=slug)
        except Tournament.DoesNotExist:
            NotFound("The tournament does not exist.")
        
        data = request.data
        serializer = self.serializer_class(tournament, data=data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

class TournamentDeleteView(generics.DestroyAPIView):

    
    # permission_classes = [JWTAuthentication, IsOwner]
    queryset = Tournament.objects.all()
    lookup_field = "slug"

    def delete(self, request, *args, **kwargs):
        try:
            Tournament.objects.get(slug=self.kwargs.get("slug"))
        except Tournament.DoesNotExist:
            NotFound("The tournament does not exist.")
        
        delete_operation = self.destroy(request)
        data = {}
        if delete_operation:
            data["success"] = "Delete successful"

        else:
            data["failure"] = "Delete failed"

        return Response(data=data)

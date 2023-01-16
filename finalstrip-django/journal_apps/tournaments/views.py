import logging
from datetime import date

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from journal_apps.authentication.authentication import JWTAuthentication
from journal_apps.tournaments.models import Tournament
from journal_apps.tournaments.pagniation import TournamentPagination
from journal_apps.tournaments.serializers import TournamentDetailSerializer, TournamentListSerializer, TournamentCreateSerializer
from journal_apps.common.permissions import IsOwner
from journal_apps.common.utils import extract_data_and_assign_user, remove_empty_fields

User = get_user_model()

logger = logging.getLogger(__name__)


class TournamentDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    # permission_classes = [JWTAuthentication]

    def get(self, request, slug):
        
        try:
            tournament = Tournament.objects.get(slug=slug)
        except Tournament.DoesNotExist:
            NotFound("The tournament cannot be found.")


        # this could change with users are allowed to change who can view
        user = request.user
        if tournament.user != user:
            if tournament.shareable == "private":
                raise PermissionDenied("You are not allowed to view this tournament.")
            elif tournament.shareable == "my coaches":
                pass # will need to handle coach confirmation here


        serializer = TournamentDetailSerializer(tournament)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TournamentListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = TournamentListSerializer
    pagination_class = TournamentPagination

    def get_queryset(self):
        user = self.request.user
        # queryset = Tournament.objects.filter(user=user).order_by('-date')
        queryset = Tournament.objects.all().order_by('-date')
        return queryset


class TournamentCreateView(generics.CreateAPIView):
    permission_classes = [JWTAuthentication]
    serializer_class = TournamentCreateSerializer

    def create(self, request):
        data = extract_data_and_assign_user(request)
        cleaned_data = remove_empty_fields(data)
        print('cleaned data: ', cleaned_data)
        serializer = self.serializer_class(data=cleaned_data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            logger.info(
                f"Tournament {serializer.data.get('name')} created by {request.user.email}"
            )
            return Response({'message': 'Tournament created'}, status=status.HTTP_201_CREATED)

        print('serializer errors: ', serializer.errors)
        return Response({'message': 'invalid form error'}, status=status.HTTP_400_BAD_REQUEST)


class TournamentUpdateView(APIView):
    
    permission_classes = [JWTAuthentication, IsOwner]
    serializer_class = TournamentListSerializer

    def patch(self, request, slug):
        try:
            tournament = Tournament.objects.get(slug=slug)
        except Tournament.DoesNotExist:
            NotFound("The tournament cannot be found.")
        
        data = request.data
        serializer = self.serializer_class(tournament, data=data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

class TournamentDeleteView(generics.DestroyAPIView):

    permission_classes = [JWTAuthentication, IsOwner]
    queryset = Tournament.objects.all()
    lookup_field = "slug"

    def delete(self, request, *args, **kwargs):
        try:
            Tournament.objects.get(slug=self.kwargs.get("slug"))
        except Tournament.DoesNotExist:
            NotFound("The tournament cannot be found.")
        
        delete_operation = self.destroy(request)
        data = {}
        if delete_operation:
            data["success"] = "Delete successful"

        else:
            data["failure"] = "Delete failed"

        return Response(data=data)

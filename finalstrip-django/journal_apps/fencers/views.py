import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from journal_apps.authentication.authentication import JWTAuthentication
from journal_apps.common.permissions import IsOwner
from journal_apps.fencers.models import Fencer
from journal_apps.fencers.serializers import FencerSerializer

User = get_user_model()

logger = logging.getLogger(__name__)


class FencerDetailView(APIView):
    # authentication_classes = [JWTAuthentication]
    serializer_class = FencerSerializer

    def get(self, request, slug):
        
        try:
            fencer = Fencer.object.get(slug=slug)
        except Fencer.DoesNotExist:
            NotFound("The fencer cannot be found.")
        
        serializer = FencerSerializer(fencer)
        return Response(serializer, status=status.HTTP_200_OK)


class FencerListView(generics.ListAPIView):
    # permission_classes = [JWTAuthentication]
    serializer_class = FencerSerializer
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        fencers = Fencer.objects.filter(user=user)

        return fencers


class FencerCreateView(generics.CreateAPIView):
    # permission_classes = [JWTAuthentication]
    serializer_class = FencerSerializer

    def create(self, request):
        user = request.user
        data = request.data
        data["user"] = user.id
        serializer = self.serializer_class(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        logger.info(
            f"fencer {serializer.data.get('last_name')}, {serializer.data.get('first_name')} created by {user.email}"
        )


class FencerUpdateView(APIView):
    # permission_classes = [JWTAuthentication, IsOwner]
    serializer_class = FencerSerializer

    def patch(self, request, slug):
        try:
            fencer = Fencer.objects.get(slug=slug)
        except Fencer.DoesNotExist:
            NotFound("The fencer cannot be found.")
        
        data = request.data
        serializer = self.serializer_class(fencer, data=data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

class FencerDeleteView(generics.DestroyAPIView):
    # permission_classes = [JWTAuthentication, IsOwner]
    queryset = Fencer.objects.all()
    lookup_field = "slug"

    def delete(self, request, *args, **kwargs):
        try:
            Fencer.objects.get(slug=self.kwargs.get("slug"))
        except Fencer.DoesNotExist:
            NotFound("The fencer cannot be found.")
        
        delete_operation = self.destroy(request)
        data = {}
        if delete_operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete failed"

        return Response(data=data)
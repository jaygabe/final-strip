import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from journal_apps.authentication.authentication import JWTAuthentication
from journal_apps.common.permissions import IsOwner
from journal_apps.bouts.models import Bout
from journal_apps.bouts.serializers import BoutSerializer

User = get_user_model()

logger = logging.getLogger(__name__)


class BoutDetailView(APIView):
    # authentication_classes = [JWTAuthentication]
    serializer_class = BoutSerializer

    def get(self, request, slug):
        
        try:
            bout = Bout.object.get(slug=slug)
        except Bout.DoesNotExist:
            NotFound("The bout cannot be found.")
        
        serializer = BoutSerializer(bout)
        return Response(serializer, status=status.HTTP_200_OK)


class BoutListView(generics.ListAPIView):
    # permission_classes = [JWTAuthentication]
    serializer_class = BoutSerializer
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        bouts = Bout.objects.filter(user=user)

        return bouts


class BoutCreateView(generics.CreateAPIView):
    # permission_classes = [JWTAuthentication]
    serializer_class = BoutSerializer

    def create(self, request):
        user = request.user
        data = request.data
        data["user"] = user.id
        serializer = self.serializer_class(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        logger.info(
            f"bout {serializer.data.get('fencer_a')} vs {serializer.data.get('fencer_b')} created by {user.email}"
        )


class BoutUpdateView(APIView):
    # permission_classes = [JWTAuthentication, IsOwner]
    serializer_class = BoutSerializer

    def patch(self, request, slug):
        try:
            bout = Bout.objects.get(slug=slug)
        except Bout.DoesNotExist:
            NotFound("The bout cannot be found.")
        
        data = request.data
        serializer = self.serializer_class(bout, data=data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

class BoutDeleteView(generics.DestroyAPIView):
    # permission_classes = [JWTAuthentication, IsOwner]
    queryset = Bout.objects.all()
    lookup_field = "slug"

    def delete(self, request, *args, **kwargs):
        try:
            Bout.objects.get(slug=self.kwargs.get("slug"))
        except Bout.DoesNotExist:
            NotFound("The bout cannot be found.")
        
        delete_operation = self.destroy(request)
        data = {}
        if delete_operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete failed"

        return Response(data=data)
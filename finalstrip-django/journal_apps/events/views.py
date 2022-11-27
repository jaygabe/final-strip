import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from journal_apps.authentication.authentication import JWTAuthentication

from journal_apps.events.models import Event
from journal_apps.events.serializers import EventSerializer
from journal_apps.common.permissions import IsOwnerOrReadOnly


User = get_user_model()

logger = logging.getLogger(__name__)


class EventDetailView(APIView):
    
    # authentication_classes = [JWTAuthentication]
    serializer_class = EventSerializer

    def get(self, request, slug):
        
        try:
            event = Event.object.get(slug=slug)
        except Event.DoesNotExist:
            NotFound("The event does not exist.")

        # this could change with users are allowed to change who can view
        user = request.user

        if event.user != user:
            if event.shareable == "private":
                raise PermissionDenied("You are not allowed to view this event.")
            elif event.shareable == "my coaches":
                pass # will need to handle coach confirmation here

        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EventListView(generics.ListAPIView):

    # permission_classes = [JWTAuthentication]
    serializer_class = EventSerializer
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(user=user)


class EventCreateView(generics.CreateAPIView):
    # permission_classes = [JWTAuthentication]
    serializer_class = EventSerializer

    def create(self, request):
        
        user = request.user
        data = request.data
        data["user"] = user.id
        serializer = self.serializer_class(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        logger.info(
            f"Event {serializer.data.get('name')} created by {user.email}"
        )


class EventUpdateView(APIView):

    
    # permission_classes = [JWTAuthentication, IsOwnerOrReadOnly]
    serializer_class = EventSerializer

    def patch(self, request, slug):
        try:
            event = Event.objects.get(slug=slug)
        except Event.DoesNotExist:
            NotFound("The event does not exist.")
        
        data = request.data
        serializer = self.serializer_class(event, data=data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

class EventDeleteView(generics.DestroyAPIView):

    
    # permission_classes = [JWTAuthentication, IsOwnerOrReadOnly]
    queryset = Event.objects.all()
    lookup_field = "slug"

    def delete(self, request, *args, **kwargs):
        try:
            Event.objects.get(slug=self.kwargs.get("slug"))
        except Event.DoesNotExist:
            NotFound("The event does not exist.")
        
        delete_operation = self.destroy(request)
        data = {}
        if delete_operation:
            data["success"] = "Delete successful"

        else:
            data["failure"] = "Delete failed"

        return Response(data=data)
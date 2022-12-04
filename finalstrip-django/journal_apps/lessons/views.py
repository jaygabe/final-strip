import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from journal_apps.authentication.authentication import JWTAuthentication
from journal_apps.lessons.models import Lesson
from journal_apps.lessons.serializers import LessonSerializer
from journal_apps.common.permissions import IsOwner

User = get_user_model()

logger = logging.getLogger(__name__)


class LessonDetailView(APIView):

    # authentication_classes = [JWTAuthentication]
    serializer_class = LessonSerializer

    def get(self, request, slug):
        
        try:
            lesson = Lesson.object.get(slug=slug)
        except Lesson.DoesNotExist:
            NotFound("The lesson cannot be found.")

        serializer = LessonSerializer(lesson)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LessonListView(generics.ListAPIView):

    # permission_classes = [JWTAuthentication]
    serializer_class = LessonSerializer
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return Lesson.objects.filter(user=user)


class LessonCreateView(generics.CreateAPIView):
    # permission_classes = [JWTAuthentication]
    serializer_class = LessonSerializer

    def create(self, request):
        
        user = request.user
        data = request.data
        data["user"] = user.id
        serializer = self.serializer_class(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        logger.info(
            f"Lesson {serializer.data.get('title')} created by {user.email}"
        )


class LessonUpdateView(APIView):
    # permission_classes = [JWTAuthentication, IsOwner]
    serializer_class = LessonSerializer

    def patch(self, request, slug):
        try:
            lesson = Lesson.objects.get(slug=slug)
        except Lesson.DoesNotExist:
            NotFound("The lesson cannot be found.")
        
        data = request.data
        serializer = self.serializer_class(lesson, data=data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

class LessonDeleteView(generics.DestroyAPIView):
    # permission_classes = [JWTAuthentication, IsOwner]
    queryset = Lesson.objects.all()
    lookup_field = "slug"

    def delete(self, request, *args, **kwargs):
        try:
            Lesson.objects.get(slug=self.kwargs.get("slug"))
        except Lesson.DoesNotExist:
            NotFound("The lesson cannot be found.")
        
        delete_operation = self.destroy(request)
        data = {}
        if delete_operation:
            data["success"] = "Delete successful"

        else:
            data["failure"] = "Delete failed"

        return Response(data=data)
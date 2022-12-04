from django.urls import path

from .views import (
    LessonCreateView,
    LessonDeleteView,
    LessonDetailView,
    LessonListView,
    LessonUpdateView,
)

urlpatterns = [
    path("all/", LessonListView.as_view(), name="all-lesson"),
    path("create/", LessonCreateView.as_view(), name="create-lesson"),
    path("details/<slug:slug>/", LessonDetailView.as_view(), name="detail-lesson"),
    path("delete/<slug:slug>/", LessonDeleteView.as_view(), name="delete-lesson"),
    path("update/<slug:slug>/", LessonUpdateView.as_view(), name="update-lesson"),
]
from django.urls import path

from .views import (
    EventCreateView,
    EventDeleteView,
    EventDetailView,
    EventListView,
    EventUpdateView,
)

urlpatterns = [
    path("all/", EventListView.as_view(), name="all-events"),
    path("create/", EventCreateView.as_view(), name="create-event"),
    path("details/<slug:slug>/", EventDetailView.as_view(), name="detail-event"),
    path("delete/<slug:slug>/", EventDeleteView.as_view(), name="delete-event"),
    path("update/<slug:slug>/", EventUpdateView.as_view(), name="update-event"),

]
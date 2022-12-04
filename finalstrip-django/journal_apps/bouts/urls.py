from django.urls import path

from .views import (
    BoutCreateView,
    BoutDeleteView,
    BoutDetailView,
    BoutListView,
    BoutUpdateView,
)

urlpatterns = [
    path("all/", BoutListView.as_view(), name="all-bouts"),
    path("create/", BoutCreateView.as_view(), name="create-bout"),
    path("details/<slug:slug>/", BoutDetailView.as_view(), name="detail-bout"),
    path("delete/<slug:slug>/", BoutDeleteView.as_view(), name="delete-bout"),
    path("update/<slug:slug>/", BoutUpdateView.as_view(), name="update-bout"),
] 
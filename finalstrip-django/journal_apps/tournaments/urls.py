from django.urls import path

from .views import (
    TournamentCreateView,
    TournamentDeleteView,
    TournamentDetailView,
    TournamentListView,
    TournamentUpdateView,
)

urlpatterns = [
    path("all/", TournamentListView.as_view(), name="all-tournaments"),
    path("create/", TournamentCreateView.as_view(), name="create-tournament"),
    path("detail/<slug:slug>/", TournamentDetailView.as_view(), name="detail-tournament"),
    path("delete/<slug:slug>/", TournamentDeleteView.as_view(), name="delete-tournament"),
    path("update/<slug:slug>/", TournamentUpdateView.as_view(), name="update-tournament"),
]
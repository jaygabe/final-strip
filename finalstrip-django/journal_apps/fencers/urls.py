from django.urls import path

from .views import (
    FencerCreateView,
    FencerDeleteView,
    FencerDetailView,
    FencerListView,
    FencerUpdateView,
)

urlpatterns = [
    path("all/", FencerListView.as_view(), name="all-fencers"),
    path("create/", FencerCreateView.as_view(), name="create-fencers"),
    path("details/<slug:slug>/", FencerDetailView.as_view(), name="detail-fencers"),
    path("delete/<slug:slug>/", FencerDeleteView.as_view(), name="delete-fencers"),
    path("update/<slug:slug>/", FencerUpdateView.as_view(), name="update-fencers"),

]
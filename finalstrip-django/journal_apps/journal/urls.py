from django.urls import path

from .views import BoutView, EventView, FencerView, LessonView, TournamentView, manual_reload


urlpatterns = [

    path('manual_reload', manual_reload),

    path('fencer/<slug:slug>', FencerView.as_view()),
    path('tournament/', TournamentView.as_view()),
    path('tournament/<slug:slug>', TournamentView.as_view()),
    path('event/<slug:slug>', EventView.as_view()),
    path('bout/<slug:slug>', BoutView.as_view()),
    path('lesson/<slug:slug>', LessonView.as_view()),

]
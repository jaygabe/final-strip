from django.urls import path

from .views import BoutView, FencerView, LessonView


urlpatterns = [

    path('fencer/<slug:slug>', FencerView.as_view()),
    path('bout/<slug:slug>', BoutView.as_view()),
    path('lesson/<slug:slug>', LessonView.as_view()),

]
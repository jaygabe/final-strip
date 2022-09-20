from django.urls import path

from .views import FencerView


urlpatterns = [

    path('fencer/<slug:slug>', FencerView.as_view()),

]
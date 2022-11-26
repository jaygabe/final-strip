from django.urls import path

from .views import manual_reload


urlpatterns = [

    path('manual_reload', manual_reload),

]
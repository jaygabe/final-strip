from django.urls import path

from .views import manual_reload, fencer_record, query_usaf_fencers


urlpatterns = [

    path('manual-reload', manual_reload),
    path('fencer-record/<str:member_id>', fencer_record),
    path('search-members/<str:query>', query_usaf_fencers)

]
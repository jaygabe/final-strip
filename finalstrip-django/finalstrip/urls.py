
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Finalstrip",
        default_version="v1",
        description="API endpoints for finalstrip journal app.  Please reach out if you would like to use this resouce directly.",
        contact=openapi.Contact(email="info@finalstrip.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/auth/', include('journal_apps.authentication.urls')),
    path('api/tournaments/', include('journal_apps.tournaments.urls')),
    path('api/events/', include('journal_apps.events.urls')),
    path('api/bouts/', include('journal_apps.bouts.urls')),
    path('api/fencers/', include('journal_apps.fencers.urls')),
    path('api/lessons/', include('journal_apps.lessons.urls')),
    path('api/usaf-data/', include('journal_apps.usaf_data.urls'))
]

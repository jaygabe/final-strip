
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
    path('api/journal/', include('journal_apps.journal.urls')),
    path('api/usaf-data/', include('journal_apps.usaf_data.urls'))
]

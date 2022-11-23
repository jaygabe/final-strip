
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('journal_apps.authentication.urls')),
    path('journal/', include('journal_apps.journal.urls'))
]

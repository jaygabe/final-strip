from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LessonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lessons'
    verbose_name = _("Lessons")
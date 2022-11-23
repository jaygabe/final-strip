from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class FencersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'journal_apps.fencers'
    verbose_name = _("Fencers")

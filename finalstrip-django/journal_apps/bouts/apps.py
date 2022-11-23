from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class BoutsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'journal_apps.bouts'
    verbose_name = _("Bouts")

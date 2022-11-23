from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SocialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'journal_apps.social'
    verbose_name = _('Social')

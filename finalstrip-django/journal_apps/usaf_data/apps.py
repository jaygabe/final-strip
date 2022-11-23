from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UsfaDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'journal_apps.usaf_data'
    verbose_name = _("USA Fencing Data")

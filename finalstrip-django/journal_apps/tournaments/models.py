from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from journal_apps.common.models import JournalModel


class Tournament(JournalModel):
    class EventLevel(models.TextChoices):
        LOCAL = 'Local', _('Local')
        REGIONAL = 'Regional', _('Regional')
        NATIONAL = 'National', _('National')
        WORLD = 'World', _('World')

    name = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    event_level = models.CharField(max_length=200, null=True, choices=EventLevel.choices)
    club = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
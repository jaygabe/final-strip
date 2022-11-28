from datetime import date

from django.db import models
from django.utils.translation import gettext_lazy as _

from journal_apps.tournaments.models import Tournament
from journal_apps.common.models import JournalModel


class Event(JournalModel):
    class EventType(models.TextChoices):
        Y8 = 'Y8', _('Y8')
        Y10 = 'Y10', _('Y10')
        Y12 = 'Y12', _('Y12')
        Y14 = 'Y14', _('Y14')
        CADET = 'Cadet', _('Cadet')
        JUNIOR = 'Junior', _('Junior')
        SENIOR = 'Senior/Open', _('Senior/Open')
        VET = 'Vet Combined', _('Vet Combined')
        VET40 = 'Vet40', _('Vet40')
        VET50 = 'Vet50', _('Vet50')
        VET60 = 'Vet60', _('Vet60')
        VET70 = 'Vet70', _('Vet70')
        VET80 = 'Vet80', _('Vet80')
        DIVI = 'Div I', _('Div I')
        DIVIA = 'Div IA', _('Div IA')
        DIVII = 'Div II', _('Div II')
        DIVIII = 'Div III', _('Div III')
        PARA = 'Para', _('Para')
        PENTA = 'Modern Pentathlon', _('Modern Pentathlon')
    
    class WeaponType(models.TextChoices):
        FOIL = "foil", _("foil")
        EPEE = "epee", _("epee")
        SABRE = "sabre", _("sabre")
        OTHER = "other", _("other")

    tournament = models.ForeignKey(Tournament, related_name='tournament_name', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(default=date.today)
    event_type = models.CharField(max_length=100, choices=EventType.choices, null=True, blank=True)
    weapon = models.CharField(max_length=100, choices=WeaponType.choices, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
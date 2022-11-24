from django.db import models
from autoslug import AutoSlugField
from journal_apps.tournaments.models import Tournament
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    EVENT_CHOICES = (
    ('Y8', 'Y8'),
    ('Y10', 'Y10'),
    ('Y12', 'Y12'),
    ('Y14', 'Y14'),
    ('Cadet', 'Cadet'),
    ('Junior', 'Junior'),
    ('Senior/Open', 'Senior/Open'),
    ('Vet Combined', 'Vet Combined'),
    ('Vet40', 'Vet40'),
    ('Vet50', 'Vet50'),
    ('Vet60', 'Vet60'),
    ('Vet70', 'Vet70'),
    ('Vet80', 'Vet80'),
    ('Div I', 'Div I'),
    ('Div IA', 'Div IA'),
    ('Div II', 'Div II'),
    ('Div III', 'Div III'),
    ('Para', 'Para'),
    ('Modern Pentathlon','Modern Pentathlon')
    )

    slug = AutoSlugField(max_length=10, unique=True, populate_from=('name',), editable=True)
    user = models.ForeignKey(User, related_name="event_user", on_delete=models.CASCADE, null=True, blank=True)
    tournament = models.ForeignKey(Tournament, related_name='tournament_name', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(default='2/2/2022')
    event_type = models.CharField(max_length=200, choices=EVENT_CHOICES, null=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
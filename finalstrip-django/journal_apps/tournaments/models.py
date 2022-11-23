from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model

User = get_user_model()

class Tournament(models.Model):
    EVENT_LEVEL = (
        ('Local', 'Local'),
        ('Regional', 'Regional'),
        ('National', 'National'),
        ('World', 'World'),
    )

    slug = AutoSlugField(max_length=10, unique=True, populate_from=('name',), editable=True)
    user = models.ForeignKey(User, related_name="tourn_user", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    date = models.DateField(default='2/2/2022')
    event_level = models.CharField(max_length=200, null=True, choices=EVENT_LEVEL)
    club = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
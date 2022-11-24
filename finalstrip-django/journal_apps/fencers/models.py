from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from journal_apps.usaf_data.models import USAFencingInfo

User = get_user_model()


class Fencer(models.Model):

    SCALE_CHOICES = (
    ('poor', 'poor'),
    ('fair', 'fair'),
    ('average', 'average'),
    ('good', 'good'),
    ('great', 'great'),
    ('excellent', 'excellent')
    )

    slug = AutoSlugField(max_length=10, unique=True, populate_from=('last_name',), editable=True)
    # defined by who created it
    user = models.ForeignKey(User, related_name="user_fencer", on_delete=models.SET_NULL, null=True, blank=True)
    # input by user
    fencer_is_me = models.BooleanField(default=False)
    usa_fencing_info = models.ForeignKey(USAFencingInfo, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True,)
    last_name = models.CharField(max_length=200, null=True)
    club = models.CharField(max_length=200, null=True, blank=True)
    club_2 = models.CharField(max_length=200, null=True, blank=True)
    school = models.CharField(max_length=200, null=True, blank=True)
    division = models.CharField(max_length=200, null=True, blank=True)
    region = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=20, default="USA", null=True, blank=True)
    handed = models.CharField(max_length=10, null=True, blank=True)
    grip = models.CharField(max_length=50, null=True, blank=True)
    usfa_rating_epee = models.CharField(max_length=10, default="U", blank=True)
    usfa_rating_sabre = models.CharField(max_length=10, default="U", blank=True)
    usfa_rating_foil = models.CharField(max_length=10, default="U", blank=True)
    ref_rating_epee = models.CharField(max_length=10, null = True, blank=True)
    ref_rating_sabre = models.CharField(max_length=10, null = True, blank=True)
    ref_rating_foil = models.CharField(max_length=10, null = True, blank=True)
    custom_rating = models.CharField(max_length=40, null = True, blank=True)
    timing = models.IntegerField(null = True, blank=True, choices=SCALE_CHOICES)
    distance = models.IntegerField(null = True, blank=True, choices=SCALE_CHOICES)
    bladework = models.IntegerField(null = True, blank=True, choices=SCALE_CHOICES)
    endurance = models.IntegerField(null = True, blank=True, choices=SCALE_CHOICES)
    strength = models.IntegerField(null = True, blank=True, choices=SCALE_CHOICES)

    tactical_description = models.CharField(max_length=50, blank=True)
    favorite_actions = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    public = models.BooleanField(default=True)
    share_coach = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.last_name + ", " + self.first_name
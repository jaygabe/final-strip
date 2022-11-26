from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from journal_apps.fencers.models import Fencer
from journal_apps.tournaments.models import Tournament
from journal_apps.events.models import Event

User = get_user_model()


class Bout(models.Model):

    SCALE_CHOICES = (
    ('poor', 'poor'),
    ('fair', 'fair'),
    ('average', 'average'),
    ('good', 'good'),
    ('great', 'great'),
    ('excellent', 'excellent')
    )
    HAND_CHOICES = (('Right', 'Right'), ('Left', 'Left'))
    BOUT_CHOICES = (
        ('Pool', 'Pool'), 
        ('DE', 'DE'), 
        ('Team Relay', 'Team Relay'), 
        ('Other', 'Other')
    )

    slug = AutoSlugField(max_length=10, unique=True, populate_from=('fencer_b',), editable=True)
    user = models.ForeignKey(User, related_name="bout_user", on_delete=models.SET_NULL, null=True, blank=True)
    winner_is_a = models.BooleanField(default=True)
    fencer_a = models.ForeignKey(Fencer, related_name="fencer_a", on_delete=models.SET_NULL, null=True, blank=True)
    fencer_b = models.ForeignKey(Fencer, related_name="fencer_b", on_delete=models.SET_NULL, null=True, blank=True)
    score_a = models.IntegerField()
    score_b = models.IntegerField()
    fencer_a_hand = models.CharField(choices = HAND_CHOICES, max_length=10, blank=True)
    fencer_b_hand = models.CharField(choices = HAND_CHOICES, max_length=10, blank=True)
    fencer_a_yellow_carded = models.BooleanField(default=False)
    fencer_b_yellow_carded = models.BooleanField(default=False)
    fencer_a_red_carded = models.BooleanField(default=False)
    fencer_b_red_carded = models.BooleanField(default=False)
    fencer_a_black_carded = models.BooleanField(default=False)
    fencer_b_black_carded = models.BooleanField(default=False)
    fencer_a_passivity = models.BooleanField(default=False)
    fencer_b_passivity = models.BooleanField(default=False)
    fencer_a_medical = models.BooleanField(default=False)
    fencer_b_medical = models.BooleanField(default=False)
    fencer_a_video_used = models.IntegerField(default=0, blank=True)
    fencer_b_video_used = models.IntegerField(default=0, blank=True)
    fencer_a_footwork = models.CharField(max_length=20, null = True, blank=True, choices=SCALE_CHOICES)
    fencer_b_footwork = models.CharField(max_length=20, null = True, blank=True, choices=SCALE_CHOICES)
    fencer_a_bladework = models.CharField(max_length=20, null = True, blank=True, choices=SCALE_CHOICES)
    fencer_b_bladework = models.CharField(max_length=20, null = True, blank=True, choices=SCALE_CHOICES)
    fencer_a_distance = models.CharField(max_length=20, null = True, blank=True, choices=SCALE_CHOICES)
    fencer_b_distance = models.CharField(max_length=20, null = True, blank=True, choices=SCALE_CHOICES)
    fencer_a_timing = models.CharField(max_length=20, null = True, blank=True, choices=SCALE_CHOICES)
    fencer_b_timing = models.CharField(max_length=20, null = True, blank=True, choices=SCALE_CHOICES)
    fencer_a_energy = models.CharField(max_length=20, null = True, blank=True, choices=SCALE_CHOICES)
    fencer_b_energy = models.CharField(max_length=20, null = True, blank=True, choices=SCALE_CHOICES)
    fencer_a_notes = models.TextField(null=True, blank=True)
    fencer_b_notes = models.TextField(null=True, blank=True)
    
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    referee = models.CharField(max_length=200, null=True, blank=True)
    bout_type = models.CharField(max_length=200, null=True, blank=True, choices=BOUT_CHOICES)
    round = models.IntegerField(default=1)
    notes = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=True)
    share_coach = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        #return str(self.id)
        return str(self.fencer_a) + " vs " + str(self.fencer_b)


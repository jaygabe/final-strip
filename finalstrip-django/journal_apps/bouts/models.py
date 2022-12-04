from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from journal_apps.fencers.models import Fencer
from journal_apps.tournaments.models import Tournament
from journal_apps.events.models import Event

User = get_user_model()


class Bout(models.Model):

    class ScaleChoices(models.TextChoices):
        POOR = 'poor', _('poor')
        FAIR = 'fair', _('fair')
        AVERAGE = 'average', _('average')
        GOOD = 'good', _('good')
        GREAT = 'great', _('great')
        EXCELLENT = 'excellent', _('excellent')
        NA = 'not applicable', _('not applicable')


    class HandChoices(models.TextChoices):
        RIGHT = 'right', _('right') 
        LEFT = 'left', _('left')

    
    class GripChoices(models.TextChoices):
        PISTOL = 'pistol', _('pistol')
        FRENCH = 'french', _('french')
        OTHER = 'other', _('other')


    class BoutChoices(models.TextChoices):
        POOL = 'pool', _('pool'), 
        DE = 'direct elimination', _('direct elimination'), 
        TEAM = 'team relay', _('team relay'), 
        OTHER = 'other', _('other')
    

    winner_is_a = models.BooleanField(default=True)
    fencer_a = models.ForeignKey(Fencer, related_name="fencer_a", on_delete=models.SET_NULL, null=True, blank=True)
    fencer_b = models.ForeignKey(Fencer, related_name="fencer_b", on_delete=models.SET_NULL, null=True, blank=True)
    score_a = models.IntegerField()
    score_b = models.IntegerField()
    fencer_a_hand = models.CharField(choices=HandChoices.choices, max_length=10, blank=True, null=True)
    fencer_b_hand = models.CharField(choices=HandChoices.choices, max_length=10, blank=True, null=True)
    fencer_a_grip = models.CharField(choices=GripChoices.choices, max_length=10, blank=True, null=True)
    fencer_b_grip = models.CharField(choices=GripChoices.choices, max_length=10, blank=True, null=True)
    fencer_a_yellow_carded = models.BooleanField(default=False)
    fencer_b_yellow_carded = models.BooleanField(default=False)
    fencer_a_red_carded = models.BooleanField(default=False)
    fencer_b_red_carded = models.BooleanField(default=False)
    fencer_a_black_carded = models.BooleanField(default=False)
    fencer_b_black_carded = models.BooleanField(default=False)
    fencer_a_priority = models.BooleanField(default=False)
    fencer_b_priority = models.BooleanField(default=False)
    fencer_a_medical = models.BooleanField(default=False)
    fencer_b_medical = models.BooleanField(default=False)
    fencer_a_video_used = models.IntegerField(default=0, blank=True)
    fencer_b_video_used = models.IntegerField(default=0, blank=True)
    fencer_a_footwork = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    fencer_b_footwork = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    fencer_a_bladework = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    fencer_b_bladework = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    fencer_a_distance = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    fencer_b_distance = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    fencer_a_timing = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    fencer_b_timing = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    fencer_a_energy = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    fencer_b_energy = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    fencer_a_notes = models.TextField(null=True, blank=True)
    fencer_b_notes = models.TextField(null=True, blank=True)
    
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    referee = models.CharField(max_length=200, null=True, blank=True)
    bout_type = models.CharField(max_length=200, null=True, blank=True, choices=BoutChoices.choices, default=BoutChoices.POOL)
    round = models.IntegerField(default=1)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        #return str(self.id)
        return str(self.fencer_a) + " vs " + str(self.fencer_b)


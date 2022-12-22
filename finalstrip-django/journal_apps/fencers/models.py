from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from journal_apps.usaf_data.models import USAFencingInfo

User = get_user_model()


class Fencer(models.Model):

    class ScaleChoices(models.TextChoices):
        POOR = ('poor', _('poor'))
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
        BOTH = 'both', _('both')
        OTHER = 'other', _('other')
    

    class RefRatingChoices(models.TextChoices):
        P = 'P', _('P')
        L2 = 'L2', _('L2')
        L1 = 'L1', _('L1')
        R2 = 'R2', _('R2')
        R1 = 'R1', _('R1')
        N2 = 'N2', _('N2')
        N1 = 'N1', _('N1')
        UNKNOWN = 'unknown', _('unknown')
        NA = 'not applicable', _('not applicable')


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
    handed = models.CharField(max_length=10, null=True, blank=True, choices=HandChoices.choices)
    primary_grip = models.CharField(max_length=10, null=True, blank=True, choices=GripChoices.choices)
    usaf_rating_epee = models.CharField(max_length=10, default="U", blank=True)
    usaf_rating_sabre = models.CharField(max_length=10, default="U", blank=True)
    usaf_rating_foil = models.CharField(max_length=10, default="U", blank=True)
    ref_rating_epee = models.CharField(max_length=10, null=True, blank=True)
    ref_rating_sabre = models.CharField(max_length=10, null=True, blank=True)
    ref_rating_foil = models.CharField(max_length=10, null=True, blank=True)
    custom_rating = models.CharField(max_length=10, null=True, blank=True)
    timing = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    distance = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    bladework = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    endurance = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)
    strength = models.CharField(max_length=20, null=True, blank=True, choices=ScaleChoices.choices)

    tactical_description = models.CharField(max_length=200, blank=True)
    favorite_actions = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.last_name + ", " + self.first_name
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _
from journal_apps.usaf_data.models import USAFencingInfo
from journal_apps.common.models import JournalModel
from journal_apps.bouts.models import Bout

User = get_user_model()


class Fencer(JournalModel):

    # class ScaleChoices(models.TextChoices):
    #     POOR = ('poor', _('poor'))
    #     FAIR = 'fair', _('fair')
    #     AVERAGE = 'average', _('average')
    #     GOOD = 'good', _('good')
    #     GREAT = 'great', _('great')
    #     EXCELLENT = 'excellent', _('excellent')
    #     NA = 'not applicable', _('not applicable')
    

    class HandChoices(models.TextChoices):
        RIGHT = 'Right', _('Right') 
        LEFT = 'Left', _('Left')
    

    class GripChoices(models.TextChoices):
        PISTOL = 'Pistol', _('Pistol')
        FRENCH = 'French', _('French')
        BOTH = 'Both', _('Both')
        OTHER = 'Other', _('Other')
    

    class RefRatingChoices(models.TextChoices):
        P = 'P', _('P')
        L2 = 'L2', _('L2')
        L1 = 'L1', _('L1')
        R2 = 'R2', _('R2')
        R1 = 'R1', _('R1')
        N2 = 'N2', _('N2')
        N1 = 'N1', _('N1')
        UNKNOWN = 'Unknown', _('Unknown')
        NA = 'Not Applicable', _('Not Applicable')


    fencer_is_me = models.BooleanField(default=False)
    usa_fencing_info = models.ForeignKey(USAFencingInfo, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True,)
    last_name = models.CharField(max_length=200, null=True)
    club = models.CharField(max_length=200, null=True, blank=True)
    club2 = models.CharField(max_length=200, null=True, blank=True)
    school = models.CharField(max_length=200, null=True, blank=True)
    division = models.CharField(max_length=200, null=True, blank=True)
    region = models.IntegerField(blank=True)
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
    timing = models.IntegerField(null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)
    bladework = models.IntegerField(null=True, blank=True)
    endurance = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)

    tactical_description = models.CharField(max_length=200, blank=True)
    favorite_actions = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        if self.usa_fencing_info:
            first = str('' if self.usa_fencing_info.first_name is None else self.usa_fencing_info.first_name)
            last = str('' if self.usa_fencing_info.last_name is None else self.usa_fencing_info.last_name)
        else:
            first = str('' if self.first_name is None else self.first_name)
            last = str('' if self.last_name is None else self.last_name)
        return last + ", " + first

    @property
    def average_timing(self):
        if Bout.objects.all().count() > 0:
            timing = (
                Bout.objects.filter(fencer_a=self.pkid).all().aggregate(Avg("value"))
            )
            return round(timing["value__avg"], 1) if timing["value__avg"] else 0
        return 0
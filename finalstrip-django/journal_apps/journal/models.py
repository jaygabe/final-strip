from django.db import models
from django.db.models import Q
from journal_apps.authentication.models import User
from journal_apps.social.models import ConnectFencers
from journal_apps.usaf_data.models import USAFencingInfo
from journal_apps.tournaments.models import Tournament

from autoslug import AutoSlugField

# to drop from db using manage.py:
# 1) pen the db shell using python manage.py dbshell
# 2) DROP TABLE {app-name}_{model-name}


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
    tournament = models.ForeignKey(Tournament, related_name='tournament', on_delete=models.CASCADE)
    name= models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(default='2/2/2022')
    event_type = models.CharField(max_length=200, choices=EVENT_CHOICES, null=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

 
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


class Lesson(models.Model):
    slug = AutoSlugField(max_length=10, unique=True, populate_from=('coach',), editable=True)
    user = models.ForeignKey(User, related_name='fencer', on_delete=models.SET_NULL, null=True, blank=True)
    coach = models.ForeignKey(User, related_name='instructor', on_delete=models.SET_NULL, null=True, blank=True)
    lesson_date = models.DateField(default="1/1/1900")
    title = models.CharField(max_length=100, null = True, blank=True)
    description = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=True)
    share_coach = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.title)
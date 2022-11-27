from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.db.models import Q
from journal_apps.social.models import ConnectFencers

User = get_user_model()

class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = "male", _("male")
        FEMALE = "female", _("female")
        OTHER = "other", _("other")
    
    user = models.ForeignKey(User)

    about_me = models.TextField(
        verbose_name=_("about me"),
        default="say something about yourself",
    )
    gender = models.CharField(
        verbose_name=_("gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("country"), default="US", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("city"),
        max_length=180,
        default="Colorado Springs",
        blank=False,
        null=False,
    )

    def coaches(self):
        connections = ConnectFencers.objects.filter(student=self.user)
        coach_connects = connections.objects.filter(c_accepts=True)
        accepted_connects = coach_connects.objects.filter(s_accepts=True)
        return accepted_connects.objects.values_list('coach', flat=True)
        
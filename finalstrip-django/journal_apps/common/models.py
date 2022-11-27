import uuid
from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class JournalModel(models.Model):
    class Shareability(models.TextChoices):
            PRIVATE = "private", _("private")
            COACHES = "my coaches", _("my coaches")
            # CLUB = "club members", _("club members")
            # FRIENDS = "friends", _("friends")
            EVERYONE = "everyone", _("everyone")

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = AutoSlugField(max_length=10, unique=True, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.DateField(null=True, blank=True)
    shareable = models.CharField(max_length=10, choices=Shareability.choices, default=Shareability.PRIVATE )
    
    class Meta:
        abstract = True
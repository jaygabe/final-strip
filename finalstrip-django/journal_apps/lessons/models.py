from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model

User = get_user_model()


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
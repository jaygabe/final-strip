from django.db import models
from django.db.models import Q
from journal_apps.authentication.models import User
from journal_apps.social.models import ConnectFencers
from journal_apps.usaf_data.models import USAFencingInfo
from journal_apps.tournaments.models import Tournament
from journal_apps.events.models import Event


# to drop from db using manage.py:
# 1) pen the db shell using python manage.py dbshell
# 2) DROP TABLE {app-name}_{model-name}
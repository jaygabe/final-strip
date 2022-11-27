from rest_framework import serializers

from journal_apps.tournaments.models import Tournament


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        exclude = ('pkid','id')
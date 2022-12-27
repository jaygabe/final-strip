from rest_framework import serializers

from journal_apps.tournaments.models import Tournament


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        exclude = ('pkid','id')


class TournamentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = (
            'name', 
            'date', 
            'event_level',
            'club', 
            'location',
            'url', 
            'notes',
            'user'
            )
from rest_framework import serializers

from journal_apps.tournaments.models import Tournament
from journal_apps.events.serializers import EventSerializer

class TournamentDetailSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField(read_only=True)

    def get_events(self, obj):
        events = obj.events.all()
        serializer = EventSerializer(events, many=True)
        return serializer.data
    
    class Meta:
        model = Tournament
        exclude = ('pkid','id')


class TournamentListSerializer(serializers.ModelSerializer):
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
from rest_framework import serializers

from journal_apps.events.models import Event
from journal_apps.bouts.serializers import BoutSerializer

class EventDetailSerializer(serializers.ModelSerializer):
    bouts = serializers.SerializerMethodField(read_only=True)

    def get_bouts(self, obj):
        events = obj.bouts.all()
        serializer = BoutSerializer(events, many=True)
        return serializer.data
    
    class Meta:
        model = Event
        exclude = ('pkid','id')

class EventSerializer(serializers.ModelSerializer):
    tourn_info = serializers.SerializerMethodField(read_only=True)

    def get_tourn_info(self, obj):
        return {
            "name": obj.tournament.name,
            "location": obj.tournament.location,
            "date": obj.tournament.date,
            "url": obj.tournament.url
        }

    class Meta:
        model = Event
        exclude = ('pkid', 'id', 'deleted')

class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'user',
            'tournament',
            'name',
            'date',
            'weapon',
            'event_type',
            'notes'
        )


class UpdateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('pkid','id','deleted')
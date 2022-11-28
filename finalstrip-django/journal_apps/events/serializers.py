from rest_framework import serializers

from journal_apps.events.models import Event

class EventSerializer(serializers.ModelSerializer):
    tourn_info = serializers.SerializerMethodField(read_only=True)

    def get_tournament(self, obj):
        return {
            "name": obj.tournament.name,
            "location": obj.tournament.location,
            "date": obj.tournament.date,
            "url": obj.tournament.url
        }

    class Meta:
        model = Event
        exclude = ('pkid', 'id', 'deleted')


class UpdateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('pkid','id','deleted')
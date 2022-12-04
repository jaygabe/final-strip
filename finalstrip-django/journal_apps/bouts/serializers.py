from rest_framework import serializers

from journal_apps.bouts.models import Bout

class BoutSerializer(serializers.ModelSerializer):
    tournament = serializers.SerializerMethodField(read_only=True)
    event = serializers.SerializerMethodField(read_only=True)

    def get_tournament(self, obj):
        return {
            "name": obj.tournament.name,
            "location": obj.tournament.location,
            "date": obj.tournament.date,
            "url": obj.tournament.url,
            "slug": obj.tournament.slug
        }
    
    def get_event(self, obj):
        return {
            "name": obj.event.name,
            "date": obj.event.date,
            "event_type": obj.event.event_type,
            "weapon": obj.event.weapon,
            "slug": obj.event.slug
        }

    class Meta:
        model = Bout
        exclude = ('pkid', 'id', 'deleted')


class UpdateBoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bout
        exclude = ('pkid','id','deleted')
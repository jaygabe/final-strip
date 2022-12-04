from rest_framework import serializers

from journal_apps.bouts.models import Bout

class BoutSerializer(serializers.ModelSerializer):
    tournament = serializers.SerializerMethodField(read_only=True)
    event = serializers.SerializerMethodField(read_only=True)

    def get_tournament(self, obj):
        return {
            "name": obj.tournament_name.name,
            "location": obj.tournament_name.location,
            "date": obj.tournament_name.date,
            "url": obj.tournament_name.url,
            "slug": obj.tournament_name.slug
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
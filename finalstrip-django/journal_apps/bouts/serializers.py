from rest_framework import serializers

from journal_apps.bouts.models import Bout

class BoutSerializer(serializers.ModelSerializer):
    fencer_a = serializers.CharField()
    fencer_b = serializers.CharField()
    event = serializers.SerializerMethodField(read_only=True)
    tournament = serializers.SerializerMethodField(read_only=True)

    def get_fencer_a(self, obj):
        return obj.fencer_a.__str__
    
    def get_fencer_b(self, obj):
        return obj.fencer_b.__str__
    
    def get_event(self, obj):
        return {
            "name": obj.event.name,
            "date": obj.event.date,
            "event_type": obj.event.event_type,
            "weapon": obj.event.weapon,
            "slug": obj.event.slug
        }
    
    def get_tournament(self, obj):
        return {
            "name": obj.tournament.name,
            "slug": obj.tournament.slug
        }

    class Meta:
        model = Bout
        exclude = ('pkid', 'id', 'deleted')


class UpdateBoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bout
        exclude = ('pkid','id','deleted')
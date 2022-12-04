from rest_framework import serializers

from journal_apps.bouts.models import Bout
from journal_apps.fencers.models import Fencer
from journal_apps.bouts.serializers import BoutSerializer


class FencerSerializer(serializers.ModelSerializer):
    bouts = serializers.SerializerMethodField(read_only=True)


    def get_bouts(self, obj):
        fencer_a_bouts = obj.fencer_a.all()
        fencer_b_bouts = obj.fencer_b.all()
        fencer_bouts = fencer_a_bouts | fencer_b_bouts
        serializer = BoutSerializer(fencer_bouts, many=True)
        return serializer.data
    
    class Meta:
        model = Fencer
        exclude = ('pkid', 'id', 'deleted')


class UpdateFencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fencer
        exclude = ('pkid','id','deleted')
from rest_framework import serializers
# from journal_apps.bouts.models import Bout
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

class CreateFencerSerializer(serializers.ModelSerializer):
    region = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    def validate_region(self, value):
        if not value:
            return None
        # return value

        try:
             return int(value)
        except ValueError:
            raise serializers.ValidationError('Valid integer is required')


    class Meta:
        model = Fencer
        fields = (
            'user',
            'usa_fencing_info',
            'first_name',
            'last_name',
            'club',
            'club2',
            'school',
            'division',
            'region',
            'nationality',
            'handed',
            'primary_grip',
            'usaf_rating_epee',
            'usaf_rating_sabre',
            'usaf_rating_foil',
            'ref_rating_epee',
            'ref_rating_sabre',
            'ref_rating_foil',
            'custom_rating',
            'tactical_description',
            'favorite_actions',
            'notes'
        )

class ChooseFencerSerializer(serializers.ModelSerializer):
    fencer_name = serializers.SerializerMethodField(read_only=True)

    def get_fencer_name(self, obj):
        return str(obj.last_name) + ", " + str(obj.first_name)


    class Meta:
        model = Fencer
        fields = ('slug', 'fencer_name')
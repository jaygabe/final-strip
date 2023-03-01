from rest_framework import serializers

from journal_apps.usaf_data.models import USAFencingInfo

class FencerRecordSerializer(serializers.Serializer):
    class Meta:
        model = USAFencingInfo
        exclude = ['id']


class USAFencingInfoSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField(read_only=True)
    club = serializers.CharField(source="club1_abv")
    usafid = serializers.CharField(source="member_id")

    def get_name(self, obj):
        return str(obj.last_name) + ", " + str(obj.first_name)

    class Meta:
        model = USAFencingInfo
        fields = ['name', 'club1_abv', 'usafid']

from rest_framework import serializers


class FilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(user=self.context['request'].user, edition__hide=False)
        return super(FilteredListSerializer, self).to_representation(data)
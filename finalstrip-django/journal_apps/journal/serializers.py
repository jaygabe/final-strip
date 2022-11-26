from pyexpat import model
from rest_framework import serializers

from journal_apps.lessons.models import Lesson
from journal_apps.usaf_data.models import USAFencingInfo
from journal_apps.tournaments.models import Tournament
from journal_apps.events.models import Event
from journal_apps.bouts.models import Bout
from journal_apps.fencers.models import Fencer


class FencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fencer
        exclude = ('id',)


class AddFencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fencer
        exclude = ('id','slug')





class AddTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        exclude = ('id','slug', 'user')

    # def create(self, validated_data):
    #     validated_data['user'] = self.context['request'].user
    #     return super(AddTournamentSerializer, self).create(validated_data)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('id',)


class AddEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('id','slug')


class BoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bout
        exclude = ('id',)


class AddBoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bout
        exclude = ('id','slug')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ('id',)  

class AddLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ('id','slug')    


class USAFencingSerializer(serializers.ModelSerializer):
    class Meta:
        model = USAFencingInfo
        exclude = ()      
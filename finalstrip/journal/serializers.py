from pyexpat import model
from rest_framework import serializers
from .models import Fencer, Tournament, Event, Bout, Lesson, USAFencingInfo


class FencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fencer
        exclude = ('id',)


class AddFencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fencer
        exclude = ('id','slug')


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        exclude = ('id',)


class AddTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        exclude = ('id','slug')


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
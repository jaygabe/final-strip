from pyexpat import model
from rest_framework import serializers
from .models import Fencer, Tournament, Event, Bout, Lesson, USAFencingInfo

class FencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fencer
        exclude = ('id')


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        exclude = ('id')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('id')


class BoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bout
        exclude = ('id')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ('id')      
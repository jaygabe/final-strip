from urllib import response
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions, status

from journal_apps.lessons.models import Lesson
from journal_apps.usaf_data.models import USAFencingInfo
from journal_apps.tournaments.models import Tournament
from journal_apps.events.models import Event
from journal_apps.bouts.models import Bout
from journal_apps.fencers.models import Fencer


from journal_apps.authentication.models import User
from journal_apps.social.models import ConnectFencers
from .serializers import FencerSerializer, EventSerializer, BoutSerializer, LessonSerializer, USAFencingSerializer
from .serializers import AddFencerSerializer, AddEventSerializer, AddBoutSerializer, AddLessonSerializer
from journal_apps.authentication.authentication import JWTAuthentication



def get_requested_model(Model):
    pass


class FencerView(APIView):
    # authentication_classes = [JWTAuthentication]
    serializer_classes = [FencerSerializer, BoutSerializer, AddFencerSerializer]

    def get(self, request, slug=None):
        if slug != None:
            fencer = get_object_or_404(Fencer, user=request.user, slug=slug)
            user_bouts = Bout.objects.filter(user=request.user)
            bouts = user_bouts.filter(Q(fencer_a__slug=slug)|Q(fencer_b__slug=slug))
            data = {
                'Fencer': FencerSerializer(fencer).data, 
                'Bouts': BoutSerializer(bouts, many=True).data
            }
        else:
            fencer = get_list_or_404(Fencer, user=request.user)
            data = {
                'Fencer': FencerSerializer(fencer, many=True).data, 
            }
        
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, slug=None):
        serializer = self.serializer_classes[2](data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'Good Request': 'Fencer Added'}, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid Fencer Data...'}, status=status.HTTP_400_BAD_REQUEST)


class EventView(APIView):
    # authentication_classes = [JWTAuthentication]
    serializer_classes = [EventSerializer, AddEventSerializer]

    def get(self, request, slug):
        if slug:
            event = get_object_or_404(Event, slug=slug) # user=request.user,
            bouts = get_list_or_404(Bout, event=event.id)
            data = {
                'event': EventSerializer(event).data,
                'bouts': BoutSerializer(bouts, many=True).data
            }
        else:
            raw_data = get_list_or_404(Event) # user=request.user
            data = self.serializer_classes[0](raw_data, many=True).data

        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request, slug=None):
        serializer = self.serializer_classes[1](data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'Good Request': 'Event Added'}, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid Event Data...'}, status=status.HTTP_400_BAD_REQUEST)


class BoutView(APIView):
    # authentication_classes = [JWTAuthentication]
    serializer_classes = [BoutSerializer, AddBoutSerializer]

    def get(self, request, slug):
        if slug != None:
            bout = get_object_or_404(Bout, user=request.user, slug=slug)
            data = self.serializer_classes[0](bout).data
        else:
            bout = get_list_or_404(Bout, user=request.user)
        
        data = {
                'Bout': BoutSerializer(bout).data
            }
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request, slug=None):
        serializer = self.serializer_classes[1](data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'Good Request': 'Bout Added'}, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid Bout Data...'}, status=status.HTTP_400_BAD_REQUEST)


class LessonView(APIView):
    # authentication_classes = [JWTAuthentication]
    serializer_classes = [LessonSerializer, AddLessonSerializer]

    def get(self, request, slug):
        if slug != None:
            lesson = get_object_or_404(Lesson, user=request.user, slug=slug)
            data = self.serializer_classes[0](lesson).data
        else:
            lesson = get_list_or_404(Lesson, user=request.user)
        
        data = {
                'Lesson': LessonSerializer(lesson).data
            }
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request, slug=None):
        serializer = self.serializer_classes[1](data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'Good Request': 'Lesson Added'}, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid Lesson Data...'}, status=status.HTTP_400_BAD_REQUEST)


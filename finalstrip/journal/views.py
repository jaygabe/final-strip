from urllib import response
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions, status

from .models import Fencer, Tournament, Event, Bout, Lesson, USAFencingInfo
from authentication.models import User
from social.models import ConnectFencers
from .serializers import FencerSerializer, TournamentSerializer, EventSerializer, BoutSerializer, LessonSerializer, USAFencingSerializer
from authentication.authentication import JWTAuthentication


def profile_page(request, user_id):

    user = request.user
    viewed_user = User.objects.get(pk=user_id)
    # bouts = Bout.objects.get()
    tournaments = Tournament.objects.filter(user__id=user_id)

    connect_fencers = ConnectFencers.objects.filter(Q(coach__id=user_id) | Q(student__id=user_id))
    complete = connect_fencers.filter(Q(s_accepts=True) and Q(c_accepts=True))
    incomplete = connect_fencers.filter((Q(s_accepts=True) and Q(c_accepts=False)) or (Q(s_accepts=False) and Q(c_accepts=True)))

    students = complete.filter(Q(connected=True) and Q(coach__id=user_id))
    coaches = complete.filter(Q(connected=True) and Q(student__id=user_id))
    pending_students = incomplete.filter(Q(connected=False) and Q(coach__id=user_id))
    pending_coaches = incomplete.filter(Q(connected=False) and Q(student__id=user_id))
    testing = [False]

    context = {
        'viewed_user': viewed_user,
        'students': students,
        'coaches': coaches,
        'pending_students': pending_students,
        'pending_coaches': pending_coaches,
        'all_connections': connect_fencers,
        'testing': testing,
    }

    return render(request, 'authentication/auth_accounts.html', context)



class FencerView(APIView):
    # authentication_classes = [JWTAuthentication]
    serializer_classes = [FencerSerializer, BoutSerializer]

    def get(self, request, slug):

        fencer = get_object_or_404(Fencer, user=request.user, slug=slug)
        user_bouts = Bout.objects.filter(user=request.user)
        bouts = user_bouts.filter(Q(fencer_a__slug=slug)|Q(fencer_b__slug=slug))

        data = {
            'Fencer': FencerSerializer(fencer).data, 
            'Bouts': BoutSerializer(bouts, many=True).data
        }

        return Response(data, status=status.HTTP_200_OK)


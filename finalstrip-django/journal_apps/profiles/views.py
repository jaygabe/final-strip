from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.db.models import Q
from django.contrib.auth import get_user_model

from journal_apps.social.models import ConnectFencers
from journal_apps.tournaments.models import Tournament

User = get_user_model()

#  change to a class view for edits
# differentiate profile owner from stranger
def profile_page(request, user_id):

    
    user = request.user
    viewed_user = User.objects.get(pk=user_id)  # this is a bad thing
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

    # this should probably be serialized and should be private unless user.
    data = {
        'viewed_user': viewed_user,
        'students': students,
        'coaches': coaches,
        'pending_students': pending_students,
        'pending_coaches': pending_coaches,
        'all_connections': connect_fencers,
        'testing': testing,
    }

    return Response(data, status=status.HTTP_200_OK) 
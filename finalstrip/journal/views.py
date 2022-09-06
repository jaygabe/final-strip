from django.shortcuts import render
from django.db.models import Q

from authentication.models import User
from social.models import ConnectFencers
from .models import Tournament

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


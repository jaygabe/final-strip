from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.db.models import Max, Q, Sum
from django.contrib.auth.decorators import login_required
from . import forms
from . import utils 

from .models import *

"""
TODOS:

[] add messages for broken forms
[] add search functionality 
[] import usafencing info
[] integrate usa fencing data into personal fencer list
[] add error handling if form is invalid
[] use form.user.queryset = User.objects.filter(user=user) to query only items related to that user.
[] use related key in queries to source data faster
[] new fencer submit should go back to previous page
[] coaches dashboard
"""

@login_required
def journal(request):
    context = {}
    return render(request, 'journal/journal.html', {})

# see all lessons for given user
@login_required
def lesson(request):

    submitted = False
    if request.method == 'POST':
        form = forms.LessonForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/journal/lesson?submitted=True')
        else:
            lessons = Lesson.objects.all()
            context = {
                'lessons': lessons,
                'LessonForm': form,
                'submitted': submitted,
            }
            return render(request, 'journal/lesson.html', context)
    else:
        form = forms.LessonForm   
        lessons = Lesson.objects.all()

        if 'submitted' in request.GET:
                submitted = True

    context = {
        'lessons': lessons,
        'LessonForm': form,
        'submitted': submitted,
    }

    return render(request, 'journal/lesson.html', context)


# this is broken on the template 
# view individual lesson and edit if choose
@login_required
def lesson_view(request, lesson_id):
    
    lesson = get_object_or_404(Lesson, id=lesson_id)
    form = forms.LessonForm(instance=lesson, user=request.user)

    submitted = False
    if request.method == 'POST':
        form = forms.LessonForm(request.POST)
        print('form errors: ', form.errors)
        print('form non-field errors: ', form.non_field_errors())
        print('valid form? ', form.is_valid())  #   this is broken on the template
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/journal/lesson/' + lesson_id + '?submitted=True')
        else:
            lesson = get_object_or_404(Lesson, id=lesson_id)
            context = {
                'lesson': lesson,
                'LessonForm': form,
                'submitted': submitted,
            }
            return render(request, 'journal/lesson_view.html', context)

    context = {
        'lesson': lesson,
        'lessonForm': form,
        'lesson_id': lesson_id,
    }

    return render(request, 'journal/lesson_view.html', context)


# See all tournaments in their own cards that can be clicked
@login_required
def tournaments(request):

    submitted = False
    if request.method == 'POST':
        form = forms.TournamentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/journal/tourn?submitted=True')
        else:
            tournaments = Tournament.objects.filter(user=request.user)
            context = {
                'tournaments': tournaments,
                'tournamentForm': form,
                'submitted': submitted,
            }
            return render(request, 'journal/tournament.html', context)
    else:
        form = forms.TournamentForm   
        tournaments = Tournament.objects.filter(user=request.user)

        if 'submitted' in request.GET:
                submitted = True

    context = {
        'tournaments': tournaments,
        'tournamentForm': form,
        'submitted': submitted,
    }

    return render(request, 'journal/tournament.html',context)
    

# once a tournament is selected find the bouts
@login_required
def tournement_view(request, tourn_id):
    # checks if we receive the form and is valid then saves it
    submitted = False
    if request.method == 'POST':
        form = forms.BoutForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.tournament = Tournament.objects.filter(pk=tourn_id).first()
            instance.save()
        else:
            
            bouts = Bout.objects.filter(tournament=tourn_id)
            context = {
                'bouts': bouts,
                'round': round_list,
                'boutForm': form,
                'tourn_id': tourn_id,
                }
            
            return render(request, 'journal/tournament_view.html',context)
        
    else:
        form = forms.BoutForm
        if 'submitted' in request.GET:
                submitted = True


    if Tournament.objects.filter(id=tourn_id).exists():
        bouts = Bout.objects.filter(tournament=tourn_id)
    else:
        bouts = []
        raise Http404

    # grab list of rounds
    max_round = Bout.objects.filter(tournament=tourn_id).aggregate(Max('round'))
    if max_round['round__max'] == None:
        round_list = []
    else:
        round_list = [x+1 for x in range(max_round['round__max'])]

    context = {
        'bouts': bouts,
        'round': round_list,
        'boutForm': form,
        'tourn_id': tourn_id,
    }
    
    return render(request, 'journal/tournament_view.html',context)


# view details of a bout given the tournement and bout id
@login_required
def bout_view(request, tourn_id, bout_id):
    bout = Bout.objects.get(id=bout_id)
    context = {
        'bout': bout,
        'tourn_id': tourn_id
    }
    return render(request, 'journal/bout.html',context)


# view data on a fencer with a certain id
@login_required
def fencer_view(request, fencer_id):

    fencer_pro = get_object_or_404(Fencer, id=fencer_id)
    user_bouts = Bout.objects.filter(user=request.user)
    bouts = user_bouts.filter(Q(fencer_a__pk=fencer_id)|Q(fencer_b__pk=fencer_id))

    context = {
        'fencer': fencer_pro,
        'bouts': bouts,
        }

    return render(request, 'journal/fencer_view.html',context)


# search for fencers in a list
@login_required
def fencer(request):
     # checks if we receive the form and is valid then saves it
    submitted = False
    if request.method == 'POST':
        form = forms.FencerForm(request.POST)
        print(form.errors)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/journal/fencer?submitted=True')
        else:

            fencers = Fencer.objects.filter(user=request.user)
            context = {
                'fencers': fencers,
                'FencerForm': form,
                'submitted': submitted,
            }
            return render(request, 'journal/fencer.html', context)
    else:
        form = forms.FencerForm   
        fencers = Fencer.objects.filter(user_id=request.user)

        if 'submitted' in request.GET:
                submitted = True

    context = {
        'fencers': fencers,
        'form': forms.FencerForm,
        'submitted': submitted,
    }

    return render(request, 'journal/fencer.html',context)


def fencer_profile(request, profile_id):
    
    if profile_id == request.user:
        return my_profile(request)

    profile = User.objects.get(pk=profile_id)
    tournaments_recorded = Tournament.objects.filter(user=profile_id).count()
    user_bouts = Bout.objects.filter(user__id=profile_id)

    utils.find_age_group()
    total = utils.my_bout_query_stats(user_bouts=user_bouts)

    context = {
        'profile': profile,
        'tournaments_recorded': tournaments_recorded,
        'total': total,
    }
    
    return render(request, 'journal/fencer_profile.html',context)

@login_required
def my_profile(request):
    
    profile_id = request.user

    profile = User.objects.get(pk=profile_id)
    user_bouts = Bout.objects.filter(user__id=profile_id)
    tournaments = Tournament.objects.filter(user=profile_id) # might not need this on this page
    tournaments_count = tournaments.count()

    age_groups = utils.find_age_group()
    total = utils.my_bout_query_stats(user_bouts=user_bouts)
    pools = utils.my_bout_query_stats(user_bouts=user_bouts, bout_type='pool')
    de = utils.my_bout_query_stats(user_bouts=user_bouts, bout_type='DE')

    context = {
        'profile': profile,
        'tournaments_count': tournaments_count,
        'total': total,
        'pools': pools,
        'de': de,

    }
    
    return render(request, 'journal/my_profile.html',context)



# Eventually turn this into a CRON job and done automatically maybe weekly on wednesdays?
from .load_usa_fencing_membership import load_membership_data 
def manual_reload(request):
    test_data = load_membership_data()
    context ={'testing': test_data}
    return render(request, 'journal/test.html',context)


def test(request):

    #coach_requests = User.objects.filter(student = request.user.id)
    # connected_coaches = ConnectFencers.objects.filter(student=request.user)
    # connected_coaches = ConnectFencers.objects.filter(s_accepts=True)
    # coach_requests = User.objects.filter(coach__in=connected_coaches)
    
    test_data = load_membership_data()

    context ={
        'testing': test_data
    }

    return render(request, 'journal/test.html',context)


"""
# sandox for forms
def tournament_form(request):
    submitted = False
    if request.method == 'POST':
        form = tournament_form(request.POST)
        if form.is_valid():
            form.save()

    form = forms.TournamentForm
    context = {'form' : form}
    return render(request, 'Journal/tournament_form.html',context)
    # return HttpResponse('Putin is a sad little man')

"""
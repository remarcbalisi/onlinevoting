from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, PositionForm, ElectionForm, PartyForm, CollegeForm, CandidateForm, VoteForm, BulletinForm
from .models import User, Election, Position, Party, College, Candidate, Vote, Bulletin
from django.http import Http404

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.contrib import messages

def user_add(request):
    if request.user.is_authenticated() and request.user.is_admin:
        try:
            if request.method == 'POST':
                idnum = request.POST['id_number']
                fname = request.POST['first_name']
                mname = request.POST['middle_name']
                lname = request.POST['last_name']
                age = request.POST['age']
                course = request.POST['course']
                year = request.POST['year']
                contact_number = request.POST['contact_number']
                email = request.POST['email']
                password = request.POST['password']

                user2 = User.objects.create_user(id_number=idnum, password=password)
                user2.email = email
                user2.first_name = fname
                user2.middle_name = mname
                user2.last_name = lname
                user2.age = age
                user2.course = course
                user2.year = year
                user2.contact_number = contact_number
                user2.save()

                success = "User successfully added!"
                return render(request, 'system/user_add.html', {'success': success})

            else:
                form = UserForm()

        except:
            exist = "id number already exist"
            form = UserForm()
            return render(request, 'system/user_add.html', {'exist': exist})

        return render(request, 'system/user_add.html', {'form': form})

    elif not request.user.is_authenticated():
        return redirect('system.views.user_login')

def user_login(request):

    if request.method == 'POST':
        try:
            idnum = request.POST['id_number']
            password = request.POST['password']
            user = authenticate(id_number=idnum, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect('system.views.user_home')

            else:
                failed = "login failed!"
                return render(request, 'system/user_login.html', {'failed': failed})

        except User.DoesNotExist:
            failed = "login failed!"
            return render(request, 'system/user_login.html', {'failed': failed})

    elif request.user.is_authenticated():
        return redirect('system.views.user_home')

    elif not request.user.is_authenticated():
        return render(request, 'system/user_login.html')

def user_home(request):
    if request.user.is_authenticated():
        user = get_object_or_404(User, pk=request.user.pk)

        if user.is_admin:
            return render(request, 'system/index3.html', {'user': user})

        else:
            return HttpResponse("NOT ADMIN!")
    else:
        return redirect(request, 'system.views.user_login')	

def user_logout(request):

    if request.user.is_authenticated():
        logout(request)
        return redirect('system.views.user_login')

    else:
        return redirect('system.views.user_login')

def position_add(request):

    if request.user.is_authenticated and request.user.is_admin:
        try:
            if request.method == 'POST':
                form = PositionForm(request.POST)

                position = form.save()
                position.save()

                form = PositionForm()
                success = "Position successfully added!"
                return render(request,'system/position_add.html', {'form': form, 'success': success})

            else:
                form = PositionForm()
                return render(request,'system/position_add.html', {'form':form})

        except:
            exist = "Position already exist"
            form = PositionForm()
            return render(request,'system/position_add.html', {'form':form, 'exist': exist})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def position_view(request):

    if request.user.is_authenticated() and request.user.is_admin:
        try:
            positions = Position.objects.all()
            colleges = College.objects.all()
            candidates = Candidate.objects.all()
            parties = Party.objects.all()
            return render(request, 'system/view_position.html', {'positions': positions, 'colleges': colleges,
                                                                 'candidates': candidates, 'parties': parties})

        except:
            error = "No existing position!"
            return render(request, 'system/view_position.html', {'positions': positions})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def position(request, pk):

    if request.user.is_authenticated() and request.user.is_admin:
        try:
            positions = Position.objects.all()
            candidates = Candidate.objects.filter(position_id=pk).all()
            return render(request, 'system/position.html', {'positions': positions, 'candidates': candidates})

        except:
            error = "No existing position!"
            return render(request, 'system/position.html', {'positions': positions})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def election_add(request):

    if request.user.is_authenticated() and request.user.is_admin:
        try:
            if request.method == 'POST':
                form = ElectionForm(request.POST)

                election = form.save()
                election.save()
                success = "Election successfully added!"
                form = ElectionForm()
                return render(request,'system/election_add.html', {'form':form, 'success': success})

            else:
                form = ElectionForm()
                return render(request,'system/election_add.html', {'form':form})

        except:
            exist = "Election year already exist"
            form = ElectionForm()
            return render(request,'system/election_add.html', {'form':form, 'exist': exist})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def party_add(request):

    if request.user.is_authenticated and request.user.is_admin:
        try:
            if request.method == 'POST':
                form = PartyForm(request.POST)

                party = form.save()
                party.save()

                form = PartyForm()
                success = "Party successfully added!"
                elections = Election.objects.all()
                return render(request,'system/party_add.html', {'form': form, 'success': success, 'elections': elections})

            else:
                elections = Election.objects.all()
                form = PartyForm()
                return render(request,'system/party_add.html', {'form':form, 'elections' :elections})

        except:
            exist = "Party already exist"
            form = PartyForm()
            elections = Election.objects.all()
            return render(request,'system/party_add.html', {'form':form, 'exist': exist, 'elections': elections})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def party_view(request):

    if request.user.is_authenticated() and request.user.is_admin:
        try:
            candidate = Candidate.objects.all()
            elections = Election.objects.all()
            parties = Party.objects.all()
            return render(request, 'system/party_view.html', {'candidate':candidate, 'elections' :elections, 'parties':parties})

        except:
            error = "No party to display"
            return render(request, 'system/party_view.html',{'parties':parties})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def party(request, pk):

    if request.user.is_authenticated() and request.user.is_admin:
        try:
            parties = Party.objects.all()
            candidate = Candidate.objects.filter(party_id=pk).all()
            return render(request, 'system/party.html', {'parties': parties, 'candidate': candidate})

        except:
            error = "No party to display!"
            return render(request, 'system/party.html', {'parties': parties})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def college_add(request):

    if request.user.is_authenticated and request.user.is_admin:
        try:
            if request.method == 'POST':
                form = CollegeForm(request.POST)

                college = form.save()
                college.save()

                form = CollegeForm()
                success = "College successfully added!"
                colleges = College.objects.all()
                return render(request,'system/college_add.html', {'form': form, 'success': success})

            else:
                colleges = College.objects.all()
                form = CollegeForm()
                return render(request,'system/college_add.html', {'form':form})

        except:
            exist = "College already exist"
            form = CollegeForm()
            colleges = College.objects.all()
            return render(request,'system/college_add.html', {'form':form, 'exist': exist})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def college_view(request):

    if request.user.is_authenticated():
        try:
            positions = Position.objects.all()
            colleges = College.objects.all()
            candidates = Candidate.objects.all()
            parties = Party.objects.all()
            return render(request, 'system/view_college.html', {'positions': positions, 'colleges': colleges,
                                                                 'candidates': candidates, 'parties': parties})

        except:
            error = "No existing college!"
            return render(request, 'system/view_college.html', {'positions': positions})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def college(request, pk):

    if request.user.is_authenticated() and request.user.is_admin:
        try:
            positions = Position.objects.all()
            candidates = Candidate.objects.filter(college_id=pk).all()
            return render(request, 'system/college.html', {'positions': positions, 'candidates': candidates})

        except:
            error = "No existing position!"
            return render(request, 'system/college.html', {'positions': positions})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def candidate_add(request):

    if request.user.is_authenticated and request.user.is_admin:
        try:
            if request.method == 'POST':
                form = CandidateForm(request.POST)
                
                candidate = form.save()
                candidate.save()

                success = "Candidate successfully added!"
                elections = Election.objects.all()
                positions = Position.objects.all()
                colleges = College.objects.all()
                parties = Party.objects.all()
                form = CandidateForm()
                return render(request,'system/candidate_add.html', {'form':form, 'success': success, 'elections' :elections,
                                                                'positions': positions, 'colleges':colleges, 'parties':parties})

            else:
                elections = Election.objects.all()
                positions = Position.objects.all()
                colleges = College.objects.all()
                parties = Party.objects.all()
                form = CandidateForm()
                return render(request,'system/candidate_add.html', {'form':form, 'elections' :elections,
                                                                'positions': positions, 'colleges':colleges, 'parties':parties})

        except:
            exist = "Please Try Again!"
            form = CandidateForm()
            return render(request,'system/candidate_add.html', {'form':form, 'exist': exist})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def candidate_view(request):
    if request.user.is_authenticated():
        try:
            candidate = Candidate.objects.all()
            elections = Election.objects.all()
            positions = Position.objects.all()
            colleges = College.objects.all()
            parties = Party.objects.all()
            return render(request, 'system/candidate_view.html', {'candidate':candidate, 'elections' :elections,
                                                                'positions': positions, 'colleges':colleges, 'parties':parties})
         
        except:                                                       
            error = " No candidates to display"
            return render(request,'system/candidate_view.html', {'candidate':candidate, 'elections' :elections,
                                                                'positions': positions, 'colleges':colleges, 'parties':parties})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

@login_required
def vote(request):
    candidates = Candidate.objects.all()

    # select 1 election that is active
    election = Election.objects.all().filter(is_active=True)
    positions = Position.objects.all()
    user = get_object_or_404(User, pk=request.user.pk)
    button = True

    try:
        if len(election) == 1:
            if user.is_voted == False:
                if request.method == 'POST':
                    vote_formset = VoteForm(request.POST)

                    if vote_formset.is_valid():
                        vote = vote_formset.save()
                        vote.save()
                        vote.election_id = election[0]
                        vote.user_id = user
                        vote.vote_init()
                        vote.save()
                        user.is_voted=True
                        user.save()

                        success = "successfully voted!"
                        button = False
                        return render(request,'system/vote.html', {'success': success})

                else:
                    form = VoteForm()
                    return render(request,'system/vote.html', {'form':form, 'candidates': candidates,
                                                               'election': election, 'user': user,
                                                               'positions': positions,
                                                               'button': button})

            elif user.is_voted == True:
                exist = "You already voted!"
                button = False
                return render(request,'system/vote.html', {'exist': exist})

        elif len(election) == 0:
            exist = "Eleciton is not active!"
            return render(request,'system/vote.html', {'exist': exist})

    except:
        return render(request,'system/vote.html', {'candidates': candidates,
                                                       'election': election, 'user': user,
                                                       'positions': positions,
                                                       'button': button})

def bulletin_update(request):

    if request.user.is_authenticated and request.user.is_admin:
        try:
            if request.method == 'POST':

                form = BulletinForm(request.POST)

                bulletin = form.save()
                bulletin.save()

                form = BulletinForm()
                success = "Bulletin successfully updated!"
                return render(request,'system/bulletin_update.html', {'form': form, 'success': success})

            else:
                form = BulletinForm()
                return render(request,'system/bulletin_update.html', {'form':form})

        except:
            exist = "Already exist"
            form = BulletinForm()
            return render(request,'system/bulletin_update.html', {'form':form, 'exist': exist})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

def bulletin_view(request):

    if request.user.is_authenticated() and request.user.is_admin:
        try:
            bulletin = Bulletin.objects.all()
            return render(request, 'system/view_bulletin.html', {'bulletin': bulletin})

        except:
            error = "No existing announcement!"
            return render(request, 'system/view_bulletin.html', {'bulletin': bulletin})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')

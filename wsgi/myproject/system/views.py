from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, PositionForm, ElectionForm, PartyForm, CollegeForm, VoteForm
from .models import User, Election, Position, Party, College, Vote, Candidate
from django.http import Http404

def user_add(request):
    if request.user.is_authenticated() and request.user.is_admin:
        try:
            if request.method == 'POST':
                idnum = request.POST['id_number']
                fname = request.POST['first_name']
                lname = request.POST['last_name']
                contact_number = request.POST['contact_number']
                email = request.POST['email']
                password = request.POST['password']

                user2 = User.objects.create_user(id_number=idnum, password=password)
                user2.email = email
                user2.first_name = fname
                user2.last_name = lname
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

    if request.user.is_authenticated() and request.user.is_admin:
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

def vote(request):

    if request.user.is_authenticated and request.user.is_admin:
        candidates = Candidate.objects.all()
        election = Election.objects.all().filter(is_active=True)
        positions = Position.objects.all()
        user = get_object_or_404(User, pk=request.user.pk)

        try:
            if request.method == 'POST':
                candidate_id_list = request.POST.getlist('candidate_id')
                counter = 0

                for candidate_list in candidate_id_list:
                    candidate_pk = candidate_id_list[counter]
                    print candidate_id_list
                    print candidate_pk
                    print election
                    candidate = get_object_or_404(Candidate, pk=candidate_pk)
                    print candidate
                    print user
                    vote = Vote.objects.create(candidate_id=candidate)
                    vote.save()
                    print "1"
                    vote.election_id = election
                    vote.save()
                    vote.user_id = user
                    vote.save()
                    counter = counter+1

                return HttpResponse("added!")

            else:
                form = VoteForm()
                return render(request,'system/vote.html', {'form':form, 'candidates': candidates,
                                                            'election': election, 'user': user,
                                                            'positions': positions})

        except:
            exist = "ERROR!"
            form = VoteForm()
            return render(request,'system/vote.html', {'form':form, 'exist': exist})

    elif not request.user.is_authenticated:
        return redirect('system.views.user_login')
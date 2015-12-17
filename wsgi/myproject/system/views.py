from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, PositionForm, ElectionForm, PartyForm, CollegeForm, CandidateForm, VoteForm, BulletinForm
from .models import User, Election, Position, Party, College, Candidate, Vote, Bulletin, Tally
from django.http import Http404

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.contrib import messages

@login_required
def user_add(request):

    colleges = College.objects.all()

    if request.user.is_admin:
        try:
            if request.method == 'POST':
                idnum = request.POST['id_number']
                fname = request.POST['first_name']
                mname = request.POST['middle_name']
                lname = request.POST['last_name']
                address = request.POST['address']
                course = request.POST['course']
                year = request.POST['year']
                contact_number = request.POST['contact_number']
                email = request.POST['email']
                password = request.POST['password']
                college_id = request.POST['college_id']

                user2 = User.objects.create_user(id_number=idnum, password=password)
                user2.email = email
                user2.first_name = fname
                user2.middle_name = mname
                user2.last_name = lname
                user2.address = address
                user2.course = course
                user2.year = year
                college_instance = get_object_or_404(College, pk=college_id)
                user2.college_id = college_instance
                user2.contact_number = contact_number

                user2.save()

                success = "User successfully added!"
                return render(request, 'system/user_add.html', {'success': success, 'colleges':colleges})

            else:
                form = UserForm()
                return render(request, 'system/user_add.html', {'colleges':colleges})

        except KeyError:
            return KeyError

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
				return render(request, 'system/user_login.html', {'failed':failed})

		except User.DoesNotExist:
			failed = "login Failed!"
			return render(request, 'system/user_login.html', {'failed': failed})

	elif request.user.is_authenticated():
		return redirect('system.views.user_home')

	elif not request.user.is_authenticated():
		return render(request, 'system/user_login.html')

@login_required
def user_home(request):
	user = get_object_or_404(User, pk=request.user.pk)

	if user.is_admin:
		return render(request, 'system/index3.html', {'user': user})

	elif not user.is_admin:
		return redirect('system.views.voters_view')	

def user_logout(request):

	if request.user.is_authenticated():
		logout(request)
		return redirect('system.views.user_login')

	else:
		return redirect('system.views.user_login')

@login_required
def user_profile(request, user_pk):
	if request.user.is_authenticated():
		user = User.objects.get(pk=request.user.pk)
		user_prof = User.objects.get(pk=user_pk)

		if user.is_admin:
			return render(request, 'system/user_profile.html', {'user':user, 'user_prof': user_prof})

		elif not user.is_admin:
			return render(request, 'system/user_profile.html', {'user':user, 'user_prof':user_prof})

@login_required
def user_view(request):
	user = get_object_or_404(User, pk=request.user.pk)
	try:
		users = User.objects.all()
		return render(request, 'system/user_view.html', {'users':users})

	except:
		error = "No users to display"
		return render(request, 'system/user_view.html', {'users':users})

@login_required
def user_update(request):
	user = get_object_or_404(Bulletin)
	colleges = College.objects.all()

	if request.user.is_admin:
		try:
			if request.method == 'POST':
				form = UserForm(request.POST, instance=user)

				if form.is_valid():
					this_user = form.save()
					this_user.save()

					success = "user profile successfully updated!"
					return render(request, 'system/user_update.html', {'success':success, 'colleges':colleges, 'user':user})

			else:
				return render(request, 'system/user_update.html', {'user':user, 'colleges':colleges})

		except:
			exist = "User Profile already updated!"
			return render(request, 'system/user_update.html', {'success':success, 'user':user, 'colleges':colleges})

@login_required
def position_add(request):
	try:
		if request.method == 'POST':
			form = PositionForm(request.POST)

			if form.is_valid():
				position = form.save()
				position.save()

				success = "Position successfully added!"
				return render(request, 'system/position_add.html', {'success': success})

			else:
				exist = "Position already exist"
				return render(request, 'system/position_add.html', {'exist':exist})

		else:
			return render(request, 'system/position_add.html')

	except:
		exist = "Position already exist"
		return render(request, 'system/position_add.html', {'exist':exist})

@login_required
def position_update(request, position_pk):
	position = get_object_or_404(Position, pk=position_pk)

	if request.user.is_admin:
		try:
			if request.method == 'POST':
				form = PositionForm(request.POST, instance=position)

				if form.is_valid():
					this_position = form.save()
					this_position.save()

					success = "Position successfully updated!"
					return redirect('system.views.position_view')
			
			else:
				return render(request, 'system/position_update.html', {'position':position})

		except:
			pass

@login_required
def position_delete(request, position_pk):
	position = get_object_or_404(Position, pk=position_pk)
	position.delete()

	return redirect('system.views.position_view')

@login_required
def position_view(request):
	if request.user.is_admin:
		try:
			positions = Position.objects.all()
			colleges = College.objects.all()
			candidates = Candidate.objects.all()
			parties = Party.objects.all()

			return render(request, 'system/view_position.html', {'positions':positions, 'colleges':colleges, 'candidates':candidates, 'parties':parties})

		except:
			error = "No existing position!"
			return render(request, 'system/view_position.html', {'positions':positions})

@login_required
def position(request, pk):
	if request.user.is_admin:
		try:
			positions = Position.objects.all()
			candidates = Candidate.objects.all().filter(position_id=pk)
			return render(request, 'system/position.html', {'positions':positions, 'candidates':candidates})

		except:
			error = "No existing position!"
			return render(request, 'system/position.html', {'positions':positions})

def election_add(request):
	if request.user.is_admin:
		try:
			if request.method == 'POST':
				form = ElectionForm(request.POST)

				if form.is_valid():
					election = form.save()
					election.save()
					success = "Election successfully added!"
					return render(request, 'system/election_add.html', {'success':success})
					
				else:
					exist = "Election year already exist"
					return render(request, 'system/election_add.html', {'exist':exist})

			else:
				return render(request, 'system/election_add.html')

		except:
			exist = "Election year already exist"
			return render(request, 'system/election_add.html', {'exist':exist})

@login_required
def election_view(request):
	if request.user.is_admin:
		try:
			election = Election.objects.all()
			return render(request, 'system/election_view.html', {'election':election})

		except:
			error = "No existing election year!"
			return render(request, 'system/election_view.html', {'election':election})

@login_required
def election_update(request):
	election = get_object_or_404(Election)

	if request.user.is_admin:
		try:
			if request.method == 'POST':
				form = ElectionForm(request.POST, instance=election)

				if form.is_valid():
					this_election = form.save()
					this_election.save()

					success = "election year successfully updated!"
					return render(request, 'system/election_update.html', {'success':success, 'election':election})

			else:
				return render(request, 'system/election_update.html', {'election':election})

		except:
			exist = "Election Year already updated!"
			return render(request, 'system/election_update.html', {'exist':exist, 'election':election})

@login_required
def election_delete(request):
	election = get_object_or_404(Election)
	election.delete()

	return redirect('system.views.election_view')

@login_required
def party_add(request):
	if request.user.is_admin:
		try:
			if request.method == 'POST':
				get_election = get_object_or_404(Election, pk=request.POST['election_id'])
				get_parties = Party.objects.filter(party_name=request.POST['party_name'], election_id=get_election)

				if len(get_parties) == 0:
					form = PartyForm(request.POST)

					if form.is_valid():
						party = form.save()
						party.save()

						success = "Party successfully added!"
						elections = Election.objects.all()
						return render(request, 'system/party_add.html', {'success':success, 'elections':elections})

				elif len(get_parties) > 0:
					exist = "Party already exist"
					elections = Election.objects.all()
					return render(request, 'system/party_add.html', {'exist':exist, 'elections':elections})

			else:
				elections = Election.objects.all()
				return render(request, 'system/party_add.html', {'elections':elections})

		except KeyError:
			return KeyError

@login_required
def party_update(request, party_pk):
    party = get_object_or_404(Party, pk=party_pk)
    elections = Election.objects.all()

    if request.user.is_admin:
        try:
            if request.method == 'POST':
                form = PartyForm(request.POST, instance=party)

                if form.is_valid():
                    this_party = form.save()
                    this_party.save()

                    default_election = this_party.election_id
                    success = "party successfully updated!"
                    return render(request, 'system/party_update.html', {'success':success, 'elections':elections, 'party':party, 'default_election':default_election})

            else:
            	default_election = party.election_id
            	return render(request, 'system/party_update.html', {'party':party, 'elections':elections, 'default_election':default_election})

        except:
        	pass

@login_required
def party_view(request):
	if request.user.is_admin:
		parties = Party.objects.all()
		try:
			elections = Election.objects.all()
			return render(request, 'system/party_view.html', {'elections':elections, 'parties':parties})

		except:
			error = "No party to display"
			return render(request, 'system/party_view.html', {'error':error, 'parties':parties})

@login_required
def delete_party(request, party_pk):
	party = get_object_or_404(Party, pk=party_pk)
	party.delete()

	return redirect('system.views.party_view')

@login_required
def party(request, pk):
	if request.user.is_admin: 
		try:
			parties = Party.objects.all()
			candidate = Candidate.objects.all().filter(party_id=pk)
			return render(request, 'system/party.html', {'parties':parties, 'candidate':candidate})

		except:
			error = "No party to display!"
			return render(request, 'system/party.html', {'parties':parties, 'error':error})

@login_required
def college_add(request):
	if request.user.is_admin:
		try:
			if request.method == 'POST':
				form = CollegeForm(request.POST)

				if form.is_valid():
					college = form.save()
					college.save()

					success = "College successfully added!"
					return render(request, 'system/college_add.html', {'success': success})

			else:
				return render(request, 'system/college_add.html')

		except:
			exist = "College already exist!"
			return render(request, 'system/college_add.html')

@login_required
def college_view(request):
	try:
		positions = Position.objects.all()
		colleges = College.objects.all()
		candidates = Candidate.objects.all()
		parties = Party.objects.all()
		return render(request, 'system/view_college.html', {'positions':positions, 'colleges':colleges, 'candidates':candidates, 'parties':parties})

	except:
		error = "No existing college!"
		return render(request, 'system/view_college.html', {'positions':positions})

@login_required
def college(request, pk):
	if request.user.is_admin:
		try:
			positions = Position.objects.all()
			candidates = Candidate.objects.filter(college_id=pk)
			return render(request, 'system/college.html', {'positions':positions, 'candidates':candidates})

		except:
			error = "No existing position!"
			return render(request, 'system/college.html', {'positions':positions})

@login_required
def candidate_add(request):
	if request.user.is_admin:
		elections = Election.objects.all()
		positions = Position.objects.all()
		parties = Party.objects.all()
		users = User.objects.all()
		colleges = College.objects.all()
		try:
			if request.method == 'POST':
				form = CandidateForm(request.POST)
				get_position = get_object_or_404(Position, pk=request.POST['position_id'])
				get_party = get_object_or_404(Party, pk=request.POST['party_id'])
				get_election = get_object_or_404(Election, pk=request.POST['election_id'])
				check_candidate = Candidate.objects.all().filter(user_id=request.POST['user_id'], election_id=get_election)
				check_candidate_party = Candidate.objects.all().filter(party_id=get_party, position_id=get_position, election_id=get_election)

				if len(check_candidate) == 0 and form.is_valid():
					if len(check_candidate_party) < get_position.slot:
						candidate = form.save()
						candidate.save()
						candidate_user_id = get_object_or_404(User, pk=candidate.user_id.pk)
						candidate.college_id = candidate_user_id.college_id
						candidate.save()

						success = "Candidate successfully added!"
						return render(request, 'system/candidate_add.html', {'success':success, 'elections':elections, 'positions':positions, 'parties':parties, 'users':users, 'colleges':colleges})

					else:
						exist = "Election %s: This %s party can only have %s %s" %(get_election, get_party.party_name, get_position.slot, get_position.position_name)
						return render(request, 'system/candidate_add.html', {'exist':exist, 'elections':elections, 'positions':positions, 'parties':parties, 'users':users, 'colleges':colleges})

				else:
					exist = "Already listed as candidate. Please try again!"
					return render(request, 'system/candidate_add.html', {'exist':exist, 'elections':elections, 'positions':positions, 'parties':parties, 'users':users, 'colleges':colleges})

			else:
				return render(request, 'system/candidate_add.html', {'elections':elections, 'positions':positions, 'parties':parties, 'users':users, 'colleges':colleges})

		except:
			exist = "Already listed as candidate. Please try again!"
			return render(request, 'system/candidate_add.html', {'exist':exist, 'elections':elections, 'positions':positions, 'parties':parties, 'users':users, 'colleges':colleges})

@login_required
def candidate_view(request):
	candidates = Candidate.objects.all()
	elections = Election.objects.all()
	positions = Position.objects.all()
	colleges = College.objects.all()
	parties = Party.objects.all()

	try:
		return render(request, 'system/candidate_view.html', {'candidates':candidates, 'elections':elections, 'positions':positions, 'colleges':colleges, 'parties':parties})

	except:
		error = "No candidates to display"
		return render(request, 'system/candidate_view.html', {'candidates':candidates, 'elections':elections, 'positions':positions, 'colleges':colleges, 'parties':parties})

@login_required
def delete_candidate(request, candidate_pk):
	candidates = get_object_or_404(Candidate, pk=candidate_pk)
	candidates.delete()

	return redirect('system.views.candidate_view')

@login_required
def vote(request):

	#select 1 election that is active
	election = Election.objects.filter(is_active=True)
	positions = Position.objects.all().order_by('id')
	candidates = Candidate.objects.all().filter(election_id=election[0
		])
	user = get_object_or_404(User, pk=request.user.pk)
	button = True

	try:
		if len(election) == 1:
			if user.is_voted == False:
				if request.method == 'POST':
					form = VoteForm(request.POST)

					if form.is_valid():
						vote = form.save()
						vote.save()
						vote.election_id = election[0]
						vote.user_id = user
						vote.vote_init()
						vote.save()
						user.is_voted=True
						user.save()

						success = "successfully voted!"
						button = False
						return render(request, 'system/vote.html', {'success':success, 'button':button})

				else:
					return render(request, 'system/vote.html', {'candidates':candidates, 'election':election, 'user':user, 'positions':positions, 'button':button})

			elif user.is_voted == True:
				exist = "You already voted!"
				button = False
				return render(request, 'system/vote.html', {'exist':exist})

		elif len(election) == 0:
			exist = "Election is not active!"
			return render(request, 'system/vote.html', {'exist':exist})

	except:
		exist = "error"
		return render(request, 'system/vote.html', {'candidates':candidates, 'election':election, 'user':user, 'positions':positions, 'button':button})

@login_required
def bulletin_add(request):
	if request.user.is_admin:
		try:
			if request.method == 'POST':
				form = BulletinForm(request.POST)

				if form.is_valid():
					bulletin = form.save()
					bulletin.save()

					success = "Bulletin successfully added!"
					return render(request, 'system/bulletin_add.html', {'success':success})

			else:
				return render(request, 'system/bulletin_add.html')

		except:
			exist = "Already exist"
			return render(request, 'system/bulletin_add.html', {'exist':exist})

@login_required
def bulletin_view(request):
	if request.user.is_admin:
		try:
			bulletin = Bulletin.objects.all()
			return render(request, 'system/view_bulletin.html', {'bulletin':bulletin})

		except:
			error = "No existing announcement!"
			return render(request, 'system/view_bulletin.html', {'bulletin':bulletin})

@login_required
def bulletin_update(request):
	bulletin = get_object_or_404(Bulletin)

	if request.user.is_admin:
		try:
			if request.method == 'POST':
				form = BulletinForm(request.POST, instance=bulletin)

				if form.is_valid():
					this_bulletin = form.save()
					this_bulletin.save()

					success = "bulletin successfully updated!"
					return redirect('system.views.bulletin_view')

			else:
				return render(request, 'system/bulletin_update.html', {'bulletin':bulletin})

		except:
			exist = "Bulletin already updated!"
			return render(request, 'system/bulletin_update.html', {'exist':exist, 'bulletin':bulletin})

@login_required
def delete_bulletin(request, bulletin_pk):
	bulletin = get_object_or_404(Bulletin, pk=bulletin_pk)
	bulletin.delete()

	return redirect('system.views.bulletin_view')

@login_required
def count_tally(request):
	if request.user.is_admin:
		election = Election.objects.all().filter(is_active=True)
		candidates = Candidate.objects.all()
		tally = Tally.objects.all().filter(election_id=election[0])

		if len(tally) == 0:
			for candidate in candidates:
				vote = Vote.objects.filter(candidate_id=candidate).count()
				save_vote = Tally.objects.create(vote_count=vote, election_id=election[0], candidate_id=candidate)
				save_vote.save()
			return redirect('system.views.view_tally')

		elif len(tally) == 1:
			return redirect('system.views.view_tally')

@login_required
def view_tally(request):
	if request.user.is_admin:
		election = Election.objects.all().filter(is_active=True)
		candidates = Candidate.objects.all().filter(election_id=election[0])

		tallies = Tally.objects.all().filter(election_id=election[0])
		return render(request, 'system/view_tally.html', {'election':election, 'candidates':candidates, 'tallies':tallies})

@login_required
def voters_view(request):

    positions = Position.objects.all()
    colleges = College.objects.all()
    candidates = Candidate.objects.all()
    parties = Party.objects.all()
    return render(request, 'system/voter/landingpage.html', {'positions': positions, 'colleges': colleges,
                                                           'candidates': candidates, 'parties': parties})

@login_required
def candidate(request, pk):

    colleges = College.objects.all()
    candidates = Candidate.objects.filter(college_id=pk)
    return render(request, 'system/voter/candidate.html', {'colleges': colleges, 'candidates': candidates})
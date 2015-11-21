from django import forms
from .models import User, Position, Election, Party, College, Vote

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['id_number', 'email', 'first_name', 'last_name', 'password', 'contact_number']


class PositionForm(forms.ModelForm):

	class Meta:
		model = Position
		fields = ['position_name']

class ElectionForm(forms.ModelForm):

	class Meta:
		model = Election
		fields = ['year',]

class PartyForm(forms.ModelForm):

	class Meta:
		model = Party
		fields = ['party_name', 'election_id']

class CollegeForm(forms.ModelForm):

	class Meta:
		model = College
		fields = ['college_name']

class VoteForm(forms.ModelForm):

	class Meta:
		model = Vote
		fields = ['candidate_id', 'election_id', 'user_id']
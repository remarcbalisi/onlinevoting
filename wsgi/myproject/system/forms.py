from django import forms
from .models import User, Position, Election, Party, College, Vote, Candidate, Bulletin

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['id_number', 'email', 'first_name', 'middle_name', 'last_name', 'address', 'course', 'year', 'college_id', 'password', 'contact_number']


class PositionForm(forms.ModelForm):

	class Meta:
		model = Position
		fields = ['position_name', 'slot']


class CollegeForm(forms.ModelForm):

	class Meta:
		model = College
		fields = ['college_name']


class CollegeForm(forms.ModelForm):

	class Meta:
		model = College
		fields = ['college_name']

class ElectionForm(forms.ModelForm):

	class Meta:
		model = Election
		fields = ['year',]

class PartyForm(forms.ModelForm):

	class Meta:
		model = Party
		fields = ['party_name', 'election_id']

class CandidateForm(forms.ModelForm):

	class Meta:
		model = Candidate
		fields = ['user_id', 'platform', 'achievements', 'life_quote', 'election_id', 'party_id', 'position_id' ]

class CollegeForm(forms.ModelForm):

	class Meta:
		model = College
		fields = ['college_name']

# class VoteForm(forms.Form):

# 	subjects = forms.ModelMultipleChoiceField(queryset=Vote.objects.all(), widget=forms.CheckboxSelectMultiple)

class VoteForm(forms.ModelForm):

	class Meta:
		model = Vote
		fields = ['candidate_id', 'election_id', 'user_id']

class BulletinForm(forms.ModelForm):

	class Meta:
		model = Bulletin
		fields = ['bulletin_info']
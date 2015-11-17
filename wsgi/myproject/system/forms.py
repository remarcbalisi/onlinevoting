from django import forms
from .models import User, Position, College

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['id_number', 'email', 'first_name', 'last_name', 'password', 'contact_number']

class PositionForm(forms.ModelForm):

	class Meta:
		model = Position
		fields = ['position_name']

class CollegeForm(forms.ModelForm):

	class Meta:
		model = College
		fields = ['college_name']
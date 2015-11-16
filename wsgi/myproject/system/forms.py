from django import forms
from .models import User, Election

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['id_number', 'email', 'first_name', 'last_name', 'password', 'contact_number']

class ElectionForm(forms.ModelForm):

	class Meta:
		model = Election
		fields = ['year',]
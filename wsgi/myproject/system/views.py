from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import User
from django.http import Http404

def index(request):
	return render(request, 'system/index2.html')

def user_add(request):

	try:
		if request.method == 'POST':

			idnum = request.POST['id_number']
			fname = request.POST['first_name']
			lname = request.POST['last_name']
			contact_number = request.POST['contact_number']
			email = request.POST['email']
			password = request.POST['password']

			user = User.objects.create_user(id_number=idnum, password=password)
			user.email = email
			user.first_name = fname
			user.last_name = lname
			user.contact_number = contact_number

			return redirect('system.views.index')

		else:
			form = UserForm()

	except:
		form = UserForm()
		return render(request, 'system/user_add.html', {'form': form})

	return render(request, 'system/user_add.html', {'form': form})
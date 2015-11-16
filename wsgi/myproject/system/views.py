from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import User
from django.http import Http404

def index(request):
    return render(request, 'system/index.html')

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

            return redirect('system.views.user_login')

        else:
            form = UserForm()

    except:
        form = UserForm()
        return render(request, 'system/user_add.html', {'form': form})

    return render(request, 'system/user_add.html', {'form': form})

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
            return render(request, 'system/user_login.html')

    elif request.user.is_authenticated():
        return redirect('system.views.user_home')

    elif not request.user.is_authenticated():
        return render(request, 'system/user_login.html')

def user_home(request):
    if request.user.is_authenticated():
        user = get_object_or_404(User, pk=request.user.pk)
        return render(request, 'system/user_home.html', {'user': user})

    else:
        return redirect(request, 'system.views.user_login')	

def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect('system.views.user_login')

    else:
        return redirect('system.views.user_login')
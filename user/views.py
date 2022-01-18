from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from user.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            return render(request, template_name='login.html', context={'error_message': 'Login failed'})


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            User.objects.create(username=username, password=make_password(password))
            return render(request, template_name='login.html', context={'message': 'Register succeed'})

        return render(request, template_name='register.html', context={'error_message': 'Register failed'})


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

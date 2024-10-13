from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def ingresar(request):
    return render(request, 'ingresar.html')


def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {'err': 'El usuario ya existe'})

        return render(request, 'signup.html', {'form': UserCreationForm, 'err': 'Las contraseñas no coinciden'})


def signout(request):
    logout(request)
    return redirect('signup.html')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        user = authenticate(
            request, email=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'err': 'Usuario o contraseña incorrecto'})
        else:
            login(request, user)
            return redirect('home.html')

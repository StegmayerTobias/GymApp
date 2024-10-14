from django.shortcuts import render, redirect

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
                    username=request.POST['email'],   
                    first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('signin')
            except IntegrityError:
                return render(request, 'signup.html', {'err': 'El usuario ya existe'})

        return render(request, 'signup.html', {'err': 'Las contraseñas no coinciden'})


def signout(request):
    logout(request)
    return redirect('ingresar')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is None:
            return render(request, 'signin.html', {'err': 'Usuario o contraseña incorrecto'})
        else:
            login(request, user)
            if request.user.is_superuser:
                return redirect('alumnos_staff')
            else:
                return redirect('home')

def rutina(request):
    return render(request, 'rutina.html')

def alumnos_staff(request):
    return render(request, 'alumnos_staff.html')

def perfilAlumno_staff(request):
   return render(request, 'perfilAlumno_staff.html')
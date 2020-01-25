from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import RegistrarUsuario, RegistrarCampeon


# Create your views here.

def index(request):
    if request.POST:
        username = request.POST.get('username',False)
        password = request.POST.get('password',False)
        
        if username and password:
            user = authenticate(request=request,username=username,
            password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('usuario:inicio'))
            else:
                messages.add_message(request, messages.INFO, 'Usuario incorrecto')
        else:
            messages.add_message(request, messages.INFO, 'Debes ingresar los datos')
    return render(request,'index.html')


def base(request):
    return render(request,'base.html',{})

def inicio(request):
    return render(request,'inicio.html',{})

def campeones(request):
    return render(request,'pagcampeones.html',{})

def registrar(request):
    if request.POST:
        form = RegistrarUsuario(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.set_password(u.password)
            u.save()
            messages.add_message(request, messages.INFO, 'Usuario Creado')
            return HttpResponseRedirect(reverse('usuario:index'))
    else:
        form = RegistrarUsuario()
    return render(request, 'registrar.html', {'form': form}) 

def registrar_campeones(request):
    if request.POST:
        form = RegistrarCampeon(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.save()
            messages.add_message(request, messages.INFO, 'Campeon Campeon')
            return HttpResponseRedirect(reverse('usuario:regcampeon'))
    else:
        form = RegistrarCampeon()
    return render(request, 'regcampeon.html', {'form': form})
 
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('usuario:index'))


def registrar_staff(request):
    if request.POST:
        form = RegistrarUsuario(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.set_password(u.password)
            u.is_staff = True
            u.save()
            messages.add_message(request, messages.INFO, 'Usuario Creado')
            return HttpResponseRedirect(reverse('usuario:regstaff'))
    else:
        form = RegistrarUsuario()
    return render(request, 'regstaff.html', {'form': form})

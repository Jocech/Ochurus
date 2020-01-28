from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Usuario, Campeon, Item
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
                if user.is_staff:
                    return HttpResponseRedirect(reverse('usuario:iniciostaff'))
                return HttpResponseRedirect(reverse('usuario:inicio'))
            else:
                messages.add_message(request, messages.INFO, 'Usuario incorrecto')
        else:
            messages.add_message(request, messages.INFO, 'Debes ingresar los datos')
    return render(request,'index.html')


def base(request):
    return render(request,'base.html',{})

@login_required(login_url="/")
def inicio(request):
    return render(request,'inicio.html',{})


@login_required(login_url="/")
def campeones(request):
    return render(request,'pagcampeones.html',{})

def listar_item(request):
    context = {
        'lista_items' : Item.objects.all()
    }
    return render(request,'listaritems.html',context)

def registrar(request):
    if request.POST:
        username = request.POST.get('username',False)
        first_name = request.POST.get('first_name',False)
        last_name = request.POST.get('last_name',False)
        password = request.POST.get('password',False)
        email = request.POST.get('email',False)
        ciudad = request.POST.get('ciudad',False)
        telefono = request.POST.get('telefono',False)
        u = Usuario(username=username,first_name=first_name,last_name=last_name,password=password,email=email,ciudad=ciudad,telefono=telefono)
        u.set_password(password)
        u.save()
        return HttpResponseRedirect(reverse('usuario:registrar'))
    return render(request, 'registrar.html')

@staff_member_required(login_url="/")
def item(request):
    if request.POST:
        nombre = request.POST.get('nombre',False)
        foto = request.FILES.get('foto',False)
        i = Item(nombre=nombre)
        if foto:
            i.foto = foto 
        i.save()
    return render(request,'items.html')

@staff_member_required(login_url="/")
def registrar_campeones(request):
    if request.POST:
        form = RegistrarCampeon(request.POST,request.FILES)
        if form.is_valid():
            u = form.save(commit=False)
            u.save()
            messages.add_message(request, messages.INFO, 'Campeon Registrado')
            return HttpResponseRedirect(reverse('usuario:regcampeon'))
    else:
        form = RegistrarCampeon()
        return render(request, 'regcampeon.html', {'form': form})

@login_required(login_url="/")
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('usuario:index'))
    
    
@staff_member_required(login_url="/")
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


def campeon_list(request):
    context = {
        'lista_campeones' : Campeon.objects.all()
    }
    return render(request,'listar.html',context)

@staff_member_required(login_url="/")
def campeon_editar(request, id_campeon):
    campeon = Campeon.objects.get(id=id_campeon)
    if request.method == 'GET':
        form = RegistrarCampeon(instance=campeon)
    else:
        form = RegistrarCampeon(request.POST,instance=campeon)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('usuario:listar'))
    return render(request, 'regcampeon.html', {'form':form,'is_update':True,'item':campeon})

@staff_member_required(login_url="/")
def campeon_borrar(request,id):
    campeon = Campeon.objects.get(pk=id)
    campeon.delete()
    messages.add_message(request, messages.INFO, 'Campeon fue borrado')
    return HttpResponseRedirect(reverse('usuario:listar'))

@staff_member_required(login_url="/")
def iniciostaff(request):
    return render(request,'iniciostaff.html')
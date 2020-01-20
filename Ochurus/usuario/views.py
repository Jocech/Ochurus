from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def base(request):
    return render(request,'base.html',{})

def inicio(request):
    return render(request,'inicio.html',{})

def campeones(request):
    return render(request,'pagcampeones.html',{})
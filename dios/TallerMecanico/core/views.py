from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Mecanico, Categoria, Auto
from .forms import ContactoForm, AutoForm

# Create your views here.

def index(request):
    mecanico = Mecanico.objects.all()
    data = {
        'mecanico': mecanico
    }
    return render(request, 'core/index.html', data)

def galeria(request):
    auto = Auto.objects.all()
    data = {
        'auto': auto
    }
    return render(request, 'core/galeria.html', data)
    
def buscador(request):
    return render(request, 'core/buscador.html')

def categoria1(request):
    return render(request, 'core/categoria1.html')

def chevrolet(request):
    return render(request, 'core/chevrolet.html')
def ford(request):
    return render(request, 'core/ford.html')
def inicio_sesion(request):
    return render(request, 'core/inicio_sesion.html')
def mazda(request):
    return render(request, 'core/mazda.html')

def mecanico(request,idMecanico):
    mecanico = Mecanico.objects.filter(primary_key=idMecanico)
    data = {
        'mecanico': mecanico
    }
    return render(request, 'core/mecanico.html', data)

def raptor(request):
    return render(request, 'core/raptor.html')
def registrar(request):
    return render(request, 'core/registrar.html')
def solicitud(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "solicitud enviada"

        else:
            data["form"] = formulario

    return render(request, 'core/solicitud.html', data)
def modificar(request):
    return render(request, 'core/autos/modificar.html')
def agregar(request):

    data = {
        'form': AutoForm()
    }
    if request.method == 'POST':
        formulario = AutoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Auto Guardado"
        else:
            data["form"] = formulario
    return render(request, 'core/autos/agregar.html', data)
def listar(request):
    return render(request, 'core/autos/listar.html')
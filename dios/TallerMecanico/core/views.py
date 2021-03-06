from django import http
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mecanico, Auto, Categoria
from .forms import ContactoForm, AutoForm

# Create your views here.

def index(request):
    mecanico = Mecanico.objects.all()
    categoria = Categoria.objects.all()
    data = {
        'mecanico': mecanico,
        'categoria': categoria
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

def categoria1(request, id):
    categoria = Categoria.objects.filter(id=id)
    auto = Auto.objects.all()
    data = {
        'categoria': categoria,
        'auto': auto
    }
    return render(request, 'core/categoria1.html', data)

def chevrolet(request):
    return render(request, 'core/chevrolet.html')
def ford(request):
    return render(request, 'core/ford.html')
def inicio_sesion(request):
    return render(request, 'core/inicio_sesion.html')
def mazda(request):
    return render(request, 'core/mazda.html')

def mecanico(request, id):
    mecanico = Mecanico.objects.filter(id=id)
    auto = Auto.objects.all()
    data = {
        'mecanico': mecanico,
        'auto': auto
    }
    return render(request, 'core/mecanico.html', data)

def auto(request, id):
    auto = Auto.objects.filter(id=id)
    data = {
        'auto': auto
    }
    return render(request, 'core/autos/auto.html', data)

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

def agregar_autos(request):

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

def listar_autos(request):
    auto = Auto.objects.all()

    data = {
        'auto': auto
    }
    return render(request, 'core/autos/listar.html', data)

def modificar_autos(request, id):

    auto = get_object_or_404(Auto, id=id)
    
    data = {
        'form': AutoForm(instance=auto)
    }

    if request.method == 'POST':
        formulario = AutoForm(data=request.POST, instance=auto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="galeria")
        else:
            data["form"] = formulario
    return render(request, 'core/autos/agregar.html', data)

def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    auto.delete()
    return redirect(to="listar_autos")
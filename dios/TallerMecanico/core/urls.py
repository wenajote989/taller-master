from django.urls import path
from .views import index, galeria, buscador, categoria1, chevrolet, auto, ford, inicio_sesion, mazda, mecanico, raptor, registrar, solicitud, modificar_autos, agregar_autos, listar_autos, eliminar_auto


urlpatterns = [
    path('', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('buscador/', buscador, name="buscador"),
    path('categoria1/<id>', categoria1, name="categoria1"),
    path('chevrolet/', chevrolet, name="chevrolet"),
    path('ford/', ford, name="ford"),
    path('inicio_sesion/', inicio_sesion, name="inicio_sesion"),
    path('mazda/', mazda, name="mazda"),
    path('mecanico/<id>', mecanico, name="mecanico"),
    path('raptor/', raptor, name="raptor"),
    path('registrar/', registrar, name="registrar"),
    path('solicitud/', solicitud, name="solicitud"),
    path('agregar-autos/', agregar_autos, name="agregar_autos"),
    path('listar-autos/', listar_autos, name="listar_autos"),
    path('modificar-autos/<id>/', modificar_autos, name="modificar_autos"),
    path('eliminar-auto/<id>', eliminar_auto, name="eliminar_auto"),
    path('auto/<id>', auto, name="auto")
    ]
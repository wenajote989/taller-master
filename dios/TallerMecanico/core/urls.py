from django.urls import path
from .views import index, galeria, buscador, categoria1, chevrolet, ford, inicio_sesion, mazda, mecanico, raptor, registrar, solicitud


urlpatterns = [
    path('', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('buscador/', buscador, name="buscador"),
    path('categoria1/', categoria1, name="categoria1"),
    path('chevrolet/', chevrolet, name="chevrolet"),
    path('ford/', ford, name="ford"),
    path('inicio_sesion/', inicio_sesion, name="inicio_sesion"),
    path('mazda/', mazda, name="mazda"),
    path('mecanico/<int:Mecanico_pk>', mecanico, name="mecanico"),
    path('raptor/', raptor, name="raptor"),
    path('registrar/', registrar, name="registrar"),
    path('solicitud/', solicitud, name="solicitud"),
]

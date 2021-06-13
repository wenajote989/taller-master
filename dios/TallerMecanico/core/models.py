from django.db import models
from django.urls import reverse
# Create your models here.

# Mecanico

class Mecanico(models.Model):
    nombre_mec = models.CharField(max_length=50,verbose_name='Nombre mecanico')
    apellido_sol = models.CharField(max_length=20,verbose_name='Apellido mec')
    descr_mec = models.TextField(max_length=255,blank=True, verbose_name='desc mec')
    img_mec = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre_mec
    
    def get_url(self):
        return reverse('mecanico',args=[self.id])
#Catergoria

class Categoria(models.Model):
    nombre_cat = models.CharField(max_length=20)
    img_cat = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre_cat


#Contacto

class Contacto(models.Model):
    nombre_cont = models.CharField(max_length=25,verbose_name='Nombre')
    apellido_cont = models.CharField(max_length=45,verbose_name='Apellidos')
    modelo_cont = models.CharField(max_length=35,verbose_name='Modelo vehiculo')
    patente_cont = models.CharField(max_length=6,verbose_name='Patente')
    email_cont = models.EmailField()
    mensaje_cont = models.TextField()

    def __str__(self):
        return self.nombre_cont


# Auto

class Auto(models.Model):
    modelo_auto = models.CharField(max_length=25,verbose_name='Modelo del Auto')
    patente_auto = models.CharField(max_length=7,verbose_name='Patente')
    img_auto = models.ImageField(upload_to="productos", null=True)
    descripcion = models.TextField(max_length=455,blank=True)

    def __str__(self):
        return self.modelo_auto

# Solicitud

#class Solicitud(models.Model):
#    nombre_sol = models.CharField(max_length=20)
#    apellido_sol = models.CharField(max_length=20)
#    modelo_sol = models.CharField(max_length=15)
#    patente_sol = models.CharField(max_length=10)
#    mail_sol = models.EmailField

# Usuario

#class Usuario(models.Model):
#    nombre_user = models.CharField(max_length=20)
#    contra_user = models.CharField(max_length=20)
#    mail_user= models.EmailField
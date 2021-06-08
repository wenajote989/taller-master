from django.db import models

# Create your models here.

# Mecanico

class Mecanico(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id Categoria')
    nombre_mec = models.CharField(max_length=50,verbose_name='Nombre mec')
    apellido_sol = models.CharField(max_length=20,verbose_name='Apellido mec')
    descr_mec = models.TextField
    img_mec = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre_mec
# Catergoria

#class Categoria(models.Model):
#    nombre_cat = models.CharField(max_length=20)

# Auto

#class Auto(models.Model):
#    nombre_auto = models.CharField(max_length=20)
#    modelo_auto = models.CharField(max_length=15)
#    patente_auto = models.CharField(max_length=10)
#    probl_auto = models.TextField
#    rep_auto = models.TextField
#    img_auto = models.ImageField

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
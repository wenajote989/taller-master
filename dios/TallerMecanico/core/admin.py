from django.contrib import admin
from .models import Mecanico

# Register your models here.

class MecanicoAdmin(admin.ModelAdmin):
    list_display = ("nombre_mec", "apellido_sol")
    



admin.site.register(Mecanico, MecanicoAdmin)
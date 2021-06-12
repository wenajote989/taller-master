from django.contrib import admin
from .models import Mecanico, Categoria, Contacto

# Register your models here.

class MecanicoAdmin(admin.ModelAdmin):
    list_display = ("nombre_mec", "apellido_sol")
    list_per_page = 2




admin.site.register(Mecanico, MecanicoAdmin)
admin.site.register(Categoria)
admin.site.register(Contacto)
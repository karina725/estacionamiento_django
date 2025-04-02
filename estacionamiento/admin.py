from django.contrib import admin
from .models import Registro  

class RegistroAdmin(admin.ModelAdmin):  
    readonly_fields = ("fecha_entrada",)

# Registrar el modelo con el admin
admin.site.register(Registro, RegistroAdmin)
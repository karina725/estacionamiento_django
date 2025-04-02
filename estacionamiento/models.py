from django.contrib.auth.models import User
from django.db import models

class Registro(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    espacio = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=20)
    estado = models.CharField(max_length=10, choices=[('OCUPADO', 'Ocupado'), ('LIBRE', 'Libre')], default='LIBRE')
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.espacio} - {self.marca} {self.modelo} - {self.placa} - {self.estado} - Entrada: {self.fecha_entrada} - Salida: {self.fecha_salida}"
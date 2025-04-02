from django.forms import ModelForm
from .models import Registro
from django import forms

# Cambié registros a Registro

class RegistroForm(ModelForm):  # También cambié registrosForm a RegistroForm
    class Meta:
        model = Registro
        fields = ['espacio', 'marca', 'modelo', 'placa', 'estado', 'fecha_salida']
        widgets ={
            'espacio': forms.TimeInput(attrs={'class': 'form-control'}),
            'marca': forms.TimeInput(attrs={'class': 'form-control'}),
            'modelo': forms.TimeInput(attrs={'class': 'form-control'}),
            'placa': forms.TimeInput(attrs={'class': 'form-control'}),
            'estado': forms.TimeInput(attrs={'class': 'form-control'}),
            'fecha_entrada': forms.TimeInput(attrs={'class': 'form-control'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
        }
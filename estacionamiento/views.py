from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import RegistroForm  
from .models import Registro
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('registro')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(), 
                    "error": 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm(), 
            "error": 'Passwords do not match'
        })


@login_required
def registro(request):
    registros = Registro.objects.filter(user=request.user)
    return render(request, 'registro.html', {'registro': registros})


def registro_terminada(request):
    registros = Registro.objects.filter(user=request.user, fecha_salida__isnull=False)
    return render(request, 'registro.html', {'registro': registros})


@login_required
def crear_registro(request):
    if request.method == 'GET':
        return render(request, 'crear_registros.html', {'form': RegistroForm()})
    else:
        try:
            form = RegistroForm(request.POST)
            new_registro = form.save(commit=False)
            new_registro.user = request.user
            new_registro.save()
            return redirect('registro')
        except ValueError:
            return render(request, 'crear_registros.html', {
                'form': RegistroForm(),
                'error': 'Por favor proporcione información válida'
            })


@login_required
def registro_detail(request, registro_id):
    registro = get_object_or_404(Registro, pk=registro_id, user=request.user)
    if request.method == 'GET':
        form = RegistroForm(instance=registro)
        return render(request, 'registro_detail.html', {'registro': registro, 'form': form})
    else:
        try:
            form = RegistroForm(request.POST, instance=registro)
            form.save()
            return redirect('registro')
        except ValueError:
            return render(request, 'registro_detail.html', {
                'registro': registro,
                'form': form,
                'error': "Error al actualizar los datos"
            })


@login_required
def registro_salida(request, registro_id):
    registro = get_object_or_404(Registro, pk=registro_id, user=request.user)
    if request.method == 'POST':
        registro.fecha_salida = timezone.now()
        registro.save()
        return redirect('registro')
    

def eliminar_salida(request, registro_id):
    registro = get_object_or_404(Registro, pk=registro_id, user=request.user)
    if request.method == 'POST':
        registro.delete()
        return redirect('registro')    


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('registro')

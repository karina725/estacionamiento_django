"""
URL configuration for estaciomaniento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from estacionamiento import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('registro/', views.registro, name='registro'),
    path('registro_terminada/', views.registro_terminada, name='registro_terminada'),
    path('registros/crear/', views.crear_registro, name='crear_registro'), 
    path('registros/<int:registro_id>/', views.registro_detail, name='registro_detail'),  
    path('registros/<int:registro_id>/salida/', views.registro_salida, name='registro_salida'), 
    path('registros/<int:registro_id>/eliminar/', views.eliminar_salida, name='eliminar_salida'), 
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
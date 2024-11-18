# Adopcion/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_animal, name='registrar_animal'),  # Ruta para registrar animales
  
    path('consulta/', views.consulta_animales, name='consulta_animales'),

path('registrar_adoptante/', views.registrar_adoptante, name='registrar_adoptante'),

path('consulta_adoptantes/', views.consulta_adoptantes, name='consulta_adoptantes'),


]


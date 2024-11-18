from django.shortcuts import render

# Create your views here.
# Adopcion/views.py

from django.shortcuts import render, redirect
from .forms import AnimalForm


def registrar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_animales')  # Redirige a la lista de animales después de registrar
    else:
        form = AnimalForm()
    
    return render(request, 'Adopcion/registrar_animal.html', {'form': form})


from django.shortcuts import render
from .models import Animal

def consulta_animales(request):
    animales = Animal.objects.all()  # Obtén todos los animales de la base de datos
    return render(request, 'Adopcion/consulta_animales.html', {'animales': animales})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def consulta_animales(request):
    animales = Animal.objects.all()
    return render(request, 'Adopcion/consulta_animales.html', {'animales': animales})


from django.shortcuts import render, redirect
from .forms import AdoptanteForm

def registrar_adoptante(request):
    if request.method == 'POST':
        form = AdoptanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_adoptantes')  # Redirige a la vista de consulta
    else:
        form = AdoptanteForm()
    return render(request, 'Adopcion/registrar_adoptante.html', {'form': form})

from .models import Adoptante

def consulta_adoptantes(request):
    adoptantes = Adoptante.objects.all()
    return render(request, 'Adopcion/consulta_adoptantes.html', {'adoptantes': adoptantes})

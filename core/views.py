from django.shortcuts import render, get_object_or_404, redirect
from .models import Plato
from .forms import PlatoForm  # Lo crearemos abajo

def home(request):
    platos = Plato.objects.all()
    return render(request, 'core/home.html', {'platos': platos})

def crear_plato(request):
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlatoForm()
    return render(request, 'core/crear_plato.html', {'form': form})

def editar_plato(request, plato_id):
    plato = get_object_or_404(Plato, pk=plato_id)
    if request.method == 'POST':
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlatoForm(instance=plato)
    return render(request, 'core/editar_plato.html', {'form': form, 'plato': plato})

def eliminar_plato(request, plato_id):
    plato = get_object_or_404(Plato, pk=plato_id)
    if request.method == 'POST':
        plato.delete()
        return redirect('home')
    return render(request, 'core/eliminar_plato.html', {'plato': plato})
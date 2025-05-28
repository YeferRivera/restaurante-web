from django.shortcuts import render, get_object_or_404, redirect
from .models import Plato
from .forms import PlatoForm  # Lo crearemos abajo
from .models import Orden
from .forms import OrdenForm
from .models import Pago
from .forms import PagoForm

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

def listar_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'core/listar_ordenes.html', {'ordenes': ordenes})

def crear_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.usuario = request.user  # Asigna el usuario que crea la orden
            orden.save()
            form.save_m2m()  # Guarda la relación muchos a muchos
            return redirect('listar_ordenes')
    else:
        form = OrdenForm()
    return render(request, 'core/crear_orden.html', {'form': form})

def detalle_orden(request, orden_id):
    orden = get_object_or_404(Orden, pk=orden_id)
    return render(request, 'core/detalle_orden.html', {'orden': orden})

def listar_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'core/listar_pagos.html', {'pagos': pagos})

def crear_pago(request):
    # Solo mostrar órdenes no pagadas
    from .models import Orden
    ordenes_no_pagadas = Orden.objects.filter(pagada=False)
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save()
            # Marca la orden como pagada
            pago.orden.pagada = True
            pago.orden.save()
            return redirect('listar_pagos')
    else:
        form = PagoForm()
        form.fields['orden'].queryset = ordenes_no_pagadas
    return render(request, 'core/crear_pago.html', {'form': form})

def detalle_pago(request, pago_id):
    pago = get_object_or_404(Pago, pk=pago_id)
    return render(request, 'core/detalle_pago.html', {'pago': pago})
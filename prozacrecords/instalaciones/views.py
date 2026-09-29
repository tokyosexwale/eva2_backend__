from django.shortcuts import render, redirect, get_object_or_404
from .models import InstalacionArtistica
from .forms import InstalacionForm

def lista_instalaciones(request):
    query = request.GET.get('q', '')
    if query:
        instalaciones = InstalacionArtistica.objects.filter(
            titulo__icontains=query
        ) | InstalacionArtistica.objects.filter(
            artistas__nombre__icontains=query
        ) | InstalacionArtistica.objects.filter(
            lugar_galeria__icontains=query
        )
    else:
        instalaciones = InstalacionArtistica.objects.all()
        
    return render(request, 'instalaciones/lista_instalaciones.html', {
        'instalaciones': instalaciones,
        'query': query
    })

def crear_instalacion(request):
    if request.method == 'POST':
        form = InstalacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_instalaciones')
    else:
        form = InstalacionForm()
    return render(request, 'instalaciones/form_instalacion.html', {
        'form': form,
        'titulo_pagina': 'Agregar Instalación Artística'
    })

def editar_instalacion(request, pk):
    instalacion = get_object_or_404(InstalacionArtistica, pk=pk)
    if request.method == 'POST':
        form = InstalacionForm(request.POST, instance=instalacion)
        if form.is_valid():
            form.save()
            return redirect('lista_instalaciones')
    else:
        form = InstalacionForm(instance=instalacion)
    return render(request, 'instalaciones/form_instalacion.html', {
        'form': form,
        'titulo_pagina': 'Modificar Instalación Artística'
    })

def eliminar_instalacion(request, pk):
    instalacion = get_object_or_404(InstalacionArtistica, pk=pk)
    if request.method == 'POST':
        instalacion.delete()
        return redirect('lista_instalaciones')
    return render(request, 'instalaciones/confirmar_eliminar_instalacion.html', {
        'instalacion': instalacion
    })
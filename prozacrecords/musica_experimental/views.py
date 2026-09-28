from django.shortcuts import render, redirect, get_object_or_404
from .models import AlbumExperimental
from .forms import AlbumForm

# READ / BUSCAR
def lista_albumes(request):
    query = request.GET.get('q', '')
    if query:
        albumes = AlbumExperimental.objects.filter(titulo__icontains=query) | AlbumExperimental.objects.filter(artista__nombre__icontains=query)
    else:
        albumes = AlbumExperimental.objects.all()
    return render(request, 'musica_experimental/lista_albumes.html', {'albumes': albumes, 'query': query})

# CREATE (Agregar)
def crear_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_albumes')
    else:
        form = AlbumForm()
    return render(request, 'musica_experimental/form_album.html', {'form': form, 'titulo_pagina': 'Agregar Álbum'})

# UPDATE (Editar)
def editar_album(request, pk):
    album = get_object_or_404(AlbumExperimental, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('lista_albumes')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'musica_experimental/form_album.html', {'form': form, 'titulo_pagina': 'Modificar Álbum'})

# DELETE (Eliminar)
def eliminar_album(request, pk):
    album = get_object_or_404(AlbumExperimental, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('lista_albumes')
    return render(request, 'musica_experimental/confirmar_eliminar.html', {'album': album})

from django.shortcuts import render
from .models import AlbumExperimental

def lista_albumes(request):
    # Consulta usando Django ORM
    albumes = AlbumExperimental.objects.all()
    return render(request, 'musica_experimental/lista_albumes.html', {'albumes': albumes})
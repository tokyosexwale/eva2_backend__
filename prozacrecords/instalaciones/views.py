from django.shortcuts import render
from .models import InstalacionArtistica

def lista_instalaciones(request):
    # Consulta usando Django ORM
    instalaciones = InstalacionArtistica.objects.all()
    return render(request, 'instalaciones/lista_instalaciones.html', {'instalaciones': instalaciones})
from django.contrib import admin
from .models import ArtistaCompositor, AlbumExperimental

@admin.register(ArtistaCompositor)
class ArtistaCompositorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')

@admin.register(AlbumExperimental)
class AlbumExperimentalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'genero', 'anio', 'formato')
    list_filter = ('genero', 'formato', 'anio')
    search_fields = ('titulo', 'artista__nombre', 'genero')
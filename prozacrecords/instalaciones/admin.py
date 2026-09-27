from django.contrib import admin
from .models import ArtistaVanguardia, InstalacionArtistica

@admin.register(ArtistaVanguardia)
class ArtistaVanguardiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'movimiento', 'pais')
    list_display_links = ('nombre',) # Al hacer clic en el nombre se abre el editor
    search_fields = ('nombre', 'movimiento', 'pais')
    list_filter = ('movimiento', 'pais')

@admin.register(InstalacionArtistica)
class InstalacionArtisticaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'artistas', 'anio_exposicion', 'lugar_galeria')
    list_display_links = ('titulo',) # Al hacer clic en el título se abre el editor
    search_fields = ('titulo', 'artistas__nombre', 'lugar_galeria')
    list_filter = ('anio_exposicion', 'artistas__movimiento')
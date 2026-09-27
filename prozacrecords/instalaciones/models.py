from django.db import models

class ArtistaVanguardia(models.Model):
    nombre = models.CharField(max_length=150)
    movimiento = models.CharField(max_length=100, help_text="Ej: Arte Sonoro, Fluxus, BioArte, Futurismo")
    pais = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Artista de Vanguardia"
        verbose_name_plural = "Artistas de Vanguardia"

    def __str__(self):
        return f"{self.nombre} ({self.movimiento})"


class InstalacionArtistica(models.Model):
    titulo = models.CharField(max_length=200)
    anio_exposicion = models.IntegerField(verbose_name="Año de Exposición")
    lugar_galeria = models.CharField(max_length=200, help_text="Galería, Museo o Espacio público")
    descripcion = models.TextField()
    artistas = models.ForeignKey(ArtistaVanguardia, on_delete=models.CASCADE, related_name='instalaciones')

    class Meta:
        verbose_name = "Instalación Artística"
        verbose_name_plural = "Instalaciones Artísticas"

    def __str__(self):
        return f"{self.titulo} - {self.lugar_galeria} ({self.anio_exposicion})"
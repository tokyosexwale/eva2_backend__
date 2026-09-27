from django.db import models

class ArtistaCompositor(models.Model):
    nombre = models.CharField(max_length=150)
    pais = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Artista / Compositor"
        verbose_name_plural = "Artistas y Compositores"

    def __str__(self):
        return f"{self.nombre} ({self.pais})"


class AlbumExperimental(models.Model):
    FORMATO_CHOICES = [
        ('VINYL', 'Vinilo'),
        ('CASSETTE', 'Casete'),
        ('CD', 'CD'),
        ('DIGITAL', 'Digital / Bandcamp'),
        ('CINTA_MAGN', 'Cinta Magnética / Reel-to-Reel'),
    ]

    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    anio = models.IntegerField(verbose_name="Año de Lanzamiento")
    formato = models.CharField(max_length=20, choices=FORMATO_CHOICES, default='DIGITAL')
    portada = models.URLField(max_length=500, default="https://picsum.photos/300/300")
    artista = models.ForeignKey(ArtistaCompositor, on_delete=models.CASCADE, related_name='albumes')

    class Meta:
        verbose_name = "Álbum Experimental"
        verbose_name_plural = "Álbumes Experimentales"

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre} ({self.anio})"
from django import forms
from .models import AlbumExperimental

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumExperimental
        fields = ['titulo', 'artista', 'genero', 'anio', 'formato', 'portada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'artista': forms.Select(attrs={'class': 'form-select'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'formato': forms.Select(attrs={'class': 'form-select'}),
            'portada': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }

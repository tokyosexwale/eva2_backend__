from django import forms
from .models import InstalacionArtistica

class InstalacionForm(forms.ModelForm):
    class Meta:
        model = InstalacionArtistica
        fields = ['titulo', 'artistas', 'anio_exposicion', 'lugar_galeria', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'artistas': forms.Select(attrs={'class': 'form-select'}),
            'anio_exposicion': forms.NumberInput(attrs={'class': 'form-control'}),
            'lugar_galeria': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
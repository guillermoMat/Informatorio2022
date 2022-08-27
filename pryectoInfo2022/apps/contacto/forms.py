
from .models import Comentarios
from django import forms

class FormContacto(forms.ModelForm):
    nombre = forms.CharField(label="Nombre",max_length=100)
    comentario = forms.CharField(label='Comentario',widget=forms.Textarea)
    
    class Meta:#Le decimos que modelo utilizar para crear formulario
        model = Comentarios
        fields = ('nombre', 'telefono','domicilio','comentario')
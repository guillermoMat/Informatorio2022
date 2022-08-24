

from django import forms
from .models import Post, Categoria


class PostForm(forms.ModelForm):
    
    class Meta:#Le decimos que modelo utilizar para crear formulario
        model = Post
        fields = ('titulo', 'contenido','imagen','categoria','usuario')
        widgets = {
            'usuario': forms.HiddenInput(),
        }
        
class FormCategoria(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = '__all__'
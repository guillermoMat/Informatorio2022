from django import forms

from .models import Post 

class PostForm(forms.ModelForm):
    
    class Meta:#Le decimos que modelo utilizar para crear formulario
        model = Post 
        fields = ('titulo', 'contenido','imagen','categoria',)
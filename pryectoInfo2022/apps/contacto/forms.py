from tkinter.tix import Form

from django import forms

class FormContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    contenido = forms.CharField(label='Contenido',widget=forms.Textarea)
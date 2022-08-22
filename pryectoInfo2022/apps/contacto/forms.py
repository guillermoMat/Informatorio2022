from tkinter.tix import Form

from django import forms

class FormContacto(forms.Form):
    asunto = forms.CharField(label='asunto', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    mensaje = forms.CharField(label='mensaje',widget=forms.Textarea)
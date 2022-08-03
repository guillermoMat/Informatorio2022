from datetime import time
from email.headerregistry import ContentDispositionHeader
from tkinter import Image, image_names
from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=30, blank=True, null=True),
    descripcion = models.CharField(max_length=50, blank=True, null=True),
    Contenido = models.CharField(max_length=400, blank=True, null=True),
    # imagen = 
    # fech_creacion = models.TimeField(_("fecha creacion"), auto_now=False, auto_now_add=False),
    
    # estado
    # categoria_id
    # usuario_id:
from datetime import time
from email.headerregistry import ContentDispositionHeader
from tkinter import Image, image_names
from django.db import models
from django.db.models import Model

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=30, blank=True, null=False)
    descripcion = models.CharField(max_length=50, blank=True, null=False)
    contenido = models.CharField(max_length=400, blank=True, null=False)
    # imagen =
    # fech_creacion = models.TimeField(_("fecha creacion"), auto_now=False, auto_now_add=False),
    
    # estado
    # categoria_id
    # usuario_id:
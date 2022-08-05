from datetime import time
from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=15, blank=False,null=True)


class Post(models.Model):
    titulo = models.CharField(max_length=30, blank=False, null=True)
    descripcion = models.CharField(max_length=50, blank=False, null=True)
    contenido = models.CharField(max_length=400, blank=False, null=True)
    # imagen =
    fecha_creacion = models.TimeField(auto_now=False, auto_now_add=False),
    estado = models.CharField
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)
    


from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=15, blank=False,null=True)
    
    def __str__(self):
        return self.categoria


class Post(models.Model):
    titulo = models.CharField(max_length=200, blank=False, null=True)
    descripcion = models.CharField(max_length=200, blank=False, null=True)
    contenido = models.TextField(null=True)
    imagen = models.ImageField(upload_to='post/',null=True,blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    activo = models.BooleanField(default=True)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True)
    usuario_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)

    
    def __str__(self):
        return self.titulo
    

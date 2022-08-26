from django.db import models

# Create your models here.

class Comentarios(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=True)
    comentario = models.TextField(null=True)
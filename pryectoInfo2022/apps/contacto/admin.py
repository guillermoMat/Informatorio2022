from django.contrib import admin

# Register your models here.
from apps.contacto.models import Comentarios

class AdminComentarios(admin.ModelAdmin):
    list_display =   ('id','nombre','comentario',)

admin.site.register(Comentarios,AdminComentarios)
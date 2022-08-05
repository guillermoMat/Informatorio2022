from django.contrib import admin
from apps.usuarios.models import Usuario
# Register your models here.
from apps.post.models import Categoria, Post

class AdminPost(admin.ModelAdmin):
    list_display =   ('id','titulo','descripcion','contenido','fecha_creacion',
                      'estado')
    

class AdminCategoria(admin.ModelAdmin):
    list_display =   ('id','categoria')


admin.site.register(Post,AdminPost)
admin.site.register(Categoria,AdminCategoria)
from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Categoria, Post

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('id','titulo','descripcion','contenido',
                    'activo','fecha_creation','IMAGEN','usuario_id')
    
    readonly_fields  = ('fecha_creation','fecha_update')
    
    search_fields = ('titulo','descripcion')
    
    # list_filter = ('fecha_creation','usuario_id')
    def IMAGEN(self, obj):
        return format_html('<img src="{}" style="width: 100px; \ height: 100px" />',(obj.imagen.url))
    
    
    

class AdminCategoria(admin.ModelAdmin):
    list_display =   ('id','categoria')


# admin.site.register(Post,AdminPost)
admin.site.register(Categoria,AdminCategoria)
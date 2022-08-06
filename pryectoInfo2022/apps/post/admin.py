from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Categoria, Post

class AdminPost(admin.ModelAdmin):
    list_display =   ('id','titulo','descripcion','contenido',
                      'activo','fecha_creacion','IMAGEN')
    
    
    # def img (self):
    #     return format_html("img src = {} />", self. )
    def IMAGEN(self, obj):
        return format_html('<img src="{}" style="width: 60px; \ height: 60px" />',(obj.imagen.url))
    
    # foto.short_description = 'foto' style="width: 30px; \ height: 30px"
    

class AdminCategoria(admin.ModelAdmin):
    list_display =   ('id','categoria')


admin.site.register(Post,AdminPost)
admin.site.register(Categoria,AdminCategoria)
from django.contrib import admin

# Register your models here.
from apps.post.models import Categoria, Post

class AdminPost(admin.ModelAdmin):
    list_display =   ('titulo','descripcion','contenido')

admin.site.register(Post,AdminPost)
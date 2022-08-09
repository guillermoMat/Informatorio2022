from django.urls import path

from . import views

urlpatterns = [
    path('',views.post,name="post"),
    path('categorias/<int:categoria>',views.categorias,name="categoria"),
  
]

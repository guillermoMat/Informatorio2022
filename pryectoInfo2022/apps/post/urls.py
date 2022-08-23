from django.urls import path

from . import views

urlpatterns = [
    path('',views.post,name="post"),

    path('detalle/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('nuevo', views.post_new, name='post_new'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]

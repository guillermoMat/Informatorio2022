from django.shortcuts import render

from apps.post.models import Post

# Create your views here.
def inicio(request):
    
    post = Post.objects.all()
    # if post :
    context = {'blog':post}
    # else:
        # context = {'vacio':'No hay blogs disponibes'}
    # nombre = "Nestor Acevedo"
    # lista = ["Acevedo","Alegre","Alvarin","Alvarez","Busi","Echavarria","Mathieu","Salcedo","Sotelo"]
    return render(request,'inicio.html', context)
    
   

    
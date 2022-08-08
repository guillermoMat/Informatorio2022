from django.shortcuts import render

from apps.post.models import Post

# Create your views here.
def post(request):
    
    post = Post.objects.filter(activo=True)
    if post :
        context = {'blog':post}
    else:
        context = {'vacio':'No hay blogs disponibes'}
    # nombre = "Nestor Acevedo"
    # lista = ["Acevedo","Alegre","Alvarin","Alvarez","Busi","Echavarria","Mathieu","Salcedo","Sotelo"]
    return render(request,'post.html', context)
    
   

    
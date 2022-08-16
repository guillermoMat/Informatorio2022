from django.shortcuts import render

from apps.post.models import Post,Categoria

# Create your views here.
def post(request):
    
    post = Post.objects.filter(activo=True)
    cat = {}
    if post :
        for x in post:
         
                cat[x.categoria] = x.categoria_id
        
        context = {'blog':post, 'cat':cat}
    else:
        context = {'vacio':'No hay blogs disponibes'}

    return render(request,'post.html', context)
    
def categorias(request,categoria):
    cat = Categoria.objects.get(id=categoria)
    post = Post.objects.filter(activo=True,categoria_id=categoria)
    context = {'blog':post,'categ':cat.categoria}
    return render(request,'post_categorias.html', context)

    
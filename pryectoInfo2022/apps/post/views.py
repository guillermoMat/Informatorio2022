from django.shortcuts import render

from apps.post.models import Post,Categoria

# Create your views here.
def post(request):
    parametro_categoria = request.GET.get("categoria")
    parametro_categorias = request.GET.get("categorias")
    
    if not parametro_categoria:
        
        post = Post.objects.filter(activo=True)
        cat = {}
        if post :
            for x in post:
                cat[x.categoria] = x.categoria_id
            
            context = {'blog':post, 'cat':cat}
        else:
            context = {'vacio':'No hay blogs disponibes'}
            
    else:
        cat = Categoria.objects.get(id=parametro_categoria)
        post = Post.objects.filter(activo=True,categoria_id=parametro_categoria)
        context = {'blog':post,'categ':cat.categoria,'cat':parametro_categorias}

    return render(request,'post_blog.html', context)
    


    
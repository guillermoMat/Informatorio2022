from django.shortcuts import render

from apps.post.models import Post,Categoria

# Create your views here.
def post(request):
    
    parametro_categoria = request.GET.get("categoria")
    
    post = Post.objects.filter(activo=True)
    cat = {}
    if post :
        for x in post:
            cat[x.categoria_id] = x.categoria
        if not parametro_categoria:
            context = {'blog':post, 'cat':cat}
        else:
            cate = Categoria.objects.get(id=parametro_categoria)
            post = Post.objects.filter(activo=True,categoria_id=parametro_categoria)
            context = {'blog':post,'categ':cate.categoria,'cat':cat}
    
    else:
        context = {'vacio':'No hay blogs disponibes'}
        
    return render(request,'post_blog.html', context)
    


    
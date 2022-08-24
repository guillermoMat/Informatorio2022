from django.shortcuts import render, get_object_or_404, redirect
from apps.post.models import Post,Categoria
from .forms import PostForm


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
    

def post_detail(request, pk):

    post = get_object_or_404(Post, id=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    post = {'form':PostForm()}
    if request.method == 'POST':
        formulario = PostForm(request.POST,request.FILES)
        # formulario = PostForm(data = request.POST)
        # form = PostForm(request.POST) 
        if formulario.is_valid():
            # post = form.save(commit=False)
            # post.usuario = request.user
            # post.save()
            # return redirect('post_detail', pk=post.pk)
            formulario.save()
            post['mensaje']='Post guardado'
        else:
            post['form']=formulario
    # else:
    #     form = PostForm()
    #  return render(request, 'post_edit.html', {'form' : post})
    return render(request, 'post_edit.html',post)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    
    return redirect('post_blog.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.post.models import Post,Categoria
from .forms import PostForm, FormCategoria


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
        context = {'vacio':'No hay posts disponibes'}
        
    return render(request,'post_blog.html', context)
    
@login_required
def post_detail(request, pk):

    post = get_object_or_404(Post, id=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_new(request):
    post = {'form':PostForm(initial={'usuario':request.user})}
    if request.method == 'POST':
        formulario = PostForm(request.POST,request.FILES)
      
        # formulario = PostForm(data = request.POST)
        # form = PostForm(request.POST) 
        if formulario.is_valid():
            # post = form.save(commit=False)
            # form.usuario = request.user
           
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

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('post')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

@login_required
def post_delete(request, pk):
   
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post')
   
  

@login_required
def admincategorias(request):
    data = {'form': FormCategoria()}
   
    if request.method=="GET":
        
        if  request.GET :
            id_cat=request.GET.get('lista')
            cat = Categoria.objects.get(id=id_cat)
            cat.delete()
            data['mensaje']='CATEGORIA ELIMINADA CON EXITO' 
       
    c = obtieneCategorias()
 
    if request.method == 'POST':
        formulario = FormCategoria(data=request.POST)
        if formulario.is_valid():
            valido = True
            for k,v in c.items(): 
                if request.POST['categoria'].upper() == v.upper():        
                    valido = False
            if valido:
                formulario.save()
                data['mensaje']='CATEGORIA GUARDADA'
                c = obtieneCategorias()      
            else:
                data['mensaje']='CATEGORIA EXISTENTE'
        else:
            data['form']= formulario
            data['mensaje']=""
    data['cat']=  c    
    return render(request,'adminCategoria.html',data)
        
    
def obtieneCategorias():
    categoria = Categoria.objects.all().order_by('categoria')
    categ = {}
    for x in categoria:
            categ[x.id] = x.categoria
    return categ

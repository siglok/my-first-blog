from django.shortcuts import render,redirect
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404 #para cuando no encuentra la pagina
from .forms import PostForm


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts}) #si no existe la plantila l


# LAS VIEWS SE ENCARGAN DE CONECTAR MODELOS (MODELS.PY) CON PLANTILLAS(POST_LIST)


# lo que queremos hacer: tomar algún contenido (modelos guardados en la base de datos) y mostrarlo adecuadamente en nuestra plantilla
# Agregamos el model creado en models.py desde arriba en los from


#--------------- QuerySet (conjunto de consultas)--------------------

#obtener lista de entradas e blog que hansido publicadas , ordenadas por fecha de publicacion
# agregar éste código al def post_list:
# Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) #construir el postform con los datos del formulario
        if form.is_valid(): #si el formulario se llenó correcatamente
            post = form.save(commit=False) #salva pero aun no envies, falta agregar autor
            post.author = request.user  #agregamos autor
            post.published_date = timezone.now() #agregamos la hora en que se está publicando
            post.save() #ahora si guardamos
            return redirect('post_detail', pk=post.pk) #vuelvenos a mandar a la pagina del formulario
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
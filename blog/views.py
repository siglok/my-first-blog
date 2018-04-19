from django.shortcuts import render,redirect, get_object_or_404 
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


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


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) #construir el postform con los datos del formulario
        if form.is_valid(): #si el formulario se llenó correcatamente
            post = form.save(commit=False) #salva pero aun no envies, falta agregar autor
            post.author = request.user  #agregamos autor
            # post.published_date = timezone.now() #agregamos la hora en que se está publicando
            post.save() #ahora si guardamos
            return redirect('post_detail', pk=post.pk) #vuelvenos a mandar a la pagina del formulario
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user  #agregamos autor
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


#veiw para post en borradores
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


#veiw para boton de publicar dentro de borradores
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)



@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('http://siglok.pythonanywhere.com')



#para agregar un comentario
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

#para aprovar comentarios como administrador
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
from django.shortcuts import render
from .models import Post
from django.utils import timezone


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


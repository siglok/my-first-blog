from django.db import models
from django.utils import timezone #agregamos la zona de horario ya prepuesa en settings
# Create your models here.


# Post                 queremos esta plantilla para los post
# --------
# title
# text
# author
# created_date
# published_date



class Post(models.Model):#Los modelos siempre con mayuscula inicial
	
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now) #agregamos la hora en ese momento 
	published_date = models.DateTimeField(blank=True,null=True)


	#definimos un publish para publised date
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

	def __str__(self):  #con esto obtendremos un texto (string) con un título de Post
		return self.title


	
	#Para agregar, editar y borrar los posts que hemos modelado, utilizaremos el administrador de Django

	#CREAR MODELO PARA COMENTARIOS 

class Comment(models.Model):

    post = models.ForeignKey('blog.Post', related_name='comments')
    # La opción related_name en models.ForeignKey nos permite acceder acceso a los comentarios desde el modelo Post.
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


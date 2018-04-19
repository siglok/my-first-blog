#Apartado para crear formularios que puedan agregar o modificar un post realziado


from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

	class Meta:
		model=Post #le decimos django qué modelo debe utilizar para crear formulario
		fields=('title','text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
#ahora crear un enlace a al pagina , una direccion url, una vista y una plantilla
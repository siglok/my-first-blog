from django.contrib import admin
from .models import Post, Comment
 
# from .models import Comment
# Register your models here.

admin.site.register(Post) # importamos (incluimos) el modelo Post definido en el capítulo anterior
admin.site.register(Comment)

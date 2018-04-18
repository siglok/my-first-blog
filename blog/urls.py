from django.conf.urls import include, url
from . import views #todas nuestras views del blog

urlpatterns=[
	url(r'^$',views.post_list), 
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	#Esta expresión regular coincidirá con ^ (un inicio) 
	#seguido de $ (un final) - por lo tanto, sólo una cadena vacía coincidirá
]

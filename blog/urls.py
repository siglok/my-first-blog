from django.conf.urls import include, url
from . import views #todas nuestras views del blog

urlpatterns=[
	url(r'^$',views.post_list), 
	#Esta expresión regular coincidirá con ^ (un inicio) 
	#seguido de $ (un final) - por lo tanto, sólo una cadena vacía coincidirá
]

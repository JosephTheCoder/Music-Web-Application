from django.conf.urls import url
from . import views  #the . tells it to look on the directory we're in

urlpatterns = [
    url(r'^$', views.index, name='index'),  #if the user only requests music/ then index is loaded
]

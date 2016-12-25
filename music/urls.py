from django.conf.urls import url
from . import views  #the . tells it to look on the directory we're in

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),  #if the user only requests music/ then index is loaded

    # /music/712/    712 is the id of the album
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]

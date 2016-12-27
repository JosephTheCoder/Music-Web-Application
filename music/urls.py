from django.conf.urls import url
from . import views  #the . tells it to look on the directory we're in

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),  #if the user only requests music/ then index is loaded

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/<album_id>/favorite/    Link used to perform logic in order to favorite a song, then it redirects to the previous page
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]

from django.conf.urls import url
from . import views  #the . tells it to look on the directory we're in

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),  #if the user only requests music/ then index is loaded

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),


]

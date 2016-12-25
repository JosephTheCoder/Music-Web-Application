from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums = Album.objects.all()  #go get all the albums from the database
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)

def detail(request, album_id):   #is always request inside the parenthesis
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

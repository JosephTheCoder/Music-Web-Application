from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()  #go get all the albums from the database
    return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):   #is always request inside the parenthesis
    album = get_object_or_404(Album, pk=album_id)   #Instead of using a try-except to handle the 404Responde Django got this function
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song']) #get the value of the song they selected
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True #changes the atributte
        selected_song.save() #saves changes to the database
        return render(request, 'music/detail.html', {'album': album})
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Album(models.Model):  #normal python class
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)   #1000 cause its gonna be the album cover, an url that is probably big

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) #whenever we delete an album, the songs are also deleted
    file_type = models.CharField(max_length=10)  #for each song type
    song_title = models.CharField(max_length=250)

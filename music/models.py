from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Album(models.Model):  #normal python class
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) #whenever we delete an album, the songs are also deleted
    file_type = models.CharField(max_length=10)  #for each song type
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
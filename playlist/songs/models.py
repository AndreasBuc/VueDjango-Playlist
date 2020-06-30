from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=256, unique=True)
    artist = models.CharField(max_length=256, blank=True, null=True)

    duration = models.PositiveIntegerField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=256)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

from django.db import models
from django.conf import settings


class Song(models.Model):
    title = models.CharField(max_length=256,)
    artist = models.CharField(max_length=256, blank=True, null=True)

    duration = models.PositiveIntegerField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='songs')

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=256)
    songs = models.ManyToManyField(to=Song, related_name='playlists',
                                   blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='playlists')

    def __str__(self):
        return self.name

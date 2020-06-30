from rest_framework import viewsets
from songs.api.serializers import SongSerializer, PlaylistSerializer
from songs.models import Song, Playlist


class SongsViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by("-id")
    serializer_class = SongSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all().order_by("name")
    serializer_class = PlaylistSerializer

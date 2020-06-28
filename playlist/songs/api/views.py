from rest_framework import viewsets
from songs.api.serializers import SongSerializer
from songs.models import Song


class SongsViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by("-id")
    serializer_class = SongSerializer

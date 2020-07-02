from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from songs.api.serializers import (
    SongSerializer, PlaylistSerializer, PlaylistWOSongDetailsSerializer,
    SongIDSerializer)
from songs.models import Song, Playlist
from rest_framework.permissions import IsAuthenticated


class SongsViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Song.objects.all().filter(creator_id=self.request.user.id).order_by("-id")
        # return self.request.user.accounts.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class SongsIDViewSet(viewsets.ModelViewSet):
    serializer_class = SongIDSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Song.objects.all().filter(creator_id=self.request.user.id).order_by("-id")


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all().order_by("name")
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlaylistWOSongDetailsViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all().order_by("name")
    serializer_class = PlaylistWOSongDetailsSerializer
    permission_classes = [IsAuthenticated]


class PlaylistAddRemoveAPIView(APIView):
    queryset = Playlist.objects.all().order_by("-id")
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, p_pk, s_pk):
        """Remove request.user from the voters queryset of an answer instance."""
        playlist = get_object_or_404(Playlist, pk=p_pk)
        song = get_object_or_404(Song, pk=s_pk)
        playlist.songs.remove(song)
        playlist.save()
        print(f'Delete method: request: {request.data}')
        serializer_context = {"request": request}
        serializer = self.serializer_class(playlist, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, p_pk, s_pk):
        """Add request.user to the voters queryset of an answer instance."""
        playlist = get_object_or_404(Playlist, pk=p_pk)
        song = get_object_or_404(Song, pk=s_pk)
        playlist.songs.add(song)
        print(f'Post method: request: {request.data}')
        playlist.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(playlist, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework import serializers
from songs.models import Song, Playlist


class PlaylistWOSongDetailsSerializer(serializers.ModelSerializer):

    owner_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Playlist
        exclude = ['songs', 'owner_id']


class SongSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)
    creator_id = serializers.PrimaryKeyRelatedField(read_only=True)

    playlists = serializers.SerializerMethodField()
    playlists_ids = serializers.SerializerMethodField()
    is_in_playlist = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = '__all__'

    def get_playlists_ids(self, instance):
        return [playlist.id for playlist in list(instance.playlists.all())]

    def get_playlists(self, instance):
        playserializer = PlaylistWOSongDetailsSerializer(instance.playlists, many=True)
        return playserializer.data

    def get_is_in_playlist(self, instance):
        return instance.playlists.all().exists()


class SongIDSerializer(serializers.ModelSerializer):

    creator_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'creator_id']


class PlaylistSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True)

    songs = SongIDSerializer(many=True)
    is_empty = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = '__all__'
        # the depth is just good for GET method
        # depth = 1

    def get_is_empty(self, instance):
        return not instance.songs.all().exists()

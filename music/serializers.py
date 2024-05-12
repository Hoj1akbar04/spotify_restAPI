from rest_framework import serializers
from .models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ("name", "image")


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ("title", "cover_image", "watching")


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ("title", "cover_image", "listened")

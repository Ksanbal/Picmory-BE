from rest_framework import serializers

from apps.album.models import Album, AlbumMemory


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ['id', 'name']


class AlbumMemorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumMemory
        fields = ['memory']

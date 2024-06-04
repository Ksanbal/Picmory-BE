from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.album.models import Album, AlbumMemory
from apps.album.serializers import AlbumMemorySerializer, AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('-updated_at')
    serializer_class = AlbumSerializer
    pagination_class = None

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    @action(
        detail=True,
        methods=['post'],
        url_path='memory',
        url_name='add_memory',
    )
    def add_memory(self, request, pk=None):
        album = self.get_object()
        serializer = AlbumMemorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(album=album)
        album.save()

        return Response(status=status.HTTP_201_CREATED)

    @action(
        detail=True,
        methods=['delete'],
        url_path='memory/(?P<memory_id>[^/.]+)',
        url_name='delete_memory',
    )
    def delete_memory(self, request, pk=None, memory_id=None):
        album = self.get_object()
        album_memory = get_object_or_404(
            AlbumMemory,
            id=memory_id,
            album=album,
        )
        album_memory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

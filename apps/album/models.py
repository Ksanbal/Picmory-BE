from tabnanny import verbose
from django.db import models


class Album(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'apps_album'
        verbose_name_plural = '앨범'


class AlbumMemory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(
        'album.Album',
        on_delete=models.CASCADE,
        related_name='memories',
    )
    memory = models.ForeignKey(
        'memory.Memory',
        on_delete=models.CASCADE,
        related_name='albums',
    )

    class Meta:
        db_table = 'apps_album_memory'

from django.contrib import admin
from django.utils.safestring import mark_safe
from unfold.admin import ModelAdmin, TabularInline

from apps.album.models import Album, AlbumMemory


class AlbumMemoryInline(TabularInline):
    model = AlbumMemory
    extra = 0


@admin.register(Album)
class AlbumAdmin(ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('user__email', )

    inlines = [
        AlbumMemoryInline,
    ]

from django.contrib import admin
from django.utils.safestring import mark_safe
from unfold.admin import ModelAdmin, TabularInline

from apps.memory.models import Memory
from apps.upload.models import Upload


class UploadInline(TabularInline):
    model = Upload
    extra = 0
    can_delete = False
    fields = ('file_type', 'display_file')

    readonly_fields = ('file_type', 'display_file')

    def display_file(self, obj):
        return mark_safe(
            f'<img src="{obj.file.url}" alt="{obj.file.name}" style="width:200px">'
        )

    display_file.short_description = "미리보기"


@admin.register(Memory)
class MemoryAdmin(ModelAdmin):
    list_display = ('brand', 'user', 'created_at')
    list_filter = ('brand', 'created_at')

    search_fields = ('user__email', )

    inlines = [
        UploadInline,
    ]

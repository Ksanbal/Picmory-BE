from django.contrib import admin
from django.utils.safestring import mark_safe
from unfold.admin import ModelAdmin

from apps.upload.models import Upload


@admin.register(Upload)
class UploadAdmin(ModelAdmin):
    list_display = ('user', 'memory', 'file_type', 'created_at')
    readonly_fields = ('display_file', )

    def display_file(self, obj):
        return mark_safe(
            f'<img src="{obj.file.url}" alt="{obj.file.name}" style="width:200px">'
        )

    display_file.short_description = "미리보기"

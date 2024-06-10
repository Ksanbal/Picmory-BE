import uuid
from django.db import models

from apps import memory


def upload_to(instance, filename):
    return 'uploads/{0}/{1}/{2}'.format(
        instance.user.id,
        uuid.uuid4(),
        filename,
    )


# 업로드된 파일
class Upload(models.Model):
    FILE_TYPES = (
        ('PHOTO', 'PHOTO'),
        ('VIDEO', 'VIDEO'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
    )
    memory = models.ForeignKey(
        memory.models.Memory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='uploads',
    )
    file_type = models.CharField(
        max_length=10,
        choices=FILE_TYPES,
    )
    file = models.FileField(max_length=255, upload_to=upload_to)

    class Meta:
        db_table = 'apps_upload'
        verbose_name_plural = '업로드'

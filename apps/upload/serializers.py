from apps.upload.models import Upload
from rest_framework import serializers


class UploadCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload
        fields = (
            'file_type',
            'file',
        )

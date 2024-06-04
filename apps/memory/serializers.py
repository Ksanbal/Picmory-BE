import os
from rest_framework import serializers

from apps.memory.models import Memory
from apps.upload.models import Upload


class MemoryCreateSerialzier(serializers.ModelSerializer):
    uploads = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Upload.objects.filter(memory=None),
    )

    class Meta:
        model = Memory
        fields = ('date', 'brand', 'uploads')

    def create(self, validated_data):
        uploads = validated_data.pop('uploads')
        memory = Memory.objects.create(**validated_data)
        for upload in uploads:
            upload.memory = memory
            upload.save()
        return memory


class MemorySerializer(serializers.ModelSerializer):

    class UploadSerializer(serializers.ModelSerializer):

        file = serializers.SerializerMethodField()

        class Meta:
            model = Upload
            fields = ('file', 'file_type')

        def get_file(self, obj):
            return os.environ.get('HOST') + obj.file.url

    uploads = serializers.SerializerMethodField()

    class Meta:
        model = Memory
        fields = ('id', 'date', 'brand', 'uploads')

    def get_uploads(self, obj):
        uploads = obj.uploads.order_by('file_type')
        return self.UploadSerializer(
            uploads,
            many=True,
            read_only=True,
        ).data

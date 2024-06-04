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

from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.upload import serializers


class UploadViewSet(viewsets.ViewSet):
    # 파일 업로드
    def create(self, request):
        serializer = serializers.UploadCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_upload = serializer.save(user=request.user)

        return Response(
            {
                'id': new_upload.id,
            },
            status=status.HTTP_201_CREATED,
        )

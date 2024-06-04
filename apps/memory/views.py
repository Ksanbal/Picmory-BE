from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.memory import serializers


class MemoryViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = serializers.MemoryCreateSerialzier(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(status=status.HTTP_201_CREATED)

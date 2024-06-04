from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.memory import serializers
from apps.memory.models import Memory


class MemoryViewSet(viewsets.ModelViewSet):
    queryset = Memory.objects.all().order_by('-date')
    serializer_class = serializers.MemorySerializer

    def get_queryset(self):
        return Memory.objects.filter(user=self.request.user).order_by('-date')

    def create(self, request):
        serializer = serializers.MemoryCreateSerialzier(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(status=status.HTTP_201_CREATED)

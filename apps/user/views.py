from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.user import serializers


class UserViewSet(viewsets.ViewSet):
    # 회원가입
    def create(self, request):
        serializer = serializers.SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

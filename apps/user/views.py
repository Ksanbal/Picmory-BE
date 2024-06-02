from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.user import serializers
from apps.user.models import User


class UserViewSet(viewsets.ViewSet):

    # 회원가입
    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def signup(self, request):
        serializer = serializers.SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    # 로그인
    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def signin(self, request):
        serializer = serializers.SigninSerialzier(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(
            User,
            provider=serializer.validated_data['provider'],
            provider_id=serializer.validated_data['provider_id'],
        )

        # 유저 정보 업데이트
        user.push_token = serializer.validated_data.get('push_token')
        user.save()

        # 토큰 발급
        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)

        return Response({
            'refresh_token': refresh_token,
            'access_token': access_token,
        })

    # 유저 정보 조회
    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data)

    # 로그아웃
    @action(methods=['DELETE'], detail=False)
    def signout(self, request):
        request.user.push_token = None
        request.user.save()

        return Response()

    # 회원탈퇴
    @action(methods=['DELETE'], detail=False)
    def leave(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

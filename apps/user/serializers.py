from rest_framework import serializers

from apps.user.models import User


# 회원가입
class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'provider',
            'provider_id',
            'email',
            'nickname',
            'meta_data',
        ]


# 로그인
class SigninSerialzier(serializers.Serializer):
    provider = serializers.CharField()
    provider_id = serializers.CharField()
    push_token = serializers.CharField(required=False)

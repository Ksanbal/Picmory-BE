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

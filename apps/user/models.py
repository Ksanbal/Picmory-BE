from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import time


class UserManager(BaseUserManager):

    def create_user(
        self,
        provider,
        provider_id,
        email,
        password=None,
        nickname=None,
    ):
        if not provider_id:
            raise ValueError('Provider ID is required')
        user = self.model(
            provider=provider,
            provider_id=provider_id,
            email=self.normalize_email(email),
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        nickname,
        password=None,
    ):
        user = self.create_user(
            provider='Django',  # 'DJANGO'로 고정
            provider_id=int(time.time()),
            email=email,
            password=password,
            nickname=nickname,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    provider = models.CharField(
        max_length=10,
        choices=[
            ('DJANGO', 'Django'),
            ('APPLE', 'Apple'),
            ('GOOGLE', 'Google'),
        ],
    )
    provider_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=30)
    meta_data = models.JSONField(default=dict, null=True)

    push_token = models.CharField(max_length=255, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

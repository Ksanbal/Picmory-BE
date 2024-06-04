"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from apps.memory.views import MemoryViewSet
from apps.upload.views import UploadViewSet
from apps.user.views import UserViewSet

api_router = DefaultRouter(trailing_slash=False)

api_router.register('users', UserViewSet, basename="user")
api_router.register('uploads', UploadViewSet, basename="upload")
api_router.register('memory', MemoryViewSet, basename="memory")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls)),
]

# JWT 토큰 관련 URL 설정
urlpatterns += [
    path(
        'api/token/refresh',
        TokenRefreshView.as_view(),
        name='token_refresh',
    ),
    path(
        'api/token/verify',
        TokenVerifyView.as_view(),
        name='token_verify',
    ),
]

# media 파일 서빙을 위한 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

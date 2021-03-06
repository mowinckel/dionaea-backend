"""dionaea_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from dionaea.views import TrapViewSet, MakerViewSet, PreyViewSet

router = DefaultRouter()
router.register('trap', TrapViewSet, 'trap')
router.register('prey', PreyViewSet, 'prey')
router.register('maker', MakerViewSet, 'maker')

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^api/v[1-9]/', include(router.urls)),

    re_path(r'^api/v[1-9]/jwt/', obtain_jwt_token),
    re_path(r'^api/v[1-9]/jwt/verify/', verify_jwt_token),
    re_path(r'^api/v[1-9]/jwt/refresh/', refresh_jwt_token)
]

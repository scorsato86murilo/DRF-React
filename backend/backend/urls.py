from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .view import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

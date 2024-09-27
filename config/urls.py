from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from main.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

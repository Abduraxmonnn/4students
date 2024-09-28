from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers

from config import settings

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

urlpatterns += tuple(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns += tuple(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

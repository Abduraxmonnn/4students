from django.shortcuts import render

from rest_framework import viewsets, permissions

from main.models import User
from main.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

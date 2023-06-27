from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets

# Create your views here.


class UserTaskViewSet(viewsets.ModelViewSet):
    queryset = models.TgUser.objects.all()
    serializer_class = serializers.TgUserSerializer

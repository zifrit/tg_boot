from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets

# Create your views here.


class TgUserViewSet(viewsets.ModelViewSet):
    queryset = models.TgUser.objects.all()
    serializer_class = serializers.TgUserSerializer
    filterset_fields = [
        'tg_id',
        'username',
    ]


class ListGameViewSet(viewsets.ModelViewSet):
    queryset = models.ListGames.objects.select_related('administrator')
    serializer_class = serializers.ListGamesSerializer
    filterset_fields = [
        'administrator',
        'game_name',
    ]


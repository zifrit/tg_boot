from rest_framework import serializers
from . import models


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TgUser
        fields = '__all__'


class ListGamesSerializer(serializers.ModelSerializer):
    administrator = serializers.CharField(source='administrator.username')
    class Meta:
        model = models.ListGames
        fields = ['game_name', 'administrator']


class GameCSPSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameCSP
        fields = '__all__'

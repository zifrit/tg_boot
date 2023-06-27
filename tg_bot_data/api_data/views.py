from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

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


class Test(APIView):
    def post(self, request):
        data = request.data
        user = models.TgUser.objects.get(tg_id=data['user'])
        game_in_list = models.ListGames.objects.create(administrator=user, game_name=data['game_name'])
        data_json = {
            'user_id': data['user'],
            'answer': data['answer']
        }
        create_game = models.GameCSP.objects.create(list_games=game_in_list, in_game=1, players=data_json)
        print(request.data)
        return Response({
            "status": True
        })

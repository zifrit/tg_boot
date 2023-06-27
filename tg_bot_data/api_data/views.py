from django.db import IntegrityError
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


class CreateGameRoom(APIView):
    def post(self, request):
        data = request.data
        user = models.TgUser.objects.get(tg_id=data['user'])
        try:
            game_in_list = models.ListGames.objects.create(administrator=user, game_name=data['game_name'])
            data_json = {
                'user_id': data['user'],
                'answer': data['answer']
            }
            create_game = models.GameCSP.objects.create(list_games=game_in_list, in_game=1, players=data_json)
            game_in_list.identify_game = create_game.id
            game_in_list.save()
            return Response({
                "status": True,
                'message': 'Игра успешно создана'
            })
        except IntegrityError:
            return Response({
                "status": False,
                'message': 'Такое имя игры уже существует'
            })


class JoinInRoom(APIView):
    def post(self, request):
        data = request.data
        user = models.TgUser.objects.get(tg_id=data['user'])
        room = models.GameCSP.objects.filter(list_games__game_name=data['room_name'])
        if room:
            if user.tg_id in room[0].players.values():
                return Response({
                    "status": True,
                    'message': 'Вы уже в комнате'
                })
            elif room[0].in_game >= 2:
                return Response({
                    "status": False,
                    'message': 'Количество участников превышено'
                })
            else:
                room[0].in_game += 1
                room[0].save()
                return Response({
                    "status": True,
                    'message': 'Вы присоединились к комнате'
                })
        else:
            return Response({
                "status": False,
                'message': 'Такой комнаты нету'
            })


class AnswerKMN(APIView):
    def post(self, request):
        data = request.data
        user = models.TgUser.objects.get(tg_id=data['user'])
        room = models.GameCSP.objects.filter(list_games__game_name=data['room_name'])
        if data['answer'] in ['к', 'н', 'б']:
            room[0].players[user.tg_id] = data['answer']
            room[0].save()
            return Response({
                "status": True,
                'message': 'Ваш ответ принят'
            })
        else:
            return Response({
                "status": False,
                'message': 'Неверный ответ'
            })

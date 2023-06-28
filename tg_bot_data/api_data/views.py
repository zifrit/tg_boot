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
                data['user']: data['answer']
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


class ActionInRoom(APIView):
    def get_data(self, request):
        data = request.data
        user = models.TgUser.objects.get(tg_id=data['user'])
        room = models.GameCSP.objects.filter(list_games__game_name=data['room_name'])
        return user, room


class JoinInRoom(ActionInRoom):
    def post(self, request):
        user, room = self.get_data(request)
        if room:
            if str(user.tg_id) in list(room[0].players.keys()):
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


class AnswerKMN(ActionInRoom):
    def post(self, request):
        data = request.data
        user, room = self.get_data(request)
        if data['answer'] in ['к', 'н', 'б']:
            room = models.GameCSP.objects.get(list_games__game_name=data['room_name'])
            a = room.players
            print(user.tg_id)
            print(type(user.tg_id))
            a[str(user.tg_id)] = data['answer']
            room.save()
            return Response({
                "status": True,
                'message': 'Ваш ответ принят'
            })
        else:
            return Response({
                "status": False,
                'message': 'Неверный ответ'
            })


class EndGameKMN(ActionInRoom):
    def post(self, request):
        user, room = self.get_data(request)
        if room:
            if user.tg_id == room[0].list_games.administrator.tg_id:
                answer_1 = room[0].players[list(room[0].players.keys())[0]]
                answer_2 = room[0].players[list(room[0].players.keys())[1]]
                print(answer_1)
                print(answer_2)
                if (answer_1 == 'к' and answer_2 == 'н') or (answer_1 == 'н' and answer_2 == 'б') or (
                        answer_1 == 'б' and answer_2 == 'к'):
                    return Response({
                        "status": True,
                        'message': [
                            [int(list(room[0].players.keys())[0]), 'Выиграл'],
                            [int(list(room[0].players.keys())[1]), 'Проиграл']
                        ],
                        'room_id': room[0].list_games.pk
                    })
                elif (answer_2 == 'к' and answer_1 == 'н') or (answer_2 == 'н' and answer_1 == 'б') or (
                        answer_2 == 'б' and answer_1 == 'к'):
                    return Response({
                        "status": True,
                        'message': [
                            [int(list(room[0].players.keys())[0]), 'Проиграл'],
                            [int(list(room[0].players.keys())[1]), 'Выиграл']
                        ],
                        'room_id': room[0].list_games.pk
                    })
                elif answer_1 == answer_2:
                    return Response({
                        "status": 'D',
                        'message': [
                            [int(list(room[0].players.keys())[0]), 'Ничья'],
                            [int(list(room[0].players.keys())[1]), 'Ничья']
                        ],
                        'room_id': room[0].list_games.pk
                    })
                else:
                    return Response({
                        "status": False,
                        'message': 'Ошибка'
                    })
            else:
                return Response({
                    "status": False,
                    'message': 'Вы не можете закончить игру'
                })

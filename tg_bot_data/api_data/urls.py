from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tg', views.TgUserViewSet)
router.register(r'list_games', views.ListGameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('start_kmn/', views.CreateGameRoom.as_view()),
    path('join_kmn/', views.JoinInRoom.as_view()),
    path('answer_kmn/', views.AnswerKMN.as_view()),
    path('end_game_kmn/', views.EndGameKMN.as_view())
]

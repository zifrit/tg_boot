from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tg', views.TgUserViewSet)
router.register(r'games', views.ListGameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('start/', views.CreateGameRoom.as_view()),
    path('search_join/', views.JoinInRoom.as_view()),
    path('end_game/', views.EndGameKMN.as_view())
]

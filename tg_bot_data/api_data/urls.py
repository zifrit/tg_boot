from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tg', views.TgUserViewSet)
router.register(r'list_games', views.ListGameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

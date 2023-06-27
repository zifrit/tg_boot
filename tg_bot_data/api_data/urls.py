from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tg', views.UserTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

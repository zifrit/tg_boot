from rest_framework import serializers
from . import models


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TgUser
        fields = '__all__'

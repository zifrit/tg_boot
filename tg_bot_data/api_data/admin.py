from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'tg_id']
    list_display = ['id', 'tg_id', 'username']
    list_editable = ['username']
    search_fields = ['tg_id', 'username']


@admin.register(models.ListGames)
class ListGamesAdmin(admin.ModelAdmin):
    list_display = ['id', 'administrator', 'game_name']
    list_display_links = ['id', 'administrator']
    search_fields = ['administrator__username', 'administrator__tg_id']

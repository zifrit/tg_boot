from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.TgUser)
class UserTaskAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'tg_id']
    list_display = ['id', 'tg_id', 'username']
    list_editable = ['username']
    search_fields = ['tg_id', 'username']

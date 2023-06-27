from django.db import models


# Create your models here.

class TgUser(models.Model):
    tg_id = models.IntegerField(verbose_name='id в тг', db_index=True)
    username = models.CharField(verbose_name='username в тг', max_length=255)

    class Meta:
        db_table = 'TG_user'

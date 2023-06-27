from django.db import models


# Create your models here.

class TgUser(models.Model):
    tg_id = models.IntegerField(verbose_name='id in telegram', db_index=True)
    username = models.CharField(verbose_name='username in telegram', max_length=255, db_index=True)

    def __str__(self):
        return str(self.tg_id)

    class Meta:
        db_table = 'TG_user'


class ListGames(models.Model):
    administrator = models.ForeignKey(to=TgUser, verbose_name='administrator', db_index=True, on_delete=models.CASCADE,
                                      related_name="my_games")
    game_name = models.CharField(verbose_name='game name', max_length=255)
    players = models.JSONField(verbose_name='players')

    def __str__(self):
        return f'создал {self.administrator.__str__()} игру {self.game_name}'

    class Meta:
        db_table = 'TG_list_games'

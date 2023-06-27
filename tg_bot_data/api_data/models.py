from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class TgUser(models.Model):
    tg_id = models.IntegerField(verbose_name='id in telegram', db_index=True, unique=True)
    username = models.CharField(verbose_name='username in telegram', max_length=255, db_index=True)

    def __str__(self):
        return str(self.tg_id)

    class Meta:
        db_table = 'TG_user'


class ListGames(models.Model):
    administrator = models.ForeignKey(to=TgUser, verbose_name='administrator', db_index=True, on_delete=models.CASCADE,
                                      related_name="my_games")
    game_name = models.CharField(verbose_name='game name', max_length=255, db_index=True, unique=True)
    identify_game = models.IntegerField(verbose_name='id game',
                                        validators=[
                                            MaxValueValidator(10000),
                                            MinValueValidator(0)
                                        ], default=0)

    def __str__(self):
        return f'создал {self.administrator.__str__()} игру {self.game_name}'

    class Meta:
        db_table = 'TG_list_games'


class GameCSP(models.Model):
    list_games = models.OneToOneField(to=ListGames, verbose_name='connection to list', on_delete=models.CASCADE,
                                      related_name='game')
    number_players = models.IntegerField(verbose_name='number of players', default=2,
                                         validators=[
                                             MaxValueValidator(2),
                                             MinValueValidator(0)
                                         ])
    in_game = models.IntegerField(verbose_name='players in game',
                                  validators=[
                                      MaxValueValidator(2),
                                      MinValueValidator(0)
                                  ])
    players = models.JSONField(verbose_name='players')

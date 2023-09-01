from django.db import models

# Create your models here.


class Reviews(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    game_rating = models.DecimalField(max_digits=2, decimal_places=1)
    game_user_rating = models.DecimalField(max_digits=2, decimal_places=1)
    date_of_publishing = models.DateField()


class Rankings(models.Model):
    title = models.CharField(max_length=100)
    date_of_publishing = models.DateField()


class PendingPremieres(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    release_date = models.DateField()
    will_play = models.IntegerField()
    date_of_publishing = models.DateField()
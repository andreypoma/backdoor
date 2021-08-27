from django.db import models
from django.core import validators
from login.models import User

class Game(models.Model):
    host_id = models.ForeignKey(User, related_name="hostedGames", on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    players = models.ManyToManyField(User, related_name="joinedGames")
    date = models.DateTimeField()
    address = models.TextField(max_length=300)
    type = models.TextField(max_length=300)
    buyIn = models.IntegerField()
    blinds = models.TextField()
    numberOfPlayers = models.IntegerField()
    desc = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
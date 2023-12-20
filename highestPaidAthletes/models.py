from django.db import models

# Create your models here.

class Athlete(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=20)
    currentRank = models.IntegerField()
    sport = models.CharField(max_length=50)
    year = models.IntegerField()
    earnings = models.FloatField()
    
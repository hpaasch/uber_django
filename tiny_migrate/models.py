from django.db import models

# Create your models here.


class OlympicSkier(models.Model):
    name = models.CharField(max_length=50)
    finish = models.IntegerField()
    country = models.CharField(max_length=50)
    time = models.FloatField()
    age = models.IntegerField()

    def __str__(self):
        return self.name


class OlympicCoach(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

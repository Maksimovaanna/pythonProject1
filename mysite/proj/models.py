from django.db import models
from django.urls import reverse
# Create your models here.

class car(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    moddel = models.CharField(max_length=50)
    voditel = models.CharField(max_length=50)
    nomer = models.CharField(max_length=50)
    online = models.CharField(max_length=50)

class order(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    nomer = models.CharField(max_length=50)
    voditel = models.CharField(max_length=50)
    passajir = models.CharField(max_length=50)
    naznach = models.CharField(max_length=50)
    sms = models.IntegerField(default=0)



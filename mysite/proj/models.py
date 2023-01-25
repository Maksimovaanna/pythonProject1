from django.db import models
from django.urls import reverse
# Create your models here.

class predmet(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    nazvanie = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    audit = models.CharField(max_length=50)

class uchet(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    login = models.CharField(max_length=50)
    passw = models.CharField(max_length=50)
    propusk = models.IntegerField(default=0)



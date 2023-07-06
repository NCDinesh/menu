from django.db import models


class Item(models.Model):
    itemname =models.CharField(max_length=100)
    itemtype =models.CharField(max_length=50)
    itemprice = models.IntegerField()
# Create your models here.

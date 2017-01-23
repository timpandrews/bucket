from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    category = models.TextField()
    location = models.TextField()
    container = models.TextField()
    description = models.TextField()
    unit = models.TextField()
    Qty = models.IntegerField()
    purchaseDate = models.DateTimeField()
    bestByDate = models.DateTimeField()
    checkOnFrequency = models.TextField()
    moreInfoLink = models.TextField()
    waterStored = models.IntegerField()
    numServings = models.IntegerField()
    calPerServing = models.IntegerField()
    prescriptionMed = models.BooleanField()


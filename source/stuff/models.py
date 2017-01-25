from __future__ import unicode_literals

from django.conf import settings
from django.db import models

class Container(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    sortOrder = models.FloatField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self): # python 2
        return str(self.title)

    def __str__(self): # python 3
        return str(self.title)



class Category(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    sortOrder = models.FloatField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self): # python 2
        return str(self.title)

    def __str__(self): # python 3
        return str(self.title)

    class Meta:
        verbose_name_plural = "Categories"

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    category = models.ForeignKey(Category)
    location = models.CharField(max_length=25)
    container = models.ForeignKey(Container, default=1)
    description = models.CharField(max_length=100)
    unit = models.CharField(max_length=25)
    qty = models.IntegerField()
    purchaseDate = models.DateTimeField(blank=True)
    bestByDate = models.DateTimeField(blank=True)
    checkOnFrequency = models.CharField(max_length=25, blank=True)
    moreInfoLink = models.CharField(max_length=100, blank=True)
    waterStored = models.FloatField(blank=True, null=True)
    numServings = models.IntegerField(blank=True, null=True)
    calPerServing = models.IntegerField(blank=True, null=True)
    prescriptionMed = models.BooleanField(blank=True)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self): # python 2
        return str(self.id)

    def __str__(self): # python 3
        return str(self.id)




from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Goods(models.Model):
	name = models.CharField(max_length=40)
	price = models.FloatField()
	desc = models.TextField()
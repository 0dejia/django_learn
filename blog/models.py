from __future__ import unicode_literals

from django.db import models

# Create your models here.
class article(models.Model):
	title = models.CharField(max_length=40)
	content_time = models.DateTimeField()
	content = models.TextField()
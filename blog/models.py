from __future__ import unicode_literals

from django.db import models

# Create your models here.
class article(models.Model):
	title = models.CharField(max_length=40)
	content_time = models.DateTimeField()
	content = models.TextField()

class category(models.Model):
	parent_node = models.IntegerField(default=0)
	name = models.CharField(max_length=40)

	def __str__(self):
		return self.name

class navigate(models.Model):
	nav_name = models.CharField(max_length=40)
	nav_href = models.CharField(max_length=40)

	def __str__(self):
		return self.nav_name
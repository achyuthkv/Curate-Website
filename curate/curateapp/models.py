from __future__ import unicode_literals
from django.conf import settings
from django.db import models
# Create your models here.
#MODEL VIEW CONTROLLER

class Source(models.Model):
	image = models.ImageField(upload_to='uploads/')
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return self.title

	

	class Meta:
		ordering = ["-timestamp","-updated"]


from django.db import models

# Create your models here.

class Webapp(models.Model):
	articalHeadline=models.TextField()
	articalBody=models.CharField(max_length=200)
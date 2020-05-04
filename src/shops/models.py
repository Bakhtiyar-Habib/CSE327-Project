from django.db import models

# Create your models here.
class Shops(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(default = "default.jpg", blank=True)
	url = models.CharField(max_length=120, null = True)
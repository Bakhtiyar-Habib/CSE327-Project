from django.db import models

# Create your models here.
class TraditionalMen(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(default = "default.jpg", blank=True)
	brand = models.CharField(max_length=120, blank = True)
	shop = models.CharField(max_length=120, blank = True)
	price = models.IntegerField(blank=True, default=0)
	url = models.CharField(max_length=120, blank = True)

class TraditionalWomen(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(default = "default.jpg", blank=True)
	brand = models.CharField(max_length=120, blank = True)
	shop = models.CharField(max_length=120, blank = True)
	price = models.IntegerField(blank=True, default=0)
	url = models.CharField(max_length=120, blank = True)
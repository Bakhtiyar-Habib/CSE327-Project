from django.db import models

# Create your models here.
class FootwearMen(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(default = "default.jpg", blank=True)
	brand = models.CharField(max_length=120, blank = True)
	shop = models.CharField(max_length=120, blank = True)
	price = models.IntegerField(blank=True, default=0)
	url = models.CharField(max_length=120, blank = True)

class FootwearWomen(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(default = "default.jpg", blank=True)
	brand = models.CharField(max_length=120, blank = True)
	shop = models.CharField(max_length=120, blank = True)
	price = models.IntegerField(blank=True, default=0)
	url = models.CharField(max_length=120, blank = True)
from django.db import models

# Create your models here.
class Brands(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(default = "default.jpg", blank=True)
	categoryname = models.CharField(max_length=120)
	link = models.CharField(max_length=120, blank = True)


class Brands_detail(models.Model):
	brand_name = models.CharField(max_length=120)
	title = models.CharField(max_length=120)
	photo = models.ImageField(default = "default.jpg", blank=True)
	price = models.IntegerField(blank=True)
	categoryname = models.CharField(max_length=120)
	link = models.CharField(max_length=120, blank = True)


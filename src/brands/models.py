from django.db import models

# Create your models here.
class Brands(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(default = "default.jpg", blank=True)
	categoryname = models.CharField(max_length=120)
	link = models.CharField(max_length=120, blank = True)
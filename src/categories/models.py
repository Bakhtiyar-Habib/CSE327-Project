from django.db import models

# Create your models here.

class Categories(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(default = "default.jpg", blank=True)
	subcategories = models.CharField(max_length=120, blank = True)
	link = models.CharField(max_length=200, blank = True)

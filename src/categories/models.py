from django.db import models
from django.urls import reverse
# Create your models here.

class Categories(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(default = "default.jpg", blank=True)
	link = models.CharField(max_length=200, blank = True)

	
#Product Model
class  Product(models.Model):
    title = models.CharField(max_length=300)
    gender = models.CharField(max_length=1)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='products/', blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse("product-detail", kwargs={"slug":self.slug})

    def get_add_to_cart_url(self):
    	return reverse("add-to-cart", kwargs={"slug":self.slug})

    def get_remove_from_cart_url(self):
    	return reverse("remove-from-cart", kwargs={"slug":self.slug})    



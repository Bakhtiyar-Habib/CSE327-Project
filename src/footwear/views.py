from django.shortcuts import render
from categories.models import Product
# Create your views here.
from .models import FootwearMen, FootwearWomen
from brands.models import Brands

def footwear_list_view(request):
	query_set = Product.objects.filter(category=5, gender='m')
	query_set2 = Product.objects.filter(category=5, gender='f')
	query_set3 = Brands.objects.filter(categoryname='footwear')
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set2,
    	'list_brands': query_set3
    }
    
	return render(request, "footwear/footwear_list.html", context)
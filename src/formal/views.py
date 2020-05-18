from django.shortcuts import render
from .models import FormalMen, FormalWomen
from brands.models import Brands
from categories.models import Product
# Create your views here.

def formal_list_view(request):
	query_set = Product.objects.filter(category=1, gender='m')
	query_set2 = Product.objects.filter(category=1, gender='f')
	query_set3 = Brands.objects.filter(categoryname='formal')
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set2,
    	'list_brands': query_set3
    }
    
	return render(request, "formal/formal_list.html", context)




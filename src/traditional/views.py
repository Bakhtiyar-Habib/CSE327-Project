from django.shortcuts import render
from .models import TraditionalMen, TraditionalWomen
from brands.models import Brands
# Create your views here.

def traditional_list_view(request):
	query_set = TraditionalMen.objects.all()
	query_set2 = TraditionalWomen.objects.all()
	query_set3 = Brands.objects.filter(categoryname='traditional')
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set2,
    	'list_brands': query_set3
    }
    
	return render(request, "traditional/traditional_list.html", context)
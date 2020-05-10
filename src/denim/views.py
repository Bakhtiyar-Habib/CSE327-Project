from django.shortcuts import render
from .models import DenimMen, DenimWomen
from brands.models import Brands
# Create your views here.

def denim_list_view(request):
	query_set = DenimMen.objects.all()
	query_set2 = DenimWomen.objects.all()
	query_set3 = Brands.objects.filter(categoryname='denim')
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set2,
    	'list_brands': query_set3
    }
    
	return render(request, "denim/denim_list.html", context)

from django.shortcuts import render

# Create your views here.
from .models import FootwearMen, FootwearWomen
from brands.models import Brands

def footwear_list_view(request):
	query_set = FootwearMen.objects.all()
	query_set2 = FootwearWomen.objects.all()
	query_set3 = Brands.objects.filter(categoryname='footwear')
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set2,
    	'list_brands': query_set3
    }
    
	return render(request, "footwear/footwear_list.html", context)
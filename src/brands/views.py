from django.shortcuts import render
from .models import Brands
# Create your views here.


def brand_list_view(request):
	query_set = Brands.objects.all()
	context = {
    	'object_list': query_set
    }
    
	return render(request, "brands/brands_list.html", context)
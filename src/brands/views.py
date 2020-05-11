from django.shortcuts import render
from .models import Brands, Brands_detail
# Create your views here.


def brand_list_view(request):
	query_set = Brands.objects.all()
	context = {
    	'object_list': query_set
    }
    
	return render(request, "brands/brands_list.html", context)


def levis_detail_view(request):
	query_set = Brands_detail.objects.filter(brand_name='levis')
	context = {
		'object_list': query_set
	}

	return render(request, "brands/levis_list.html", context)


def everlane_detail_view(request):
	query_set = Brands_detail.objects.filter(brand_name='everlane')
	context = {
		'object_list': query_set
	}

	return render(request, "brands/everlane_list.html", context)

def marksandspencer_detail_view(request):
	query_set = Brands_detail.objects.filter(brand_name='marks & spencer')
	context = {
		'object_list': query_set
	}

	return render(request, "brands/marksandspencer_list.html", context)

from django.shortcuts import render
from .models import Brands, Brands_detail
from casual.models import CasualMenT, CasualWomenT, CasualMenPant, CasualWomenPant
from denim.models import DenimMen, DenimWomen
from footwear.models import FootwearMen, FootwearWomen
from formal.models import FormalMen, FormalWomen
from traditional.models import TraditionalMen, TraditionalWomen
from categories.models import Product
# Create your views here.


def brand_list_view(request):
	query_set = Brands.objects.all()
	context = {
    	'object_list': query_set
    }
    
	return render(request, "brands/brands_list.html", context)


def levis_detail_view(request):
	query_set1 = Product.objects.filter(brand__iexact='levis', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='levis', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/levis_list.html", context)


def everlane_detail_view(request):
	query_set1 = Product.objects.filter(brand__iexact='everlane', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='everlane', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/everlane_list.html", context)

def marksandspencer_detail_view(request):
	query_set1 = Product.objects.filter(brand__iexact='m&s', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='m&s', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/marksandspencer_list.html", context)

def fitelegance_detail_view(request):
	query_set1 = Product.objects.filter(brand__iexact='fitelegance', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='fitelegance', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/fitelegance_list.html", context)


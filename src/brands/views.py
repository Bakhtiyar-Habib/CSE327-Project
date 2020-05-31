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
	query_set1 = Product.objects.filter(brand__iexact='fit elegance', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='fit elegance', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/fitelegance_list.html", context)

def diesel_detail_view(request):
	query_set1 = Product.objects.filter(brand__iexact='diesel', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='diesel', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/diesel_list.html", context)

def ralphlauren_detail_view(request):
	query_set1 = Product.objects.filter(brand__iexact='ralph lauren', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='ralph lauren', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/ralphlauren_list.html", context)

def aarong_detail_view(request):
	query_set1 = Product.objects.filter(brand__iexact='aarong', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='aarong', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/aarong_list.html", context)

def dorjibari_detail_view(request):
	query_set1 = Product.objects.filter(brand__iexact='dorjibari', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='dorjibari', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/dorjibari_list.html", context)

def bata_detail_view(request):
	query_set1 = Product.objects.filter(brand__iexact='bata', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='bata', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/bata_list.html", context)

def adidas_detail_view(request):
	query_set1 = Product.objects.filter(brand__iexact='adidas', gender='m')
	query_set2 = Product.objects.filter(brand__iexact='adidas', gender='f')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/adidas_list.html", context)	
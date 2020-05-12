from django.shortcuts import render
from .models import Brands, Brands_detail
from casual.models import CasualMenT, CasualWomenT, CasualMenPant, CasualWomenPant
from denim.models import DenimMen, DenimWomen
from footwear.models import FootwearMen, FootwearWomen
from formal.models import FormalMen, FormalWomen
from traditional.models import TraditionalMen, TraditionalWomen
# Create your views here.


def brand_list_view(request):
	query_set = Brands.objects.all()
	context = {
    	'object_list': query_set
    }
    
	return render(request, "brands/brands_list.html", context)


def levis_detail_view(request):
	query_set1 = DenimMen.objects.filter(brand='levis')
	query_set2 = DenimWomen.objects.filter(brand='levis')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/levis_list.html", context)


def everlane_detail_view(request):
	query_set1 = DenimMen.objects.filter(brand='everlane')
	query_set2 = DenimWomen.objects.filter(brand='everlane')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/everlane_list.html", context)

def marksandspencer_detail_view(request):
	query_set1 = FormalMen.objects.filter(brand='Marks & Spencer')
	query_set2 = FormalWomen.objects.filter(brand='Marks & Spencer')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/marksandspencer_list.html", context)

def fitelegance_detail_view(request):
	query_set1 = FormalMen.objects.filter(brand='Fit Elegance')
	query_set2 = FormalWomen.objects.filter(brand='Fit Elegance')
	context = {
		'object_listmen': query_set1,
		'object_listwomen': query_set2
	}

	return render(request, "brands/fitelegance_list.html", context)


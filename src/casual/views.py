from django.shortcuts import render
from .models import CasualMenT, CasualWomenT
from brands.models import Brands
# Create your views here.

def casual_list_view(request):
	query_set = CasualMenT.objects.all()
	query_set2 = CasualWomenT.objects.all()
	query_set3 = Brands.objects.filter(categoryname='casual')
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set2,
    	'list_brands': query_set3
    }
    
	return render(request, "casual/casual_list.html", context)
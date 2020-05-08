from django.shortcuts import render
from .models import CasualMenT, CasualWomenT
# Create your views here.

def casual_list_view(request):
	query_set = CasualMenT.objects.all()
	query_set2 = CasualWomenT.objects.all()
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set2
    }
    
	return render(request, "casual/casual_list.html", context)
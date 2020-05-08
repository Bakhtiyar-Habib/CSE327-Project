from django.shortcuts import render
from .models import TraditionalMen, TraditionalWomen
# Create your views here.

def traditional_list_view(request):
	query_set = TraditionalMen.objects.all()
	query_set2 = TraditionalWomen.objects.all()
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set2
    }
    
	return render(request, "traditional/traditional_list.html", context)
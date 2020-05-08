from django.shortcuts import render
from .models import DenimMen, DenimWomen
# Create your views here.

def denim_list_view(request):
	query_set = DenimMen.objects.all()
	query_set2 = DenimWomen.objects.all()
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set2
    }
    
	return render(request, "denim/denim_list.html", context)

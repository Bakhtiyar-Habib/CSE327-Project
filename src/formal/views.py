from django.shortcuts import render
from .models import FormalMen, FormalWomen
# Create your views here.

def formal_list_view(request):
	query_set = FormalMen.objects.all()
	query_set1 = FormalWomen.objects.all()
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set1
    }
    
	return render(request, "formal/formal_list.html", context)




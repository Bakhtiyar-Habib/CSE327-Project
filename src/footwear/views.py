from django.shortcuts import render

# Create your views here.
from .models import FootwearMen, FootwearWomen

def footwear_list_view(request):
	query_set = FootwearMen.objects.all()
	query_set2 = FootwearWomen.objects.all()
	context = {
    	'object_listmen': query_set,
    	'object_listwomen': query_set2
    }
    
	return render(request, "footwear/footwear_list.html", context)
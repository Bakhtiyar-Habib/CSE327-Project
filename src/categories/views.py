from django.shortcuts import render
from .models import Categories
# Create your views here.

def category_detail_view(request):
	obj = Categories.objects.get(id=1)
	context = {
    	'object': obj
    }
    
	return render(request, "categories/categories_detail.html", context)



def category_list_view(request):
	query_set = Categories.objects.all()
	context = {
    	'object_list': query_set
    }
    
	return render(request, "categories/categories_list.html", context)
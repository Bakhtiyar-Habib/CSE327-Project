from django.shortcuts import render
from .models import Shops
# Create your views here.

def shop_list_view(request):
	query_set = Shops.objects.all()
	context = {
    	'object_list': query_set
    }
    
	return render(request, "shops/shops_list.html", context)
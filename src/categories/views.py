from django.shortcuts import render, get_object_or_404
from .models import Categories, Product
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
    
	return render(request, "categories/categories_list1.html", context)


def product_detail_view(request, slug):
	#obj = Product.objects.get(id=id)
	obj = get_object_or_404(Product, slug=slug)
	context = {
		"object":obj
	}
	return render(request, "categories/product_detail.html", context)
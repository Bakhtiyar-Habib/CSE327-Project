from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def product_view(request, *args, **kwargs):
	return render(request, "product.html", {})

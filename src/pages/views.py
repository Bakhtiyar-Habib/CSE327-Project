from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "home1.html", {})


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def product_view(request, *args, **kwargs):
	return render(request, "product.html", {})

def allshops_view(request, *args, **kwargs):
	return render(request, "allshops.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

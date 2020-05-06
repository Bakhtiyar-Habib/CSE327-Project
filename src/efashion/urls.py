"""efashion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pages.views import home_view
from pages.views import about_view
from pages.views import product_view
from pages.views import allshops_view
from pages.views import contact_view
from categories.views import category_detail_view, category_list_view
from brands.views import brand_list_view

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('about/', about_view),
    path('products/', product_view),
    path('allshops/', allshops_view),
    path('contact/', contact_view),

    path('products/categories/', category_list_view),
    path('products/create/list/', category_list_view),
    path('products/brands/', brand_list_view),

    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
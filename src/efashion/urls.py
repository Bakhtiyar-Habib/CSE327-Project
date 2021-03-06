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

from brands.views import brand_list_view, levis_detail_view, everlane_detail_view, marksandspencer_detail_view, fitelegance_detail_view, diesel_detail_view, ralphlauren_detail_view, aarong_detail_view, dorjibari_detail_view, bata_detail_view, adidas_detail_view

from shops.views import shop_list_view

from formal.views import formal_list_view
from denim.views import denim_list_view
from casual.views import casual_list_view
from traditional.views import traditional_list_view
from footwear.views import footwear_list_view

from accounts.views import signup_view, login_view, logout_view
from cart.views import add_to_cart, remove_from_cart, OrderSummaryView


#for test
from categories.views import product_detail_view

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
    path('products/shops/', shop_list_view),

    path('products/categories/formal', formal_list_view),
    path('products/categories/denim', denim_list_view),
    path('products/categories/casual', casual_list_view),
    path('products/categories/traditional', traditional_list_view),
    path('products/categories/footwear', footwear_list_view),

    #brands
    path('products/brands/levis', levis_detail_view),
    path('products/brands/everlane', everlane_detail_view),
    path('products/brands/marksandspencer', marksandspencer_detail_view),
    path('products/brands/fitelegance', fitelegance_detail_view),
    path('products/brands/diesel', diesel_detail_view),
    path('products/brands/ralphlauren', ralphlauren_detail_view),
    path('products/brands/aarong', aarong_detail_view),
    path('products/brands/dorjibari', dorjibari_detail_view),
    path('products/brands/bata', bata_detail_view),
    path('products/brands/adidas', adidas_detail_view),   

    path('signup/', signup_view),
    path('login/', login_view),
    path('logout/', logout_view),

    #CART
    path('addtocart/<slug>', add_to_cart, name='add-to-cart'),
    path('removefromcart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),

    path('admin/', admin.site.urls),




    #for test
    path('products/<str:slug>/', product_detail_view, name="product-detail"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
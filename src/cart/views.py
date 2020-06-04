from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from cart.models import Cart, Order, OrderItem
from categories.models import Product 
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# Add to Cart View

def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create( #'created' because it is returning tuple to us
        item=item, 
        user=request.user, 
        ordered=False) #makes sure we are not getting an item that has been already purchased
    order_qs = Order.objects.filter(user=request.user, ordered=False) #to make sure we are only getting orders not completed yet
    if order_qs.exists(): #qs=query set
        order = order_qs[0]
    #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists(): #means item is already in cart
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
            return redirect("product-detail", slug=slug)
        else: #if not in order
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
            return redirect("product-detail", slug=slug)
    else: #if order_qs does not exist
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect("product-detail", slug=slug)
    return redirect("product-detail", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug) #to get the item we want to remove

    order_qs = Order.objects.filter(user=request.user, ordered=False) #to make sure we are only getting orders not completed yet
    if order_qs.exists(): #qs=query set
        order = order_qs[0] #grabbing the order
    #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists(): #means item is already in cart
            order_item = OrderItem.objects.filter( #'created' because it is returning tuple to us
                item=item, 
                user=request.user, 
                ordered=False
            )[0]
            order.items.remove(order_item) 
            messages.info(request, "This item was removed from your cart")
            return redirect("product-detail", slug=slug)
        else:
            #add message saying user doesn't have order
            messages.info(request, "This item was not in your cart")
            return redirect("product-detail", slug=slug)

    else:
        #add message saying user doesn't have order
        messages.info(request, "You do not have an active order")
        return redirect("product-detail", slug=slug)

#now add messages to template to see them in browser


class OrderSummaryView(View): #first class based view
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, "accounts/order_summary.html", context)
        except ObjectDoesNotExist:
            return redirect("home")

        return render(self.request, "accounts/order_summary.html", context)

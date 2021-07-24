from django.shortcuts import render , get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from .models import Item , Cart , Order

class homeView(ListView):
    model = Item
    template_name = "frontend/index.html"

def add_to_cart(request,slug):
    item = get_object_or_404(Item,slug = slug)
    item_check = Cart.objects.filter(item = item)
    if item_check.exists():
        order = item_check[0]
        order.quantity += 1
        order.save()
    else:
        order_item = Cart.objects.create(item = item)
    return redirect("mainApp:home")

class cartView(ListView):
    model = Cart
    template_name = "frontend/cart.html"

def buyView(request,user):
    try:
        user_cart = Cart.objects.filter(user = request.user)
        cart_order = Order.objects.filter(user = request.user)
        print(cart_order)
        if cart_order.exists():
            old_user = Order.objects.filter(user = request.user)
            print(old_user)
            old_user.items.add(user_cart)
            print('exists')
        else:
            new_user = Order.objects.create(user = request.user)
            print(new_user)
            new_user.items.add(user_cart)
        return redirect("mainApp:home")
    except:
        # Cart.objects.all().delete()
        return redirect('mainApp:home')

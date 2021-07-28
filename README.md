[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# django-smart-basket
<h2>Simple E - Commerce Website made using Django and machine learning(frequency pattern) which can suggest items as per user history</h2><br>
<p>hope you have installed django or else you can follow the command</p><br>
python -m pip install Django
<br>
<h3>Create the project</h3>
django-admin startproject flipkart
<br>
<p>change the directory to the new project folder created</p>
<p>Then create the app for the project</p>
python manage.py startapp mainApp
<br>
<br>
<p>For quick overview of the project you can copy and overwrite the files and folder from the repo to the respective files of django that you have created</p>
<h3>How to run the django server</h3>
python manage.py runserver

<h2>Important Code Snippets</h2>
<p>models.py</p>

```python

from django.db import models
from django.conf import settings
from django.shortcuts import reverse

class Item(models.Model):
    title = models.CharField(max_length = 100)
    price = models.FloatField()
    link = models.URLField()
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("mainApp:cart", kwargs={"slug": self.slug})
    
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank = True,null = True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_absolute_user(self):
        return reverse("mainApp:buy", kwargs={"user": self.user})

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart)
    # ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
        
```
<p>3 set of models of database made<p>
<ul>
    <li>Item</li>
    <li>Cart</li>
    <li>Order</li>
</ul>

<h3>Item</h3>
<p>This model of database will store all the items along with it's picture , description and price</p>

<h3>Cart</h3>
<p>This database will store the user which is logged in,and the items added to cart by user</p>

<h3>Order</h3>
<p>This database will confirm the purchase and clear the Cart database and store the data as transaction history of the user which will be later trained my ML to suggest items to the same user from the Order database</p>

<p>views.py</p>

```python
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

```

from django.urls import path
from .views import homeView ,add_to_cart,cartView,buyView

app_name = 'mainApp'

urlpatterns = [
    path('home/',homeView.as_view(),name = 'home'),
    path('cart_list',cartView.as_view(),name = 'order_items'),
    path('cart/<slug>',add_to_cart,name = 'cart'),
    path('buy/<str:user>',buyView,name = 'buy'),
]
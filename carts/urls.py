
from django.urls import path
from .views import add_cart, cartView, removeCart, removeCartItem
urlpatterns = [
    
    path('',cartView,name="cart"),
    path('add_cart/<int:product_id>',add_cart, name="add_cart"),
    path('remove_cart/<int:product_id>',removeCart, name="remove_cart"),
    
    path('remove_cart_item/<int:product_id>',removeCartItem, name="remove_cart_item")
]

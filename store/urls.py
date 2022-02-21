
from django.urls import path
from .views import productView, search, storeView
urlpatterns = [
    
    path('',storeView,name="store"),
    path('category/<slug:category_slug>/',storeView,name="product_by_category"),
    path('category/<slug:category_slug>/<slug:product_slug>',productView,name="product"),
    path('search/',search,name="search"),
]

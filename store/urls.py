
from django.urls import path
from .views import productView, storeView
urlpatterns = [
    
    path('',storeView,name="store"),
    path('<slug:category_slug>/',storeView,name="product_by_category"),
    path('<slug:category_slug>/<slug:product_slug>',productView,name="product"),
]

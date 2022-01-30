from unicodedata import category
from django.shortcuts import get_object_or_404, render
from categories.models import Categories

from store.models import Product

# Create your views here.

def storeView(request,category_slug=None):
    categories   = None
    products     = None
    print(category_slug)
    
    if category_slug != None:
        categories = get_object_or_404(Categories,slug=category_slug)
        print("cat",categories)
        products   = Product.objects.filter(category=categories,is_available=True)
        counts      = products.count()
    else:
        products    = Product.objects.all().filter(is_available=True)
        counts=products.count()

    context={
        'products':products,
        'counts':counts
    }
    return render(request,"store/store.html",context)



def productView(request,category_slug,product_slug):

    try:
        single_product= Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    context={
        "single_product":single_product
    }
    return render(request,"store/product.html",context)

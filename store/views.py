from unicodedata import category
from django.shortcuts import get_object_or_404, render
from carts.models import CartItem
from carts.views import _cart_id
from categories.models import Categories
from django.db.models import Q

from store.models import Product
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def storeView(request,category_slug=None):
    categories   = None
    products     = None
    
    
    if category_slug != None:
        categories = get_object_or_404(Categories,slug=category_slug)
        products   = Product.objects.filter(category=categories,is_available=True).order_by('id')
        paginator   = Paginator(products,1)
        page        =request.GET.get('page')
        paged_product  =paginator.get_page(page)
        counts      = products.count()
    else:
        products    = Product.objects.all().filter(is_available=True).order_by('id')
        paginator   = Paginator(products,2)
        page        =request.GET.get('page')
        paged_product  =paginator.get_page(page)

        counts=products.count()

    context={
        'products':paged_product,
        'counts':counts
    }
    return render(request,"store/store.html",context)



def productView(request,category_slug,product_slug):

    try:
        single_product  = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart         = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()

    except Exception as e:
        raise e
    context={
        "single_product":single_product,
        "in_cart"         :in_cart
    }
    return render(request,"store/product.html",context)


def search (request):
    if 'keyword' in request.GET:
        keyword= request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-create_date').filter(Q( description__icontains=keyword) | Q(product_name__icontains=keyword))
            counts      = products.count()
    context={
        "products":products,
        "counts":counts
    }
    return render(request,"store/store.html",context)
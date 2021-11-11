from re import template

from django.views.generic import ListView, DetailView
from.models import Product
# Create your views here.
from django.http import HttpResponse


from django.shortcuts import render, redirect
from alexadashcams.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'alexadashcams/home.html', context )


class ProductListView(ListView):
    model = Product 
    template_name = 'alexadashcams/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'products'
    ordering = ['-date_created']
    paginate_by = 12

class ProductDetailView(DetailView):
    model = Product 
    

def about(request):
    # return HttpResponse("We are at about")
    return render(request, 'alexadashcams/about.html')



@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    # return render(request, 'alexadashcams/home.html' )
    return redirect("alexadashcams-home")
    


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
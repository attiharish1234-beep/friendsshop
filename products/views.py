from django.shortcuts import render, get_object_or_404
from .models import Product

# HOME PAGE - SHOW ALL PRODUCTS
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


# PRODUCT DETAIL PAGE
def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product.html", {'product': product})


def save_order(request):
    return render(request, 'payment.html')


def payment(request):
    return render(request, 'payment.html')


def success(request):
    return render(request, 'success.html')
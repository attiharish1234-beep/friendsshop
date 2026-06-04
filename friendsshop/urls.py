from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from products.views import save_order

def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')

def payment(request):
    return render(request, 'payment.html')

def success(request):
    return render(request, 'success.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('product/', product),
    path('payment/', payment),
    path('success/', success),
    path('save-order/', save_order),
]
from django.shortcuts import render, redirect
from .models import Order


def home(request):
    return render(request, "home.html")


def product(request):
    return render(request, "product.html")


def save_order(request):
    if request.method == "POST":
        Order.objects.create(
            product="Comfort Slippers",
            size=request.POST.get("size"),
            full_name=request.POST.get("full_name"),
            address=request.POST.get("address"),
            phone=request.POST.get("phone"),
            payment_status="Pending"
        )
        return redirect('/payment/')

    return redirect('/product/')


def payment(request):
    return render(request, "payment.html")


def success(request):
    return render(request, "success.html")
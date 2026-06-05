from django.shortcuts import render, redirect
from .models import Order

def save_order(request):
    if request.method == "POST":
        Order.objects.create(
            product="Comfort Slippers",
            size=request.POST.get("size"),
            full_name=request.POST.get("full_name"),
            address=request.POST.get("address"),
            phone=request.POST.get("phone"),
            payment_status="pending"
        )
        return redirect('/payment/')

    return redirect('/product/')
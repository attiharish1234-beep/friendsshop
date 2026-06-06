from django.shortcuts import render, redirect
from .models import Order


def save_order(request):
    if request.method == "GET":
        order = Order.objects.create(
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
    if request.method == "POST":
        txn_id = request.POST.get("txn_id")

        order = Order.objects.last()
        order.txn_id = txn_id
        order.payment_status = "Paid"
        order.save()

        return render(request, "success.html", {"txn_id": txn_id})

    return redirect('/')


def home(request):
    return render(request, "home.html")
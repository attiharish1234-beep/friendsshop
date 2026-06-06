from django.shortcuts import render, redirect
from .models import Order


def home(request):
    return render(request, "home.html")


def product(request):
    return render(request, "product.html")


def slippers(request):
    return render(request, "slippers.html")


def sandals(request):
    return render(request, "sandals.html")


def footwear(request):
    return render(request, "footwear.html")


def save_order(request):
    if request.method == "GET":
        Order.objects.create(
            product="Comfort Slippers",
            size=request.GET.get("size"),
            full_name=request.GET.get("full_name"),
            address=request.GET.get("address"),
            phone=request.GET.get("phone"),
            payment_status="Pending"
        )

        return redirect('/payment/')

    return redirect('/product/')


def payment(request):
    return render(request, "payment.html")


def success(request):
    if request.method == "GET":
        txn_id = request.GET.get("txn_id")

        order = Order.objects.last()

        if order:
            order.txn_id = txn_id
            order.payment_status = "Paid"
            order.save()

        return render(request, "success.html")

    return redirect('/')
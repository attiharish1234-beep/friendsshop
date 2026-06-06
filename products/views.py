from django.shortcuts import render, redirect
from .models import Order

# 1. def save_order(request):
    if request.method == "GET":
        product_name = request.GET.get("product")

        Order.objects.create(
            product=product_name,
            size="Free Size",
            full_name="",
            address="",
            phone="",
            payment_status="Pending"
        )

        return redirect('/payment/')

    return redirect('/product/')

# 2. Payment Page
def payment(request):
    return render(request, "payment.html")


# 3. Success Page (after transaction ID or payment)
def success(request):
    if request.method == "POST":
        txn_id = request.POST.get("txn_id")

        # update last order (simple working version)
        order = Order.objects.last()
        order.txn_id = txn_id
        order.payment_status = "Paid"
        order.save()

        return render(request, "success.html", {"txn_id": txn_id})

    return redirect('/')


# 4. Home / fallback (optional)
def home(request):
    return render(request, "home.html")
def save_order(request):
    if request.method == "POST":
        Order.objects.create(
            product="Comfort Slippers",
            size=request.POST.get("size"),
            full_name=request.POST.get("full_name"),
            address=request.POST.get("address") + ", " +
                    request.POST.get("state") + " - " +
                    request.POST.get("pincode"),
            phone=request.POST.get("phone"),
            payment_status="Pending"
        )

        return redirect('/payment/')

    return redirect('/product/')
def product(request):
    product = request.GET.get("product")

    if product == "sandals":
        image = "images/sandals.jpg"
        title = "Sports Sandals"

    elif product == "footwear":
        image = "images/footwear.jpg"
        title = "Daily Wear Footwear"

    else:
        image = "images/slippers.jpg"
        title = "Comfort Slippers"

    return render(request, "product.html", {
        "image": image,
        "title": title
    })
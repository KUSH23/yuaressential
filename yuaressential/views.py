from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True)

    # Get the reviews
    reviews = None
    if products:
        for product in products:
            reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products[:4],
        'reviews': reviews,
    }
    return render(request, 'home.html', context)
from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    latest_products = Product.objects.all().filter(is_available=True).order_by('-modified_date')
    products = Product.objects.all().filter(is_available=True)

    # Get the reviews
    reviews = None
    if products:
        for product in products:
            reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'latest_products': latest_products,
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)
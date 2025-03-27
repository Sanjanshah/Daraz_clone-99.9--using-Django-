from django.shortcuts import render
from .models import Category, Product

def home(request):
    # Fetch all categories
    categories = Category.objects.all()

    # Fetch all products
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'main/index.html', context)

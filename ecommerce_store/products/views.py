from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product

# View to list all products
def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'products/product_list.html', {'products': products})  # Render HTML template

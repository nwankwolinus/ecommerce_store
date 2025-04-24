from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# View to display cart
def view_cart(request):
    return render(request, 'orders/view_cart.html')  # Render cart template

# View to handle checkout
def checkout(request):
    return render(request, 'orders/checkout.html')  # Render checkout template

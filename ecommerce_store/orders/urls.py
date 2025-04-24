from django.urls import path
from . import views

# URLs for the orders app
urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),  # View cart
    path('checkout/', views.checkout, name='checkout'),  # Checkout
]

from django.urls import path
from . import views

# URLs for the products app
urlpatterns = [
    path('', views.product_list, name='product_list'),  # List of products
]

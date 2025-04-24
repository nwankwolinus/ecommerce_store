"""
URL configuration for ecommerce_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# The URL routing for the project
urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # Include the URLs of each app
    path('', include('products.urls')),  # Product catalog
    path('users/', include('users.urls')),  # User authentication and profile
    path('orders/', include('orders.urls')),  # Cart and order management
]

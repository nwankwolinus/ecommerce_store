from django.urls import path
from . import views

# URLs for the users app
urlpatterns = [
    path('signup/', views.signup, name='signup'),  # User signup
    path('login/', views.login_view, name='login'),  # User login
]

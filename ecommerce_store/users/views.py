from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# View to handle user signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save new user
            login(request, form.save())  # Log in after signup
            return redirect('product_list')  # Redirect to product list
    else:
        form = UserCreationForm()  # Create empty signup form
    return render(request, 'users/signup.html', {'form': form})

# View to handle user login
def login_view(request):
    return render(request, 'users/login.html')  # Return login template

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest

# Home page view for users not logged in (redirects to login)
# def home(request):
#     return render(request, 'auth/login.html')

# Register view for guests (users not logged in)
@guest  # Ensuring this is for users not logged in
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user after form validation
            login(request, user)  # Log the user in
            return redirect('login')  # Redirect to home after successful registration
    else:
        form = UserCreationForm()  # For GET request, show an empty form

    return render(request, 'auth/register.html', {'form': form})


# Login view for guests (users not logged in)
@guest  # Ensuring this is for users not logged in
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the user object after form validation
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home after successful login
    else:
        form = AuthenticationForm()  # For GET request, show an empty form

    return render(request, 'auth/login.html', {'form': form})

# Dashboard view for authenticated users
@auth  
def dashboard_view(request):
    return render(request, 'home.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logging out

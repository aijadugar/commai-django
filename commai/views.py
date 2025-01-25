from django.shortcuts import render

# Define the home view
def home(request):
    return render(request, 'home.html')  # Renders the home.html template

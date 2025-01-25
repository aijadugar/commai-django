from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def text_interaction(request):
    return render(request, 'services/text_interaction.html')

def speech_interaction(request):
    return render(request, 'services/speech_interaction.html')

def daily_tasks(request):
    return render(request, 'services/daily_tasks.html')

def partners(request):
    return render(request, 'partners/partners.html')

def contactus(request):
    return render(request, 'more/contactus.html')

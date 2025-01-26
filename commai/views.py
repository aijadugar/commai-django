from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import google.generativeai as genai
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    return render(request, 'home.html')

def text_interaction(request):
    return render(request, 'services/text_interaction.html')

# Configure the Gemini API with the API key
G_API_KEY = 'AIzaSyAh1SVrLBQbEW5OfRsDFxccnNJXe0rpJYY'
genai.configure(api_key=G_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# View to handle the ask functionality
@csrf_exempt
def ask(request):
    if request.method == 'POST':
        user_input = request.body.decode('utf-8')
        
        # Send the user input to the Gemini API and get the response
        response = model.generate_content(user_input)
        
        # Get the response text from Gemini
        ai_response = response.text
        # print(ai_response)
        # Return the AI response as a JSON response
        return JsonResponse({'response': ai_response})
    
    return render(request, 'services/text_interaction.html')

def speech_interaction(request):
    return render(request, 'services/speech_interaction.html')

def daily_tasks(request):
    return render(request, 'services/daily_tasks.html')

def submit_writing_exercise(request):
    """
    Handle the submission of writing exercises.
    """
    if request.method == 'POST':
        writing_task = request.POST.get('writing_task')
        # Save or process the writing task here
        print(f"Writing Task Received: {writing_task}")  # For debugging purposes
        return HttpResponse("Thank you for submitting your writing exercise!")

    return redirect('daily_tasks')  # Redirect to the daily tasks page if not POST

def submit_speaking_exercise(request):
    """
    Handle the submission of speaking exercises.
    """
    if request.method == 'POST':
        speaking_topic = request.POST.get('speaking_topic')
        # Save or process the speaking topic here
        print(f"Speaking Topic Received: {speaking_topic}")  # For debugging purposes
        return HttpResponse("Thank you for submitting your speaking exercise!")

    return redirect('daily_tasks')  # Redirect to the daily tasks page if not POST



def partners(request):
    return render(request, 'partners/partners.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can process the form data here, e.g., save it to a database
        return HttpResponse('Thank you for contacting us!')

    return render(request, 'more/contactus.html')

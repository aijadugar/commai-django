from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.middlewares import auth, guest
import urllib.parse
import re
import os
#added
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from app.middlewares import auth, guest
from commai.intelligence.evaluation_parameters import evaluate_text
from commai.intelligence.grammer_spelling import evaluate_grammer_spelling
from commai.intelligence.level_selector import select_level
from .model import commai_summarys, predict_emotion, recommend_courses

from app import views

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import google.generativeai as genai
from django.views.decorators.csrf import csrf_exempt
import json
import logging

# from .model import SpellCheckerModule
from django import template
from django.contrib import messages

# spell_checker_module=SpellCheckerModule()

register = template.Library()

@register.filter
def get_key(dictionary, key):
    """Retrieve a dictionary value by key in Django templates."""
    return dictionary.get(key, [])


# Home page for logged-in users (the main page of the service)
def home(request):
    return render(request, 'home.html')

def text_interaction(request):
    return render(request, 'services/text_interaction.html')

# Documentation page for CommAI
def documentation(request):
    return render(request, 'documentation.html')

# Path to store conversation history
CONVERSATION_FILE = os.path.join(os.path.dirname(__file__), "conversation.json")

@csrf_exempt
def results(request):
    """Handles conversation submission and renders results.html."""
    if request.method == "POST":
        try:
            conversation_data = json.loads(request.POST.get("conversation", "[]"))

            # Overwrite the conversation file with new conversation data
            with open(CONVERSATION_FILE, "w") as file:
                json.dump(conversation_data, file, indent=4)

        except json.JSONDecodeError:
            conversation_data = []

    else:
        # If not a POST request, load the latest saved conversation
        try:
            with open(CONVERSATION_FILE, "r") as file:
                conversation_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            conversation_data = []

    # Extract all user messages and join them into a single string
    user_text = " ".join(msg["text"] for msg in conversation_data if msg["sender"] == "User")

    # print(user_text)
    
    # Evaluate the conversation
    evaluation = evaluate_text(user_text)
    grammer_spelling = evaluate_grammer_spelling(user_text)
    level = select_level(user_text)
    summary = commai_summarys(user_text)
    emotion = predict_emotion(r"C:\Users\Admin\OneDrive\Desktop\commai-django\commai\intelligence\DATASET\train\7\train_09753_aligned.jpg")
    courses = recommend_courses(user_text).to_dict(orient='records')
    # print(evaluation)
    # print(grammer_spelling)
    # print(level)
    # print(summary)
    # print(emotion)
    # print(courses)
    print("Done from views.py...")

    return render(request, "results.html", {"results": evaluation, "grammer_spelling": grammer_spelling, "level": level, "summary": summary, "emotion": emotion, "courses": courses})

@csrf_exempt
def submit_conversation(request):
    """Saves the entire conversation to file when 'Submit Conversation' is clicked."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            conversation_data = data.get("conversation", [])

            if not conversation_data:
                return JsonResponse({"error": "No conversation data to save"}, status=400)

            # **Overwrite the conversation file**
            with open(CONVERSATION_FILE, "w") as file:
                json.dump(conversation_data, file, indent=4)

            return JsonResponse({"message": "Conversation saved successfully."})

        except Exception as e:
            logger.error(f"Error in submit_conversation view: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)

# Service-related views (no authentication needed)


# Setup Logging
logger = logging.getLogger(__name__)

# Set API Key
G_API_KEY = "AIzaSyC1l9rED1nJeliRvS3LtWD3IxfC_Goue0E"
genai.configure(api_key=G_API_KEY)

# Use a stable Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

@csrf_exempt
def ask(request):
    """Handles user input, generates AI response, but does not store to file."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_input = str(data.get("message", "")).strip()

            if not user_input:
                return JsonResponse({"error": "Message cannot be empty"}, status=400)

            # Read temporary conversation from request (not stored in file yet)
            conversation_data = data.get("conversation", [])
            
            # Generate AI response
            response = model.generate_content(user_input)
            ai_response = response.text.strip() if hasattr(response, "text") else "AI response unavailable."

            # Append to conversation (but don't save yet)
            conversation_data.append({"sender": "User", "text": user_input})
            conversation_data.append({"sender": "AI", "text": ai_response})

            return JsonResponse({"response": ai_response, "conversation": conversation_data})

        except Exception as e:
            logger.error(f"Error in ask view: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)


def speech_interaction(request):
    return render(request, 'services/speech_interaction.html')

def daily_tasks(request):
    return render(request, 'services/daily_tasks.html')

def easy_mode(request):
    return render(request, 'services/easy_mode.html')

# def submit_writing_exercise(request):
#     """Handle the submission of writing exercises."""
#     if request.method == 'POST':
#         text = request.POST.get('writing_task')  # Correct form access
#         corrected_text = spell_checker_module.correct_spell(text)  # Correct spelling mistakes
#         corrected_grammar,errors_count,suggestions = spell_checker_module.get_grammar_errors(text)  # Correct grammar errors
#         # Use Django's messages framework to pass the data to the template
        
#         # Show grammar corrections along with suggestions
#         if errors_count > 0:
#             messages.success(request, f"Corrected text: {corrected_text}")
#             messages.success(request, f"Grammatical Errors & misspelled Words: {corrected_grammar}")
#             # messages.success(request, f"Suggestions: {suggestions}")
#         else:
#             messages.success(request, "No grammar errors found.")
        
#         return redirect('daily_tasks')  # Redirect to the daily tasks page
    
#     return redirect('daily_tasks')  # Redirect to the daily tasks page 

# def submit_speaking_exercise(request):
#     """Handle the submission of speaking exercises."""
#     if request.method == 'POST':
#         speaking_topic = request.POST.get('speaking_topic')
#         # Process the speaking topic here
#         print(f"Speaking Topic Received: {speaking_topic}")  # For debugging purposes
#         return HttpResponse("Thank you for submitting your speaking exercise!")
#     return redirect('daily_tasks')  # Redirect to the daily tasks page if not POST

def partners(request):
    return render(request, 'partners/partners.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Process the form data (e.g., save it to the database)
        return HttpResponse('Thank you for contacting us!')
    return render(request, 'more/contactus.html')



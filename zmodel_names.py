import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
G_API_KEY = os.environ.get('GEMINI_API')
genai.configure(api_key=G_API_KEY)

models = genai.list_models()
for model in models:
    print(model.name)
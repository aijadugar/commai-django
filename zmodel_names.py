import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
# Set API Key
G_API_KEY = os.environ.get('GEMINI_API')
genai.configure(api_key=G_API_KEY)

# List Available Models
models = genai.list_models()
for model in models:
    print(model.name)

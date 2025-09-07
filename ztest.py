import pathlib
import textwrap
from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai

model = genai.GenerativeModel('models/gemini-2.5-flash-lite')

G_API_KEY = os.environ.get('GEMINI_API')

genai.configure(api_key = G_API_KEY)

def prompt():
    input = "What is the meaning of life?"
    response = model.generate_content(input)
    print(response.text)
    return response

if __name__ == '__main__':
    prompt()

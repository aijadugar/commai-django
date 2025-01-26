import pathlib
import textwrap

import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')

G_API_KEY = 'AIzaSyAh1SVrLBQbEW5OfRsDFxccnNJXe0rpJYY'

genai.configure(api_key = G_API_KEY)

def prompt():
    input = "What is the meaning of life?"
    response = model.generate_content(input)
    print(response.text)
    return response

if __name__ == '__main__':
    prompt()
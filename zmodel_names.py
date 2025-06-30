import google.generativeai as genai

# Set API Key
G_API_KEY = "api-key-here"
genai.configure(api_key=G_API_KEY)

# List Available Models
models = genai.list_models()
for model in models:
    print(model.name)

import google.generativeai as genai

# Set API Key
G_API_KEY = "AIzaSyC1l9rED1nJeliRvS3LtWD3IxfC_Goue0E"
genai.configure(api_key=G_API_KEY)

# List Available Models
models = genai.list_models()
for model in models:
    print(model.name)

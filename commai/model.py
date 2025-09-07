# import language_tool_python
# from textblob import TextBlob

# class SpellCheckerModule:
#     def __init__(self):
#         self.spell_check = TextBlob("")  # creating an instance of TextBlob for spell_check
#         self.grammar_check = language_tool_python.LanguageTool('en-US')  # creating an instance of LanguageTool for grammar_check
    
#     def correct_spell(self, text):
#         words = text.split()  # Tokenization
#         corrected_words = []

#         for word in words:
#             corrected_word = str(TextBlob(word).correct())  # correct() fixes spelling errors
#             corrected_words.append(corrected_word)
        
#         return " ".join(corrected_words)

#     def get_grammar_errors(self, text):
#         matches = self.grammar_check.check(text)  # Getting the list of grammar mistakes

#         error_words = []
#         # Iterate through the list of matches and extract the error words using offset and length

#         suggestions=[]

#         for match in matches:
#             # Extract the error word based on the 'offset' and 'length' of the match
#             error_word = text[match.offset:match.offset + match.errorLength]
#             error_words.append(error_word)
#             # Extract suggestions for fixing the error
#             suggestions.append(match.replacements)  # List of suggested corrections
#         error_words_count=len(error_words)
        
#         return error_words, error_words_count, suggestions

# if __name__ == "__main__":
#     obj = SpellCheckerModule()
#     message = "Hello World. I like mashine learning. appple bananna. I wants to eat ornge"
    
#     print("Corrected Spelling:")
#     print(obj.correct_spell(message))  # Calling the spell correction function

#     print("\nGrammar Errors:")
#     print(obj.get_grammar_errors(message))  # Calling the grammar error extraction function


import os
from commai.settings import BASE_DIR
# from transformers import T5Tokenizer, T5ForConditionalGeneration
# import torch
# import torchvision.transforms as transforms
# from PIL import Image
# import torch.nn as nn
# import torch.nn.functional as F
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / 'models'

# For AI Summarizer

# model_path = "commai/intelligence/commai_summarizer_latest"
# models = T5ForConditionalGeneration.from_pretrained(model_path)
# tokenizer = T5Tokenizer.from_pretrained(model_path)

def commai_summary(text):
    input_text = "summarize: " + text
    input_ids = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=1024).input_ids
    output_ids = models.generate(
    input_ids,
    max_length=150,  
    min_length=80,  
    num_beams=5,  
    length_penalty=1.0,   
    temperature=0.8,  
    repetition_penalty=2.0,  
    no_repeat_ngram_size=4,  
    early_stopping=True  
    )
    
    return tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()


# For Emotion detection

# class EmotionCNN(nn.Module):
#     def __init__(self):
#         super(EmotionCNN, self).__init__()
#         self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
#         self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
#         self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
#         self.fc1 = nn.Linear(128 * 6 * 6, 256)
#         self.fc2 = nn.Linear(256, 7)  # 7 classes

#     def forward(self, x):
#         x = F.relu(self.conv1(x))
#         x = F.max_pool2d(x, 2)
#         x = F.relu(self.conv2(x))
#         x = F.max_pool2d(x, 2)
#         x = F.relu(self.conv3(x))
#         x = F.max_pool2d(x, 2)
#         x = x.view(-1, 128 * 6 * 6)
#         x = F.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x

# # Load model
# model = EmotionCNN()
# model.load_state_dict(torch.load(MODELS_DIR / "emotion_cnn.pth"))
# model.eval()

# transform = transforms.Compose([
#     transforms.Grayscale(num_output_channels=1),  # Convert to grayscale
#     transforms.Resize((48, 48)),  # Resize to match training input
#     transforms.ToTensor(),  # Convert to tensor
#     transforms.Normalize(mean=[0.5], std=[0.5])  # Normalize
# ])

# def preprocess_image(image_path):
#     image = Image.open(image_path).convert("L")  # Convert to grayscale
#     image = transform(image)  # Apply transformations
#     image = image.unsqueeze(0)  # Add batch dimension
#     return image

# def predict_emotion(image_path, model=model):
#     image = preprocess_image(image_path)
#     with torch.no_grad():
#         output = model(image)
#         predicted_class = torch.argmax(output, dim=1).item()
#         class_mapping = {0: "Surprised", 1: "Fear", 2: "Disgust", 3: "Happy", 4: "Sad", 5: "Angry", 6: "Neutral"}
#     return class_mapping[predicted_class]


# For Courses Recommender

with open(MODELS_DIR / 'vectorizer.pkl', 'rb') as f:
    main_vectorizer = pickle.load(f)
    
with open(MODELS_DIR / 'course_tfidf.pkl', 'rb') as f:
    course_vector = pickle.load(f)

preprocessed_courses = pd.read_csv(MODELS_DIR / 'proprocessed_courses.csv')

def recommend_courses(user_text):
    user_text = user_text.lower()
    user_vector = main_vectorizer.transform([user_text])
    cos_sim = cosine_similarity(user_vector, course_vector)
    top_indices = cos_sim.argsort()[0][-5:][::-1]
    return preprocessed_courses.iloc[top_indices][['Title', 'URL', 'ShortIntro']]



import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from.env file
G_API_KEY = os.environ.get('GEMINI_API')  # Replace with a secure method to load API key
genai.configure(api_key=G_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

def commai_summarys(text):
    """CommAI's summary generator using Gemini API"""
    base_prompt = (
        "As a CommAI's Summary Generator,\n\n"
        "Summarize the following text in a simple, user-friendly way. "
        "Make it engaging and easy to understand. Also, highlight "
        "key points clearly in a structured format."
    )
    
    # Generate text with the Gemini model
    response = model.generate_content(f"{base_prompt}\n\n{text}")
    
    if response.text:
        return f"CommAI's Summary Generator:\n\n{response.text.strip()}"
    else:
        return "CommAI's Summary Generator:\n\nSummary generation failed."
    
    

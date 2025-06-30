import requests

def evaluate_conversation_grammar(text):
    url = "https://api.languagetool.org/v2/check"

    data = {
        'text': text,
        'language': 'en-US',
    }

    response = requests.post(url, data=data)
    result = response.json()

    corrections = []
    for match in result.get('matches', []):
        start = match['offset']
        end = start + match['length']
        correction = {
            'full_text': text,  # Store full text for reference
            'before_error': text[:start],  # Text before the error
            'error_text': text[start:end],  # The actual error part
            'after_error': text[end:],  # Text after the error
            'suggestion': [sugg['value'] for sugg in match['replacements'][:6]],  # Top 6 suggestions
            'message': match['message'],
            'offset': match['offset'],
            'length': match['length']
        }
        corrections.append(correction)

    return corrections

def evaluate_grammer_spelling(text):
    if text is None:
        return {"Grammar and Spelling": []}
    
    return {"Grammar and Spelling": evaluate_conversation_grammar(text)}



# print(evaluate_grammer_spelling("Remember the name - Ankit and Yash , they are the founders of Commai"))




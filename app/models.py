from django.db import models

# Create your models here.
import language_tool_python
from textblob import TextBlob

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = language_tool_python.LanguageTool('en-US')
    
    def correct_spell(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        
        return " ".join(corrected_words)

    def get_grammar_errors(self, text):
        matches = self.grammar_check.check(text)

        error_words = []

        suggestions=[]

        for match in matches:
            error_word = text[match.offset:match.offset + match.errorLength]
            error_words.append(error_word)
            suggestions.append(match.replacements)
        error_words_count=len(error_words)
        
        return error_words, error_words_count, suggestions

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello World. I like mashine learning. appple bananna. I wants to eat ornge"
    
    print("Corrected Spelling:")
    print(obj.correct_spell(message))

    print("\nGrammar Errors:")
    print(obj.get_grammar_errors(message))
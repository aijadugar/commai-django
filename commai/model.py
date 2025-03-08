import language_tool_python
from textblob import TextBlob

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")  # creating an instance of TextBlob for spell_check
        self.grammar_check = language_tool_python.LanguageTool('en-US')  # creating an instance of LanguageTool for grammar_check
    
    def correct_spell(self, text):
        words = text.split()  # Tokenization
        corrected_words = []

        for word in words:
            corrected_word = str(TextBlob(word).correct())  # correct() fixes spelling errors
            corrected_words.append(corrected_word)
        
        return " ".join(corrected_words)

    def get_grammar_errors(self, text):
        matches = self.grammar_check.check(text)  # Getting the list of grammar mistakes

        error_words = []
        # Iterate through the list of matches and extract the error words using offset and length

        suggestions=[]

        for match in matches:
            # Extract the error word based on the 'offset' and 'length' of the match
            error_word = text[match.offset:match.offset + match.errorLength]
            error_words.append(error_word)
            # Extract suggestions for fixing the error
            suggestions.append(match.replacements)  # List of suggested corrections
        error_words_count=len(error_words)
        
        return error_words, error_words_count, suggestions

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello World. I like mashine learning. appple bananna. I wants to eat ornge"
    
    print("Corrected Spelling:")
    print(obj.correct_spell(message))  # Calling the spell correction function

    print("\nGrammar Errors:")
    print(obj.get_grammar_errors(message))  # Calling the grammar error extraction function

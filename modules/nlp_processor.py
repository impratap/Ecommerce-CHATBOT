import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class NLPProcessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
    
    def preprocess(self, text):
        """
        Preprocess text: lowercase, tokenize, and lemmatize.
        Args:
            text (str): User input text
        Returns:
            list: List of processed tokens
        """
        # Convert to lowercase
        text = text.lower()
        # Tokenize
        tokens = word_tokenize(text)
        # Lemmatize tokens
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return tokens

# Example usage (for testing)
if __name__ == "__main__":
    processor = NLPProcessor()
    sample_text = "Where is my order?"
    print(processor.preprocess(sample_text))  # Output: ['where', 'is', 'my', 'order', '?']
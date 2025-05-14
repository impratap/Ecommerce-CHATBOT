import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import os

class NLPProcessor:
    def __init__(self):
        # Set NLTK data path to a writable directory in Streamlit Cloud
        nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
        nltk.data.path.append(nltk_data_path)
        
        # Download required NLTK data if not present
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt_tab', download_dir=nltk_data_path)
        
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet_tab', download_dir=nltk_data_path)
        
        self.lemmatizer = WordNetLemmatizer()
    
    def preprocess(self, text):
        """
        Preprocess text: lowercase, tokenize, and lemmatize.
        Args:
            text (str): User input text
        Returns:
            list: List of processed tokens
        """
        try:
            text = text.lower()
            tokens = word_tokenize(text)
            tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
            return tokens
        except Exception as e:
            raise Exception(f"Error in text preprocessing: {str(e)}")
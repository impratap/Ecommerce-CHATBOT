import json
import re
from modules.nlp_processor import NLPProcessor
from collections import Counter

class IntentClassifier:
    def __init__(self, intents_file):
        self.nlp_processor = NLPProcessor()
        with open(intents_file, 'r') as f:
            self.intents = json.load(f)['intents']
        self.pattern_cache = {}  # Cache preprocessed patterns
        self._preprocess_patterns()
    
    def _preprocess_patterns(self):
        """Preprocess all patterns and cache them."""
        for intent in self.intents:
            for pattern in intent['patterns']:
                tokens = self.nlp_processor.preprocess(pattern)
                self.pattern_cache[pattern] = tokens
    
    def _compute_similarity(self, user_tokens, pattern_tokens):
        """Compute similarity between user input and pattern using word overlap."""
        user_counter = Counter(user_tokens)
        pattern_counter = Counter(pattern_tokens)
        common = sum((user_counter & pattern_counter).values())
        total = sum(user_counter.values()) + sum(pattern_counter.values())
        return common / total if total > 0 else 0
    
    def classify(self, user_input):
        """
        Classify user input into an intent.
        Args:
            user_input (str): User input text
        Returns:
            str: Intent tag
        """
        # Preprocess user input
        user_tokens = self.nlp_processor.preprocess(user_input)
        user_text = ' '.join(user_tokens)
        best_intent = 'fallback'
        best_score = 0.3  # Minimum similarity threshold
        
        # Try regex for exact matches
        for intent in self.intents:
            for pattern in intent['patterns']:
                pattern_text = ' '.join(self.pattern_cache[pattern])
                regex_pattern = re.compile(r'\b' + re.escape(pattern_text) + r'\b', re.IGNORECASE)
                if regex_pattern.search(user_text):
                    return intent['tag']
        
        # Fall back to bag-of-words similarity
        for intent in self.intents:
            for pattern in intent['patterns']:
                pattern_tokens = self.pattern_cache[pattern]
                score = self._compute_similarity(user_tokens, pattern_tokens)
                if score > best_score:
                    best_score = score
                    best_intent = intent['tag']
        
        return best_intent

# Example usage
if __name__ == "__main__":
    classifier = IntentClassifier('data/intents.json')
    print(classifier.classify("track my order"))  # Output: order_status
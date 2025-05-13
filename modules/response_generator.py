import json
import random

class ResponseGenerator:
    def __init__(self, intents_file):
        # Load intents from JSON
        with open(intents_file, 'r') as f:
            self.intents = json.load(f)['intents']
    
    def generate(self, intent_tag):
        """
        Generate a response for the given intent.
        Args:
            intent_tag (str): Intent tag
        Returns:
            str: Response text
        """
        for intent in self.intents:
            if intent['tag'] == intent_tag:
                return random.choice(intent['responses'])
        return "Error: Intent not found."

# Example usage
if __name__ == "__main__":
    generator = ResponseGenerator('data/intents.json')
    print(generator.generate('greeting'))  # Output: Random greeting response
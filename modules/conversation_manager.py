import logging
from modules.intent_classifier import IntentClassifier
from modules.response_generator import ResponseGenerator

class ConversationManager:
    def __init__(self, intents_file, log_file='logs/conversation.log'):
        self.classifier = IntentClassifier(intents_file)
        self.generator = ResponseGenerator(intents_file)
        self.context = {}  # Store conversation context
        logging.basicConfig(filename=log_file, level=logging.INFO,
                          format='%(asctime)s - %(message)s')
    
    def handle_input(self, user_input):
        # Check if user is responding to a previous request
        if self.context.get('awaiting_order_id') and user_input.isalnum():
            order_id = user_input
            self.context = {}  # Clear context
            response = f"Got your order ID: {order_id}. Checking status... (Placeholder response)."
            logging.info(f"User: {user_input} | Intent: order_id_response | Response: {response}")
            return response
        
        # Classify intent
        intent = self.classifier.classify(user_input)
        
        # Handle context-sensitive intents
        if intent in ['order_status', 'order_cancellation', 'return_policy', 'return_status', 'refund_status']:
            self.context['awaiting_order_id'] = True
            response = self.generator.generate(intent)
        else:
            self.context = {}  # Clear context if not relevant
            response = self.generator.generate(intent)
        
        # Log interaction
        logging.info(f"User: {user_input} | Intent: {intent} | Response: {response}")
        return response
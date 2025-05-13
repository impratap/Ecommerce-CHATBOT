from modules.conversation_manager import ConversationManager

def main():
    print("E-Commerce Chatbot: Type 'exit' to quit.")
    manager = ConversationManager('data/intents.json')
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = manager.handle_input(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
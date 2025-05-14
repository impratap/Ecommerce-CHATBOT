import streamlit as st
from modules.conversation_manager import ConversationManager

# Initialize Streamlit app
st.title("E-Commerce Chatbot")
st.write("Ask about orders, returns, products, or anything else! Type 'exit' to end the session.")

# Initialize conversation manager
try:
    if 'manager' not in st.session_state:
        st.session_state.manager = ConversationManager('data/intents.json')
except Exception as e:
    st.error(f"Failed to initialize chatbot: {str(e)}")
    st.stop()

# Initialize conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", key="user_input", placeholder="Type your message here...")

# Process input when submitted
if user_input:
    try:
        if user_input.lower() == 'exit':
            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("Chatbot", "Goodbye! Thanks for chatting."))
        else:
            # Get response from conversation manager
            response = st.session_state.manager.handle_input(user_input)
            # Update history
            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("Chatbot", response))
    except Exception as e:
        st.error(f"Error processing input: {str(e)}")
        response = "Sorry, something went wrong. Please try again."
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Chatbot", response))

# Display conversation history
if st.session_state.history:
    st.write("**Conversation History**")
    for speaker, text in st.session_state.history:
        if speaker == "You":
            st.markdown(f"**{speaker}**: {text}")
        else:
            st.markdown(f"**{speaker}**: *{text}*")

# Optional: Clear chat history
if st.button("Clear Chat"):
    st.session_state.history = []
    st.rerun()
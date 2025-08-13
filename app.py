import streamlit as st
from transformers import pipeline

# ------------------------------
# 1. Emotion detection model
# ------------------------------
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=False
)

def detect_emotion(text):
    """Detect emotion from user input"""
    result = emotion_model(text)[0]
    emotion = result['label']  # e.g., 'sadness', 'joy', etc.
    return emotion

# ------------------------------
# 2. Empathetic reply function
# ------------------------------
def empathetic_reply(user_input):
    emotion = detect_emotion(user_input)
    emotion = emotion.lower()
    
    # Reflect user input + comfort
    if emotion in ["sadness", "fear", "anger"]:
        return f"It sounds like you're feeling {emotion} right now. I'm really sorry you're going through this. Remember, it's okay to feel this way and you're not alone."
    elif emotion in ["joy", "surprise"]:
        return f"It seems like you're feeling {emotion}! I'm glad to hear that. Keep embracing the positive moments in your life."
    else:
        return f"I hear you. You said: '{user_input}'. I'm here to listen and support you."

# ------------------------------
# 3. Streamlit UI
# ------------------------------
st.title("💬 Mental Health Support Chatbot")
st.write("Hi, I’m here to listen. How are you feeling today?")

if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:")

if st.button("Send") and user_input.strip():
    # Save user message
    st.session_state.messages.append(("You", user_input))
    
    # Generate empathetic response
    bot_response = empathetic_reply(user_input)
    st.session_state.messages.append(("Bot", bot_response))

# Display chat history
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**{sender}:** {msg}")
    else:
        st.markdown(f"*{sender}:* {msg}")

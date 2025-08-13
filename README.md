# 💬 Mental Health Support Chatbot
📌 Project Summary:
This project builds an interactive Streamlit web application that offers personalized, empathetic support for users experiencing various mental health states. The chatbot detects the user’s emotions from natural text input and provides context-aware, comforting responses. It demonstrates safe and responsible use of AI for sensitive topics like mental well-being.

The app accepts free-form text from users, detects underlying emotions using a pretrained emotion classification model, and generates empathetic responses through a combination of rule-based prompts and AI-powered reasoning.

# 📂 Dataset / Inputs:

- User’s text input describing their current feelings or experiences

- Emotion detection model (j-hartmann/emotion-english-distilroberta-base)

Optional: Predefined templates for fallback responses

# 🛠️ Technologies Used:

- Python Libraries: Streamlit, transformers, nltk, re

- Hugging Face Models:

- Emotion Detection: j-hartmann/emotion-english-distilroberta-base


# 🛠️ Project Workflow:

- User enters free-form text describing their current feelings in the Streamlit app.

- Text is analyzed using the emotion detection model to classify emotions (e.g., sadness, joy, anger, fear, surprise).

- The chatbot generates an empathetic response based on the detected emotion.

- Responses are reflective and comforting, either using predefined templates or AI-generated text.

- Chat history is maintained in the interface for continuous conversation.

# 🧠 Key Features:

- Detects a wide range of emotions from natural text input

- Provides context-aware, empathetic responses

- Maintains chat history for ongoing conversations

- Safe for sensitive topics, ensuring no off-topic or sarcastic replies

- Simple, user-friendly interface built with Streamlit

- Demonstrates practical use of NLP and AI for social impact


<img width="1582" height="788" alt="Screenshot 2025-08-13 130540" src="https://github.com/user-attachments/assets/ccd8c4ad-b2f3-423e-8d3d-d9e6f8ed9f78" />

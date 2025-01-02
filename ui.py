import streamlit as st
from app2 import speak, listen

# Define the questions
questions = [
    "Please enter your Name, Phone Number, and Email Address.",
    "Are you a fresher or an experienced professional?",
    "Let's define your career objective. Choose 'AI suggestion' or 'Create from scratch'.",
    "Enter your highest qualification (e.g., Graduation, Post Graduation).",
    "Let's define your skills. Enter your primary, secondary, and additional skills.",
    "How many projects would you like to add? (2, 3, or 4)",
    "Have you done any internships? (yes/no)",
    "How many certifications would you like to add? (1, 2, or 3)",
    "How many achievements would you like to add? (1, 2, or 3)",
    "Enter your hobbies.",
    "Enter languages you know.",
    "Choose a template (1, 2, 3, or 4).",
    "Submitting your resume..."
]

# Initialize session state for conversation history and question index
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

# Display chat messages from history on app rerun
for message in st.session_state.conversation:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Get the current question
if st.session_state.question_index < len(questions):
    current_question = questions[st.session_state.question_index]
    speak(current_question)
    st.session_state.conversation.append({'role': 'AI', 'content': current_question})

    # Display AI question in chat message container
    with st.chat_message('AI'):
        st.markdown(current_question)

    # Accept user input
    if prompt := st.chat_input("Your response:"):
        # Add user message to chat history
        st.session_state.conversation.append({'role': 'user', 'content': prompt})
        # Display user message in chat message container
        with st.chat_message('user'):
            st.markdown(prompt)
        # Move to the next question
        st.session_state.question_index += 1
else:
    st.write("Resume creation process completed successfully!")

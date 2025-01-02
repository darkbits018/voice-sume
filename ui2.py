import streamlit as st

# Define the questions
questions = [
    "Please enter your Name, Phone Number, and Email Address.",
    "Are you a fresher or an experienced professional?",
    "Let's define your career objective. Choose 'AI suggestion' or 'Create from scratch'."
]

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'name' not in st.session_state:
    st.session_state.name = ''
if 'phone' not in st.session_state:
    st.session_state.phone = ''
if 'email' not in st.session_state:
    st.session_state.email = ''
if 'job_role' not in st.session_state:
    st.session_state.job_role = ''
if 'career_objective' not in st.session_state:
    st.session_state.career_objective = ''
if 'career_mode' not in st.session_state:
    st.session_state.career_mode = ''


# Helper function to generate career objective using AI
def generate_career_objective(job_role):
    return f"As a passionate and dedicated individual, I aim to excel in the role of {job_role}, leveraging my skills to contribute to organizational growth and achieve personal development."


# Display previous chat messages
for message in st.session_state.conversation:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Handle the current question
if st.session_state.question_index < len(questions):
    current_question = questions[st.session_state.question_index]

    # Add the current question to the conversation if not already added
    if not st.session_state.conversation or \
            st.session_state.conversation[-1]['content'] != current_question:
        st.session_state.conversation.append({'role': 'AI', 'content': current_question})
        with st.chat_message('AI'):
            st.markdown(current_question)

    # Handle user input for each question
    if current_question == "Please enter your Name, Phone Number, and Email Address.":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.session_state.name = st.text_input("Name", value=st.session_state.name)
        with col2:
            st.session_state.phone = st.text_input("Phone Number", value=st.session_state.phone)
        with col3:
            st.session_state.email = st.text_input("Email Address", value=st.session_state.email)

        if st.session_state.name and st.session_state.phone and st.session_state.email:
            if st.button("Submit"):
                user_response = f"Name: {st.session_state.name}, Phone Number: {st.session_state.phone}, Email Address: {st.session_state.email}"
                st.session_state.conversation.append({'role': 'user', 'content': user_response})
                st.session_state.question_index += 1
                st.rerun()

    elif current_question == "Are you a fresher or an experienced professional?":
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Fresher"):
                st.session_state.conversation.append({'role': 'user', 'content': 'Fresher'})
                st.session_state.question_index += 1
                st.rerun()
        with col2:
            if st.button("Experienced"):
                st.session_state.conversation.append({'role': 'user', 'content': 'Experienced'})
                st.session_state.question_index += 1
                st.rerun()

    elif current_question == "Let's define your career objective. Choose 'AI suggestion' or 'Create from scratch'.":
        col1, col2 = st.columns(2)
        with col1:
            if st.button("AI Suggestion"):
                st.session_state.conversation.append({'role': 'user', 'content': 'AI Suggestion'})
                st.session_state.career_mode = "AI Suggestion"
                st.session_state.question_index += 1  # Move to the next step
                st.rerun()
        with col2:
            if st.button("Create from Scratch"):
                st.session_state.conversation.append({'role': 'user', 'content': 'Create from Scratch'})
                st.session_state.career_mode = "Create from Scratch"
                st.session_state.question_index += 1  # Move to the next step
                st.rerun()

# Handle AI Suggestion
elif st.session_state.career_mode == "AI Suggestion":
    st.session_state.job_role = st.text_input("Enter your desired job role:", value=st.session_state.job_role)

    if st.button("Generate Career Objective"):
        st.session_state.career_objective = generate_career_objective(st.session_state.job_role)
        st.session_state.conversation.append({'role': 'AI', 'content': st.session_state.career_objective})
        st.rerun()

    if st.session_state.career_objective:
        st.text_area("Edit your career objective:", value=st.session_state.career_objective,
                     key="career_objective_edit")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Edit"):
                st.session_state.career_objective = st.session_state.career_objective_edit
                st.rerun()
        with col2:
            if st.button("Proceed"):
                st.session_state.conversation.append({'role': 'user', 'content': 'Career objective confirmed.'})
                st.session_state.career_mode = ''  # Reset career mode
                st.session_state.question_index += 1
                st.rerun()

# Handle Create from Scratch
elif st.session_state.career_mode == "Create from Scratch":
    st.session_state.career_objective = st.text_area("Write your career objective:",
                                                     value=st.session_state.career_objective)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Edit"):
            st.rerun()
    with col2:
        if st.button("Proceed"):
            st.session_state.conversation.append({'role': 'user', 'content': 'Career objective confirmed.'})
            st.session_state.career_mode = ''  # Reset career mode
            st.session_state.question_index += 1
            st.rerun()

else:
    st.write("Resume creation process completed successfully!")

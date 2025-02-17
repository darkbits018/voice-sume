import streamlit as st
import requests

# Base URL of your Flask app
BASE_URL = "https://voice-sume.onrender.com"


# Helper function to display responses
def display_response(response, route_name):
    st.write(f"### Testing route: `{route_name}`")
    st.write(f"**Status Code:** `{response.status_code}`")
    st.write("**Response JSON:**")
    st.json(response.json())
    st.write("---")


# Streamlit app
def main():
    st.title("Flask API Tester")
    st.write("This app allows you to test all the routes of your Flask API.")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    options = [
        "Start Resume",
        "Set Experience Level",
        "Add Education",
        "Add Skills",
        "Add Projects",
        "Add Internships",
        "Add Certifications",
        "Generate Career Profile",
        "Update Career Profile",
        "Generate Roles and Responsibilities",
        "Get Resume"
    ]
    choice = st.sidebar.selectbox("Choose a route to test:", options)

    if choice == "Start Resume":
        st.header("Start Resume (Basic Information)")
        name = st.text_input("Name", "John Doe")
        phone = st.text_input("Phone", "1234567890")
        email = st.text_input("Email", "john.doe@example.com")
        if st.button("Test /start-resume"):
            data = {"name": name, "phone": phone, "email": email}
            response = requests.post(f"{BASE_URL}/start-resume", json=data)
            display_response(response, "/start-resume")

    elif choice == "Set Experience Level":
        st.header("Set Experience Level")
        experience_level = st.selectbox("Experience Level", ["fresher", "experienced"])
        if st.button("Test /set-experience-level"):
            data = {"experience_level": experience_level}
            response = requests.post(f"{BASE_URL}/set-experience-level", json=data)
            display_response(response, "/set-experience-level")

    elif choice == "Add Education":
        st.header("Add Education")
        education_input = st.text_area("Education Input",
                                       "Bachelor of Science in Computer Science, XYZ University, 2018-2022")
        if st.button("Test /add-education"):
            data = {"education_input": education_input}
            response = requests.post(f"{BASE_URL}/add-education", json=data)
            display_response(response, "/add-education")

    elif choice == "Add Skills":
        st.header("Add Skills")
        skills_sentence = st.text_area("Skills Sentence",
                                       "I am skilled in Python, JavaScript, and React. I also have experience with SQL and MongoDB.")
        if st.button("Test /add-skills"):
            data = {"skills_sentence": skills_sentence}
            response = requests.post(f"{BASE_URL}/add-skills", json=data)
            display_response(response, "/add-skills")

    elif choice == "Add Projects":
        st.header("Add Projects")
        project_input = st.text_area("Project Input",
                                     "Developed a web application using React and Node.js for a university project.")
        if st.button("Test /add-projects"):
            data = {"project_input": project_input}
            response = requests.post(f"{BASE_URL}/add-projects", json=data)
            display_response(response, "/add-projects")

    elif choice == "Add Internships":
        st.header("Add Internships")
        internship_input = st.text_area("Internship Input",
                                        "Interned at ABC Corp as a Software Developer, worked on backend systems using Python and Django.")
        if st.button("Test /add-internships"):
            data = {"internship_input": internship_input}
            response = requests.post(f"{BASE_URL}/add-internships", json=data)
            display_response(response, "/add-internships")

    elif choice == "Add Certifications":
        st.header("Add Certifications")
        certification_input = st.text_area("Certification Input",
                                           "Certified in AWS Solutions Architect - Associate, 2023.")
        if st.button("Test /add-certifications"):
            data = {"certification_input": certification_input}
            response = requests.post(f"{BASE_URL}/add-certifications", json=data)
            display_response(response, "/add-certifications")

    elif choice == "Generate Career Profile":
        st.header("Generate Career Profile")
        job_role = st.text_input("Job Role", "Software Engineer")
        if st.button("Test /generate-career-profile"):
            data = {"job_role": job_role}
            response = requests.post(f"{BASE_URL}/generate-career-profile", json=data)
            display_response(response, "/generate-career-profile")

    elif choice == "Update Career Profile":
        st.header("Update Career Profile")
        updated_profile = st.text_area("Updated Profile",
                                       "Aspiring Software Engineer with expertise in Python, React, and cloud technologies.")
        if st.button("Test /update-career-profile"):
            data = {"updated_profile": updated_profile}
            response = requests.post(f"{BASE_URL}/update-career-profile", json=data)
            display_response(response, "/update-career-profile")

    elif choice == "Generate Roles and Responsibilities":
        st.header("Generate Roles and Responsibilities")
        user_description = st.text_area("User Description", "I worked on developing REST APIs and managing databases.")
        if st.button("Test /generate-roles-responsibilities"):
            data = {"user_description": user_description}
            response = requests.post(f"{BASE_URL}/generate-roles-responsibilities", json=data)
            display_response(response, "/generate-roles-responsibilities")

    elif choice == "Get Resume":
        st.header("Get Resume")
        if st.button("Test /get-resume"):
            response = requests.get(f"{BASE_URL}/get-resume")
            display_response(response, "/get-resume")


# Run the Streamlit app
if __name__ == "__main__":
    main()

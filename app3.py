# app3.py
import requests
from app2 import speak

# API Endpoints (Replace with actual API URLs)
API_ENDPOINTS = {
    "personal_details": "https://example.com/api/personal-details",
    "experience_level": "https://example.com/api/experience-level",
    "career_objective": "https://example.com/api/career-objective",
    "educational_qualifications": "https://example.com/api/educational-qualifications",
    "skills": "https://example.com/api/skills",
    "projects": "https://example.com/api/projects",
    "internships": "https://example.com/api/internships",
    "certifications": "https://example.com/api/certifications",
    "achievements": "https://example.com/api/achievements",
    "hobbies": "https://example.com/api/hobbies",
    "languages": "https://example.com/api/languages",
    "review_finalize": "https://example.com/api/review",
    "template_selection": "https://example.com/api/template",
    "final_submission": "https://example.com/api/submit",
}


# Helper Function: Send data to API
def send_to_api(endpoint, data):
    try:
        response = requests.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with API: {e}")
        return {}


# 1. Collect Personal Details
def collect_personal_details():
    speak("Please enter your Name, Phone Number, and Email Address.")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email Address: ")
    data = {"name": name, "phone": phone, "email": email}
    return send_to_api(API_ENDPOINTS["personal_details"], data)


# 2. Experience Level
def select_experience_level():
    speak("Are you a fresher or an experienced professional?")
    experience = input("Enter 'fresher' or 'experienced': ").lower()
    data = {"experience_level": experience}
    return send_to_api(API_ENDPOINTS["experience_level"], data)


# 3. Define Career Objective
def define_career_objective():
    speak("Let's define your career objective.")
    choice = input("Choose 'AI suggestion' or 'Create from scratch': ").lower()
    if choice == "ai suggestion":
        job_role = input("Please specify your desired job role: ")
        data = {"job_role": job_role}
        response = send_to_api(API_ENDPOINTS["career_objective"], data)
        print("Suggested Career Objective:", response.get("suggested_objective"))
    elif choice == "create from scratch":
        objective = input("Voice out or type your career objective: ")
        data = {"career_objective": objective}
        response = send_to_api(API_ENDPOINTS["career_objective"], data)
    return response


# 4. Educational Qualifications
def define_educational_qualifications():
    speak("Let's define your educational qualifications.")
    qualification = input("Enter your highest qualification (e.g., Graduation, Post Graduation): ")
    details = input("Provide details in the format: Degree, Institution, Year, CGPA: ")
    data = {"highest_qualification": qualification, "details": details}
    return send_to_api(API_ENDPOINTS["educational_qualifications"], data)


# 5. Skills
def define_skills():
    speak("Let's define your skills.")
    primary_skills = input("Enter your primary skills: ")
    secondary_skills = input("Enter your secondary skills: ")
    additional_skills = input("Enter your additional skills: ")
    data = {
        "primary_skills": primary_skills,
        "secondary_skills": secondary_skills,
        "additional_skills": additional_skills,
    }
    return send_to_api(API_ENDPOINTS["skills"], data)


# 6. Projects
def define_projects():
    speak("How many projects would you like to add? (2, 3, or 4): ")
    num_projects = int(input())
    projects = []
    for i in range(num_projects):
        speak(f"Enter details for Project {i + 1}:")
        name = input("Project Name: ")
        description = input("Project Description: ")
        tech_used = input("Technologies Used: ")
        duration = input("Duration: ")
        team_size = input("Team Size: ")
        role = input("Role: ")
        projects.append({
            "name": name,
            "description": description,
            "tech_used": tech_used,
            "duration": duration,
            "team_size": team_size,
            "role": role,
        })
    data = {"projects": projects}
    return send_to_api(API_ENDPOINTS["projects"], data)


# 7. Internships
def define_internships():
    speak("Have you done any internships? (yes/no): ")
    has_internships = input().lower()
    if has_internships == "yes":
        speak("How many internships would you like to add? (1, 2, or 3): ")
        num_internships = int(input())
        internships = []
        for i in range(num_internships):
            speak(f"Enter details for Internship {i + 1}:")
            name = input("Internship Name: ")
            description = input("Internship Description: ")
            tech_used = input("Technologies Used: ")
            duration = input("Duration: ")
            team_size = input("Team Size: ")
            role = input("Role: ")
            internships.append({
                "name": name,
                "description": description,
                "tech_used": tech_used,
                "duration": duration,
                "team_size": team_size,
                "role": role,
            })
        data = {"internships": internships}
        return send_to_api(API_ENDPOINTS["internships"], data)
    return {"message": "No internships added."}


# 8. Certifications
def define_certifications():
    speak("How many certifications would you like to add? (1, 2, or 3): ")
    num_certifications = int(input())
    certifications = []
    for i in range(num_certifications):
        speak(f"Enter details for Certification {i + 1}:")
        name = input("Certification Name: ")
        description = input("Certification Description: ")
        issued_by = input("Issued By: ")
        certifications.append({
            "name": name,
            "description": description,
            "issued_by": issued_by,
        })
    data = {"certifications": certifications}
    return send_to_api(API_ENDPOINTS["certifications"], data)


# 9. Achievements
def define_achievements():
    speak("How many achievements would you like to add? (1, 2, or 3): ")
    num_achievements = int(input())
    achievements = []
    for i in range(num_achievements):
        speak(f"Enter details for Achievement {i + 1}:")
        name = input("Achievement Name: ")
        description = input("Achievement Description: ")
        issued_by = input("Issued By: ")
        achievements.append({
            "name": name,
            "description": description,
            "issued_by": issued_by,
        })
    data = {"achievements": achievements}
    return send_to_api(API_ENDPOINTS["achievements"], data)


# 10. Hobbies
def define_hobbies():
    speak("Enter your hobbies: ")
    hobbies = input("Hobbies: ")
    data = {"hobbies": hobbies}
    return send_to_api(API_ENDPOINTS["hobbies"], data)


# 11. Languages Known
def define_languages():
    speak("Enter languages you know: ")
    languages = input("Languages: ")
    data = {"languages": languages}
    return send_to_api(API_ENDPOINTS["languages"], data)


# 12. Template Selection
def select_template():
    speak("Choose a template (1, 2, 3, or 4): ")
    template_choice = int(input())
    data = {"template": template_choice}
    return send_to_api(API_ENDPOINTS["template_selection"], data)


# 13. Final Submission
def final_submission():
    speak("Submitting your resume...")
    return send_to_api(API_ENDPOINTS["final_submission"], {})


# Main Orchestration
def main():
    collect_personal_details()
    select_experience_level()
    define_career_objective()
    define_educational_qualifications()
    define_skills()
    define_projects()
    define_internships()
    define_certifications()
    define_achievements()
    define_hobbies()
    define_languages()
    select_template()
    final_submission()
    print("Resume creation process completed successfully!")


if __name__ == "__main__":
    main()

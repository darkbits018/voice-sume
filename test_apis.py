import requests

# Base URL of your Flask app
BASE_URL = "http://127.0.0.1:5000"

# Helper function to print responses
def print_response(response, route_name):
    print(f"Testing route: {route_name}")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    print("-" * 50)


# Test 1: Start Resume (Basic Information)
def test_start_resume():
    url = f"{BASE_URL}/start-resume"
    data = {
        "name": "John Doe",
        "phone": "1234567890",
        "email": "john.doe@example.com"
    }
    response = requests.post(url, json=data)
    print_response(response, "/start-resume")


# Test 2: Set Experience Level
def test_set_experience_level():
    url = f"{BASE_URL}/set-experience-level"
    data = {
        "experience_level": "fresher"  # or "experienced"
    }
    response = requests.post(url, json=data)
    print_response(response, "/set-experience-level")


# Test 3: Add Education
def test_add_education():
    url = f"{BASE_URL}/add-education"
    data = {
        "education_input": "Bachelor of Science in Computer Science, XYZ University, 2018-2022"
    }
    response = requests.post(url, json=data)
    print_response(response, "/add-education")


# Test 4: Add Skills
def test_add_skills():
    url = f"{BASE_URL}/add-skills"
    data = {
        "skills_sentence": "I am skilled in Python, JavaScript, and React. I also have experience with SQL and MongoDB."
    }
    response = requests.post(url, json=data)
    print_response(response, "/add-skills")


# Test 5: Add Projects
def test_add_projects():
    url = f"{BASE_URL}/add-projects"
    data = {
        "project_input": "Developed a web application using React and Node.js for a university project."
    }
    response = requests.post(url, json=data)
    print_response(response, "/add-projects")


# Test 6: Add Internships
def test_add_internships():
    url = f"{BASE_URL}/add-internships"
    data = {
        "internship_input": "Interned at ABC Corp as a Software Developer, worked on backend systems using Python and Django."
    }
    response = requests.post(url, json=data)
    print_response(response, "/add-internships")


# Test 7: Add Certifications
def test_add_certifications():
    url = f"{BASE_URL}/add-certifications"
    data = {
        "certification_input": "Certified in AWS Solutions Architect - Associate, 2023."
    }
    response = requests.post(url, json=data)
    print_response(response, "/add-certifications")


# Test 8: Generate Career Profile
def test_generate_career_profile():
    url = f"{BASE_URL}/generate-career-profile"
    data = {
        "job_role": "Software Engineer"
    }
    response = requests.post(url, json=data)
    print_response(response, "/generate-career-profile")


# Test 9: Update Career Profile
def test_update_career_profile():
    url = f"{BASE_URL}/update-career-profile"
    data = {
        "updated_profile": "Aspiring Software Engineer with expertise in Python, React, and cloud technologies."
    }
    response = requests.post(url, json=data)
    print_response(response, "/update-career-profile")


# Test 10: Generate Roles and Responsibilities
def test_generate_roles_responsibilities():
    url = f"{BASE_URL}/generate-roles-responsibilities"
    data = {
        "user_description": "I worked on developing REST APIs and managing databases."
    }
    response = requests.post(url, json=data)
    print_response(response, "/generate-roles-responsibilities")


# Test 11: Get Resume
def test_get_resume():
    url = f"{BASE_URL}/get-resume"
    response = requests.get(url)
    print_response(response, "/get-resume")


# Run all tests
if __name__ == "__main__":
    test_start_resume()
    test_set_experience_level()
    test_add_education()
    test_add_skills()
    test_add_projects()
    test_add_internships()
    test_add_certifications()
    test_generate_career_profile()
    test_update_career_profile()
    test_generate_roles_responsibilities()
    test_get_resume()

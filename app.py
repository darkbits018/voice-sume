from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_services import (
    parse_education_with_ai,
    parse_internship_with_ai,
    parse_project_with_ai,
    parse_certification_with_ai,
    generate_career_profile,
    generate_roles_responsibilities,
    segregate_skills
)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage for resume data (replace with a database in production)
resume_data = {}


@app.route('/start-resume', methods=['POST'])
def start_resume():
    """
    Step 1: Collect basic information (name, phone, email).
    """
    data = request.json
    resume_data['basic_info'] = {
        "name": data.get("name"),
        "phone": data.get("phone"),
        "email": data.get("email")
    }
    return jsonify({"message": "Basic information saved successfully."})


@app.route('/set-experience-level', methods=['POST'])
def set_experience_level():
    """
    Step 2: Set experience level (fresher or experienced).
    """
    data = request.json
    experience_level = data.get("experience_level")
    if experience_level not in ["fresher", "experienced"]:
        return jsonify({"error": "Invalid experience level. Choose 'fresher' or 'experienced'."}), 400

    resume_data['experience_level'] = experience_level
    return jsonify({"message": f"Experience level set to {experience_level}."})


@app.route('/add-education', methods=['POST'])
def add_education():
    """
    Step 3: Add educational qualifications using AI.
    """
    data = request.json
    input_text = data.get("education_input")

    # Parse education using AI
    education = parse_education_with_ai(input_text)
    if not education:
        return jsonify({"error": "Failed to parse education details. Please check the input format."}), 400

    if 'education' not in resume_data:
        resume_data['education'] = []
    resume_data['education'].append(education)

    return jsonify({"message": "Education details added successfully.", "data": education})


@app.route('/add-skills', methods=['POST'])
def add_skills():
    """
    Step 4: Add skills and categorize them into primary, secondary, and additional based on the job role.
    """
    data = request.json
    skills_sentence = data.get("skills_sentence")  # User sends a sentence containing skills

    if not skills_sentence:
        return jsonify({"error": "Skills sentence is required."}), 400

    # Get the job role from the career profile in resume_data
    job_role = resume_data.get('career_profile', {}).get('job_role')
    if not job_role:
        return jsonify({"error": "Job role is required. Please set the career profile first."}), 400

    # Segregate skills into primary, secondary, and additional categories
    categorized_skills = segregate_skills(skills_sentence, job_role)

    if 'error' in categorized_skills:
        return jsonify({"error": categorized_skills['error']}), 400

    # Store the categorized skills in resume_data
    if 'skills' not in resume_data:
        resume_data['skills'] = {}

    # Update the skills dictionary with the categorized skills
    resume_data['skills'].update(categorized_skills)

    response = {
        "message": "Skills added and categorized successfully.",
        "data": categorized_skills
    }

    print(response)  # Print the response for debugging

    return jsonify(response)


@app.route('/add-projects', methods=['POST'])
def add_projects():
    """
    Step 5: Add projects.
    """
    data = request.json
    input_text = data.get("project_input")

    # Parse project using AI
    project = parse_project_with_ai(input_text)
    if not project:
        return jsonify({"error": "Failed to parse project details. Please check the input format."}), 400

    if 'projects' not in resume_data:
        resume_data['projects'] = []
    resume_data['projects'].append(project)

    return jsonify({"message": "Project details added successfully.", "data": project})


@app.route('/add-internships', methods=['POST'])
def add_internships():
    """
    Step 6: Add internships using AI.
    """
    data = request.json
    input_text = data.get("internship_input")

    # Parse internship using AI
    internship = parse_internship_with_ai(input_text)
    if not internship:
        return jsonify({"error": "Failed to parse internship details. Please check the input format."}), 400

    if 'internships' not in resume_data:
        resume_data['internships'] = []
    resume_data['internships'].append(internship)

    return jsonify({"message": "Internship details added successfully.", "data": internship})


@app.route('/add-certifications', methods=['POST'])
def add_certifications():
    """
    Step 7: Add certifications using AI.
    """
    data = request.json
    input_text = data.get("certification_input")

    # Parse certification using AI
    certification = parse_certification_with_ai(input_text)
    if not certification:
        return jsonify({"error": "Failed to parse certification details. Please check the input format."}), 400

    if 'certifications' not in resume_data:
        resume_data['certifications'] = []
    resume_data['certifications'].append(certification)

    return jsonify({"message": "Certification details added successfully.", "data": certification})


@app.route('/generate-career-profile', methods=['POST'])
def generate_career_profile_route():
    """
    Generate a career profile for a fresher.
    """
    data = request.json
    job_role = data.get('job_role')

    if not job_role:
        return jsonify({"error": "Job role is required."}), 400

    response = generate_career_profile(job_role)
    resume_data['career_profile'] = {"job_role": job_role, "profile": response}  # Store as a dictionary
    return jsonify({"response": response})


@app.route('/update-career-profile', methods=['POST'])
def update_career_profile():
    """
    Update the career profile in the resume_data dictionary.
    """
    data = request.json
    updated_profile = data.get('updated_profile')

    if not updated_profile:
        return jsonify({"error": "Updated profile is required."}), 400

    # Replace the existing career profile in resume_data
    resume_data['career_profile'] = updated_profile  # Store as a string
    return jsonify({"message": "Career profile updated successfully.", "data": updated_profile})


@app.route('/generate-roles-responsibilities', methods=['POST'])
def generate_roles_responsibilities_route():
    """
    Generate roles and responsibilities based on the user's description.
    """
    data = request.json
    user_description = data.get('user_description')

    if not user_description:
        return jsonify({"error": "User description is required."}), 400

    response = generate_roles_responsibilities(user_description)
    # Store the generated roles and responsibilities in resume_data
    if 'roles_responsibilities' not in resume_data:
        resume_data['roles_responsibilities'] = []
    resume_data['roles_responsibilities'].append(response)
    return jsonify({"response": response})


# @app.route('/segregate-skills', methods=['POST'])
# def segregate_skills_route():
#     """
#     Segregate skills into primary, secondary, and additional categories.
#     """
#     data = request.json
#     skills = data.get('skills')
#
#     if not skills:
#         return jsonify({"error": "Skills are required."}), 400
#
#     response = segregate_skills(skills)
#     # Store the segregated skills in resume_data
#     if 'segregated_skills' not in resume_data:
#         resume_data['segregated_skills'] = []
#     resume_data['segregated_skills'].append(response)
#
#     return jsonify({"response": response})


@app.route('/get-resume', methods=['GET'])
def get_resume():
    """
    Step 8: Retrieve the complete resume data.
    """
    return jsonify(resume_data)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime
import smtplib
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['DEBUG'] = True

# Data storage (in production, use a proper database)
DATA_FILE = 'data/portfolio_data.json'
MESSAGES_FILE = 'data/messages.json'

def load_data():
    """Load portfolio data from JSON file"""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return get_default_data()

def save_data(data):
    """Save portfolio data to JSON file"""
    os.makedirs('data', exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_default_data():
    """Default portfolio data"""
    return {
        "personal_info": {
            "name": "Samith Shivakumar",
            "title": "Computer Science Student & Aspiring Developer",
            "email": "samithshivakumar1@gmail.com",
            "phone": "+91-XXXXXXXXXX",
            "location": "India",
            "bio": "Passionate computer science student with a strong foundation in programming and web development. Dedicated to continuous learning and building innovative solutions.",
            "linkedin": "https://www.linkedin.com/in/samith-shivakumar-98901430a/",
            "github": "https://github.com/Sam29W"
        },
        "education": [
            {
                "institution": "Jain University",
                "degree": "Bachelor of Technology in Computer Science",
                "duration": "2023-2027",
                "status": "Current"
            },
            {
                "institution": "Christ Junior College",
                "degree": "Pre-University Education",
                "duration": "2021-2023",
                "status": "Completed"
            }
        ],
        "skills": {
            "programming": ["Python", "Java", "C/C++", "JavaScript"],
            "web_development": ["HTML5", "CSS3", "Flask", "Responsive Design"],
            "tools": ["Git", "GitHub", "VS Code", "Linux/Unix"],
            "soft_skills": ["Problem Solving", "Team Collaboration", "Communication", "Critical Thinking"]
        },
        "projects": [
            {
                "name": "Personal Portfolio Website",
                "description": "Responsive portfolio website built with HTML, CSS, and Flask backend",
                "technologies": ["HTML", "CSS", "Python", "Flask"],
                "github_url": "https://github.com/Sam29W/samith-portfolio-v2",
                "live_url": "https://sam29w.github.io/samith-portfolio-v2/"
            }
        ],
        "certifications": [
            "Python Programming Fundamentals",
            "Web Development Basics",
            "Git Version Control"
        ],
        "career_highlights": [
            "Active LeetCode problem solver with focus on algorithms and data structures",
            "Developed multiple web applications using modern technologies",
            "Continuous learner exploring new programming languages and frameworks"
        ]
    }

def load_messages():
    """Load contact messages from JSON file"""
    try:
        with open(MESSAGES_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_message(message_data):
    """Save contact message to JSON file"""
    messages = load_messages()
    message_data['timestamp'] = datetime.now().isoformat()
    message_data['id'] = len(messages) + 1
    messages.append(message_data)
    
    os.makedirs('data', exist_ok=True)
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, indent=2)

@app.route('/')
def home():
    """Serve the main portfolio page"""
    return send_from_directory('.', 'index.html')

@app.route('/api/portfolio')
def get_portfolio_data():
    """API endpoint to get portfolio data"""
    data = load_data()
    return jsonify(data)

@app.route('/api/portfolio', methods=['PUT'])
def update_portfolio_data():
    """API endpoint to update portfolio data"""
    try:
        data = request.get_json()
        save_data(data)
        return jsonify({"message": "Portfolio data updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/contact', methods=['POST'])
def contact_form():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({"error": f"{field} is required"}), 400
        
        # Save message
        save_message(data)
        
        return jsonify({
            "message": "Thank you for your message! I'll get back to you soon.",
            "status": "success"
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/messages')
def get_messages():
    """Get all contact messages (for admin use)"""
    messages = load_messages()
    return jsonify(messages)

@app.route('/api/skills')
def get_skills():
    """Get skills data"""
    data = load_data()
    return jsonify(data.get('skills', {}))

@app.route('/api/projects')
def get_projects():
    """Get projects data"""
    data = load_data()
    return jsonify(data.get('projects', []))

@app.route('/api/education')
def get_education():
    """Get education data"""
    data = load_data()
    return jsonify(data.get('education', []))

@app.route('/api/certifications')
def get_certifications():
    """Get certifications data"""
    data = load_data()
    return jsonify(data.get('certifications', []))

@app.route('/api/personal-info')
def get_personal_info():
    """Get personal information"""
    data = load_data()
    return jsonify(data.get('personal_info', {}))

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Initialize data file if it doesn't exist
    if not os.path.exists(DATA_FILE):
        save_data(get_default_data())
    
    app.run(host='0.0.0.0', port=5000, debug=True)
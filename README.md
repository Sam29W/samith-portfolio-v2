# Samith Shivakumar - Personal Portfolio

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-success)](https://sam29w.github.io/samith-portfolio-v2/)

Modern personal portfolio website showcasing professional experience, education, skills, and certifications with a powerful Flask backend.

## Overview

This is a full-stack responsive personal portfolio website built with HTML, CSS frontend and Python Flask backend. The portfolio showcases my professional journey, including my educational background, technical skills, certifications, and career highlights.

## Features

- **Responsive Design**: Fully responsive layout that works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean and professional design with gradient accents and smooth animations
- **Flask Backend**: RESTful API for dynamic content management and contact form handling
- **Contact Form**: Functional contact form with validation and message storage
- **API Endpoints**: RESTful API for portfolio data management
- **Comprehensive Sections**:
  - About Me
  - Career Highlights
  - Education
  - Skills (organized by category)
  - Certifications
  - Contact Information

## Technologies Used

**Frontend:**
- HTML5
- CSS3
- JavaScript (for API integration)
- Responsive Web Design
- CSS Grid & Flexbox
- CSS Animations

**Backend:**
- Python 3.8+
- Flask 2.3.3
- Flask-CORS
- JSON file-based data storage

## Project Structure

```
samith-portfolio-v2/
├── app.py                  # Main Flask application
├── run.py                  # Application runner script
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── api/
│   └── contact.py         # Contact form API module
├── data/                  # Data storage (auto-generated)
│   ├── portfolio_data.json
│   └── messages.json
├── index.html             # Frontend HTML
├── styles.css             # Frontend CSS
└── README.md             # Project documentation
```

## API Endpoints

### Portfolio Data
- `GET /api/portfolio` - Get complete portfolio data
- `PUT /api/portfolio` - Update portfolio data
- `GET /api/skills` - Get skills data
- `GET /api/projects` - Get projects data
- `GET /api/education` - Get education data
- `GET /api/certifications` - Get certifications data
- `GET /api/personal-info` - Get personal information

### Contact Form
- `POST /api/contact` - Submit contact form
- `GET /api/messages` - Get all messages (admin)
- `PUT /api/messages/<id>` - Update message status

### System
- `GET /api/health` - Health check endpoint

## Getting Started

### View Live Site

Visit the live portfolio at: [https://sam29w.github.io/samith-portfolio-v2/](https://sam29w.github.io/samith-portfolio-v2/)

### Local Development with Backend

1. **Clone the repository:**
```bash
git clone https://github.com/Sam29W/samith-portfolio-v2.git
cd samith-portfolio-v2
```

2. **Set up Python environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables (optional):**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Run the application:**
```bash
python run.py
```

6. **Access the website:**
- Frontend: http://localhost:5000
- API: http://localhost:5000/api/
- Health Check: http://localhost:5000/api/health

### Frontend Only Development

For frontend-only development without the backend:

```bash
# Simply open the HTML file
open index.html
```

## Design Features

- **Color Scheme**: Purple gradient theme (#667eea to #764ba2)
- **Typography**: Segoe UI font family for clean readability
- **Layout**: Grid and flexbox-based responsive layouts
- **Animations**: Smooth fade-in effects and hover transitions
- **Accessibility**: Semantic HTML and proper ARIA labels

## Responsive Breakpoints

- **Desktop**: Full layout with multi-column grids
- **Tablet** (≤768px): Adjusted navigation and single-column layouts
- **Mobile** (≤480px): Optimized spacing and stacked layouts

## Backend Features

### Data Management
- JSON-based data storage for easy content updates
- RESTful API for all portfolio data
- Automatic data initialization with default content

### Contact Form
- Form validation (email format, required fields)
- Message storage with timestamps
- Admin interface for message management
- Status tracking (read/unread)

### Security & Validation
- Input validation and sanitization
- CORS protection
- Error handling and logging
- Environment variable support

## Content Sections

### About
Brief introduction highlighting my dedication to technology and continuous learning.

### Career Highlights
Showcase of professional development activities and technical projects.

### Education
- **Jain University** - Bachelor of Technology in Computer Science (2023-2027)
- **Christ Junior College** - Pre-University Education (2021-2023)

### Skills
Organized into four categories:
- Programming Languages (Python, Java, C/C++, JavaScript)
- Web Development (HTML5, CSS3, Flask, Responsive Design)
- Tools & Technologies (Git, GitHub, VS Code, Linux/Unix)
- Soft Skills (Problem Solving, Team Collaboration, Communication)

### Certifications
Ongoing professional development through online learning platforms and technical certifications.

### Contact
Functional contact form with backend processing and message storage.

Links to professional profiles:
- LinkedIn: [linkedin.com/in/samith-shivakumar-98901430a](https://www.linkedin.com/in/samith-shivakumar-98901430a/)
- GitHub: [github.com/Sam29W](https://github.com/Sam29W)

## Deployment

### Local Deployment
```bash
python run.py
```

### Production Deployment
For production deployment, consider:
- Using a production WSGI server (Gunicorn, uWSGI)
- Setting up proper environment variables
- Using a proper database (PostgreSQL, MySQL)
- Implementing proper logging and monitoring

## Future Enhancements

- Database integration (PostgreSQL/MySQL)
- User authentication for admin panel
- Email notifications for contact form
- Blog section with CMS
- Project showcase with GitHub integration
- Resume download functionality
- Dark mode toggle
- Advanced analytics and metrics
- Docker containerization
- CI/CD pipeline setup

## Contributing

Feel free to fork this repository and customize it for your own portfolio. If you have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is open source and available for personal and educational use.

## Contact

For any inquiries or collaboration opportunities, feel free to reach out:

- **LinkedIn**: [Samith Shivakumar](https://www.linkedin.com/in/samith-shivakumar-98901430a/)
- **GitHub**: [@Sam29W](https://github.com/Sam29W)
- **Email**: samithshivakumar1@gmail.com

---

**Built by Samith Shivakumar**

© 2025 Samith Shivakumar. All rights reserved.
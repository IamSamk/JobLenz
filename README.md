# JobLens Backend

This is the backend for JobLens, a Flask-based job analysis platform that processes resumes and LinkedIn profiles to generate AI-powered insights.

## 🚀 Features
- Resume Upload & AI Analysis
- LinkedIn Profile Processing
- Job Market Insights & Skill Visualization
- Secure API with CORS Support

## 📦 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/joblens-backend.git
   cd joblens-backend
   ```
2. Create a virtual environment & install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 🛠️ Running the Server
```sh
python app.py
```

## 🌍 Deployment on Render
1. Push code to GitHub
2. Deploy on [Render](https://render.com/) as a web service
3. Set environment variables & use `gunicorn`

## 📂 Folder Structure
```
joblens-backend/
│── app.py            # Flask API
│── requirements.txt  # Dependencies
│── Procfile          # Render Deployment
│── .gitignore        # Ignore unnecessary files
│── templates/        # (Optional) HTML templates
│── static/           # (Optional) Static assets
│── README.md         # Project Overview
```

## 🔗 API Endpoints
- `GET /` → Check if backend is running
- `POST /upload` → Upload resume for AI processing
- `POST /linkedin` → Analyze LinkedIn profile

## 💡 Contributing
Feel free to fork and contribute to this project!


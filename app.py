from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "JobLens Backend is Running!"})

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    # Process file (AI analysis to be added later)
    return jsonify({"message": "File received", "filename": file.filename})

@app.route('/linkedin', methods=['POST'])
def analyze_linkedin():
    data = request.get_json()
    linkedin_url = data.get('url')
    if not linkedin_url:
        return jsonify({"error": "No LinkedIn URL provided"}), 400
    # Web scraping / AI analysis to be added
    return jsonify({"message": "LinkedIn URL received", "url": linkedin_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


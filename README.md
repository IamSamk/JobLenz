# JobLenz

JobLenz is an AI-powered job analysis and portfolio evaluation platform. It extracts insights from user portfolios and LinkedIn profiles to recommend personalized career opportunities and visualize key job market trends.

## Features
- 📊 **AI-driven Job Analysis**: Extracts insights from uploaded resumes and LinkedIn profiles.
- 📈 **Data Visualization**: Uses Python libraries (Matplotlib, Seaborn, Plotly) for interactive graphs.
- 🔍 **Real-time Job Market Insights**: Provides dynamic job recommendations.
- 🌐 **Web Scraping**: Extracts key details from LinkedIn profiles.
- 🔄 **REST API Backend**: Built with Flask, deployed on Render.
- 🎨 **Modern UI**: React-based frontend, styled similarly to JobLens_1.

## Installation

### Backend (Flask)
1. Clone the repository:
   ```sh
   git clone https://github.com/IamSamk/JobLenz.git
   cd JobLenz
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set environment variables:
   ```sh
   export PORT=5000
   export GEMINI_API_KEY=your_api_key_here
   export HUGGINGFACE_API_KEY=your_api_key_here
   ```
5. Run the Flask server:
   ```sh
   python app.py
   ```

### Frontend (React)
1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```

## Deployment

### Backend Deployment (Render)
1. Push your code to GitHub.
2. Go to [Render](https://render.com) → Create a **new web service**.
3. Connect your **GitHub repo** and select the **Flask environment**.
4. Set **start command**:
   ```sh
   gunicorn app:app
   ```
5. Add **environment variables**:
   ```sh
   PORT=5000
   GEMINI_API_KEY=your_api_key_here
   HUGGINGFACE_API_KEY=your_api_key_here
   ```
6. Click **Deploy**.

### Frontend Deployment (Netlify)
1. Push your frontend code to GitHub.
2. Go to [Netlify](https://netlify.com) → Create a **new site from Git**.
3. Select your **frontend repo**.
4. Set **build settings**:
   - Build Command: `npm run build`
   - Publish Directory: `dist` (if using Vite) or `build` (if using CRA)
5. Click **Deploy**.

## Usage
- **Visit the hosted frontend URL**.
- Upload a **resume** or **LinkedIn profile URL**.
- AI processes the data and displays **visualized job insights**.

## Technologies Used
- **Backend**: Flask, Gunicorn, Pandas, Hugging Face API, Gemini API
- **Frontend**: React, TailwindCSS
- **Data Visualization**: Matplotlib, Seaborn, Plotly

## License
This project is open-source and licensed under the **MIT License**.

---
🚀 **Developed by [IamSamk](https://github.com/IamSamk)**

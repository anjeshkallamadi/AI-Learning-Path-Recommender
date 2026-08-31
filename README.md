# AI Learning Path Recommender

A full-stack web application that takes a user's natural language learning goal, matches it against a massive course database using a TF-IDF machine learning model, and generates a personalized, step-by-step learning roadmap using Google's Gemini AI.

Created by Kallamadi Anjesh.

## 🚀 Tech Stack

* **Frontend:** Angular (Standalone Components), TypeScript, HTML/CSS
* **Backend:** Django, Django REST Framework, Python
* **Machine Learning / AI:** Scikit-learn (TF-IDF vectorization), Google Gemini API (`gemini-3.6-flash`)

## 🧠 How It Works

1.  The user inputs a learning goal (e.g., "I want to master frontend development") into the Angular chat interface.
2.  The Django backend receives the request and vectorizes the text using a pre-trained TF-IDF model.
3.  The system calculates the cosine similarity against a database of courses and extracts the top 10 unique, highly relevant courses.
4.  The course list and user goal are sent to the Gemini LLM with a strict prompt to generate a chronological learning roadmap.
5.  The Angular frontend parses the resulting JSON and renders a beautiful, interactive vertical timeline UI.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your local machine:
* [Node.js and npm](https://nodejs.org/)
* [Angular CLI](https://angular.io/cli) (`npm install -g @angular/cli`)
* [Python 3.x](https://www.python.org/)

## 💻 Local Setup Instructions

### 1. Clone the Repository
```bash 
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
```
### 2. Backend Setup (Django)
Open a new terminal and navigate to your Django backend folder (e.g., recommender_pro):

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install the required Python packages
pip install django djangorestframework django-cors-headers google-genai scikit-learn pandas numpy joblib python-dotenv

# Set up your environment variables
# Create a .env file in the same directory as your settings.py and add:
# GEMINI_API_KEY=your_actual_api_key_here

# Run Django server
python manage.py runserver

The backend API will now be running at http://localhost:8000/api/generate/.

### Frontend Setup (Angular)
Open a second terminal and navigate to your Angular frontend folder (e.g., learning-path-ui):

# Install Node dependencies
npm install

# Start the Angular development server
ng serve -o

Your browser will automatically open the application at http://localhost:4200/. Type in a learning goal and generate your first roadmap!



### 🚀 Future Enhancements

As this prototype evolves, the following features are planned for future development:

Interactive Progress Dashboard: A visual UI (utilizing Chart.js or ng2-charts) allowing users to check off milestones and visualize their skill development over time.

User Authentication: Enable users to create accounts, save their personalized generated paths, and resume their progress later.

Export Functionality: Allow users to download their custom learning roadmap as a formatted PDF.

### 🤝 Contributing
Contributions, issues, and feature requests are always welcome! Feel free to check the issues page if you want to contribute.

### 📬 Contact
Kallamadi Anjesh

GitHub: @anjeshkallamadi

Project Link: https://github.com/anjeshkallamadi/AI-Learning-Path-Recommender

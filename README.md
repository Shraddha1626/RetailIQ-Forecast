# RetailIQ Forecast

RetailIQ Forecast is a **full-stack sales forecasting web application** built with **Flask (backend)** and **React (frontend)**. It allows users to track product sales, visualize forecasts via interactive charts, and manage user accounts securely.

---

## Features

- User registration and login with hashed passwords
- Dashboard displaying sales forecasts using **pie and bar charts**
- RESTful APIs with Flask and SQLAlchemy
- Responsive React frontend with Chart.js integration

---

## Project Structure

RetailIQ-Forecast2/
├── backend/
│ ├── app.py
│ ├── init_db.py
│ ├── model.py
│ ├── helpers.py
│ └── routes/
│ ├── forecast_routes.py
│ └── user_routes.py
├── frontend/
│ ├── package.json
│ ├── src/
│ │ ├── App.js
│ │ ├── Dashboard.js
│ │ └── components/
│ └── public/
│ └── index.html
├── README.md
└── requirements.txt

---

## Installation

### Backend

1. Create a virtual environment:

```bash
python -m venv venv
Activate the environment:
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Initialize the database:
python -m backend.init_db
Frontend
Navigate to frontend folder:
cd frontend
Install npm packages:
npm install
Start the frontend:
npm start

The frontend will open at http://localhost:3000 and communicate with the Flask backend running on http://localhost:5000.

Usage
Register a new user or log in with existing credentials
View sales forecasts and product trends on the dashboard
Data visualizations update dynamically from backend API
Technologies
Backend: Python, Flask, Flask-SQLAlchemy, Flask-Cors, SQLite
Frontend: React, Chart.js, react-chartjs-2
Authentication: Werkzueg password hashing
```

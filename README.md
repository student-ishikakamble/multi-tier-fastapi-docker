
FastAPI CRUD Application

This is a backend REST API built using FastAPI. It supports full CRUD operations with a SQLite database and is deployed on Render with live API documentation using Swagger UI.

Live Application Links

API Base URL
https://multi-tier-fastapi-docker-8.onrender.com

Swagger API Documentation
https://multi-tier-fastapi-docker-8.onrender.com/docs

Technology Stack

Python
FastAPI
SQLite
SQLAlchemy
Uvicorn
Render (Deployment Platform)

Features

Create user using POST request
Read user data using GET request
Update user data using PUT request
Delete user data using DELETE request
Interactive API documentation using Swagger UI
Lightweight SQLite database integration
Deployed and accessible via public URL

Project Structure
multi-tier-app/
│
├── backend/                  # FastAPI backend application
│   ├── main.py              # API routes (CRUD endpoints)
│   ├── models.py           # Database models (SQLAlchemy)
│   ├── database.py         # DB connection setup
│   ├── requirements.txt    # Python dependencies
│   └── __init__.py         # Package initializer
│
├── frontend/                # Frontend (if applicable)
│
├── docker-compose.yml      # Multi-container setup
├── Dockerfile              # Container configuration
├── test.db                 # SQLite database file
└── README.md               # Project documentation

How to Run Locally

Step 1: Clone the repository
git clone https://github.com/your-username/fastapi-crud-project.git

Step 2: Navigate to backend folder
cd fastapi-crud-project/backend

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Run the application
uvicorn main:app --reload

Step 5: Open in browser
http://127.0.0.1:8000/docs

API Endpoints

POST /user - Create a new user
GET /user/{id} - Get user by ID
PUT /user/{id} - Update user by ID
DELETE /user/{id} - Delete user by ID

Troubleshooting and Fixes
1. Error: API not loading on local server
Cause:
Missing FastAPI app instance or wrong import structure.

Fix:
Ensure this exists in main.py:
app = FastAPI()

2. Render deployment working but local not working
Cause:
Difference between production and local import paths.

Fix:
Use correct module path based on project structure (backend.main:app)

What I Learned

FastAPI backend development
REST API design principles
CRUD operations
Database integration using SQLite and SQLAlchemy ORM
Debugging import and runtime errors
Deployment on Render
GitHub project structuring
<img width="1446" height="717" alt="image" src="https://github.com/user-attachments/assets/281ca649-04ad-473f-8d16-3f5f8ec6be27" />
<img width="377" height="60" alt="image" src="https://github.com/user-attachments/assets/2a18fc5e-2a42-4e90-b4e7-f228edbd1ee6" />

Author

Your Name
GitHub:



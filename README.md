# 📌 Job Application Tracker (Flask + SQLite)

A secure web-based Job Application Tracker built using **Flask**,
**SQLite**, **HTML**, and **CSS**.

This application allows users to register, login, and manage their job
applications securely.

------------------------------------------------------------------------

## 🚀 Features

-   ✅ User Registration & Login\
-   ✅ Session-based Authentication\
-   ✅ Add Job Applications\
-   ✅ Edit Job Details\
-   ✅ Delete Applications\
-   ✅ User-specific Data (Each user sees only their jobs)\
-   ✅ Clean UI using HTML & CSS\
-   ✅ SQLite Database Integration

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Backend:** Python (Flask)
-   **Frontend:** HTML, CSS
-   **Database:** SQLite
-   **Authentication:** Flask Sessions

------------------------------------------------------------------------

## 📂 Project Structure

    job-tracker/
    │
    ├── app.py
    ├── database.db
    ├── static/
    │   └── style.css
    ├── templates/
    │   ├── index.html
    │   ├── add_job.html
    │   ├── edit_job.html
    │   ├── login.html
    │   └── register.html
    └── README.md

------------------------------------------------------------------------

## 🔐 Authentication Flow

-   Users must register first\
-   Login creates a session using Flask's `session`\
-   Only logged-in users can:
    -   View jobs
    -   Add jobs
    -   Edit jobs
    -   Delete jobs
-   Each job is linked to `user_id`
-   Logout clears session

------------------------------------------------------------------------

## 🗄️ Database Schema

### Users Table

    id INTEGER PRIMARY KEY AUTOINCREMENT
    username TEXT NOT NULL
    password TEXT NOT NULL

### Job Applications Table

    id INTEGER PRIMARY KEY AUTOINCREMENT
    company_name TEXT NOT NULL
    job_role TEXT NOT NULL
    applied_date TEXT NOT NULL
    status TEXT NOT NULL
    user_id INTEGER (Foreign Key)

------------------------------------------------------------------------

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

    https://github.com/satyabharat1207/Job-Application-Tracker.git

### 2️⃣ Install Dependencies

    pip install flask

### 3️⃣ Run Application

    python app.py

### 4️⃣ Open Browser

Visit:

    http://127.0.0.1:5000/

------------------------------------------------------------------------

## 🎯 Learning Outcomes

Through this project, I learned:

-   Flask routing and CRUD operations\
-   Session management\
-   Authentication implementation\
-   SQLite database integration\
-   Backend-Frontend integration

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Password hashing using `werkzeug.security`\
-   REST API conversion\
-   JWT Authentication\
-   Search & Filter functionality\
-   Dashboard Analytics\
-   Deployment on Render / Railway / AWS

------------------------------------------------------------------------

## 👨‍💻 Author

**Satya Bharat**\
Backend Developer \| Python \| Flask \| AI Enthusiast

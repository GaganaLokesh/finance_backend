# Finance Backend System

# Overview

-This project is a backend system for managing financial data with role-based access control. 
-It allows users to create and manage financial records and provides dashboard-level analytics.

# Features

1. 👤 User Management

* Create, update users
* Assign roles (VIEWER, ANALYST, ADMIN)
* Activate / Deactivate users

2. 💰 Financial Records

* Create, view, delete records
* Filter by type and category

3. - 📊 Dashboard

* Total Income
* Total Expense
* Net Balance
* Category-wise summary

4. 🔐 Access Control

* VIEWER → read only
* ANALYST → read only
* ADMIN → full access

# 🛠️ Tech Stack

* Python (Flask)
* MySQL
* SQLAlchemy ORM

#⚙️ Setup Instructions

1. Create virtual environment:
   python -m venv env
   env\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Configure database in config.py

4. Run application:
   python app.py

#📡 API Endpoints

--> User APIs

* POST /users
* GET /users
* GET /users/{id}
* PUT/users/{id}
* PATCH /users/{id}/status

--> Financial APIs

* POST /records?user_id=
* GET /records?user_id=
* DELETE /records/{id}?user_id=
* GET /records/filter?type="EXPENSE"

--> Dashboard API

* GET /dashboard/summary?user_id=

## 🧠 Design Decisions

* Separation of concerns using services and routes
* Role-based access implemented at service layer
* Aggregation logic handled dynamically for dashboard
* Validation and error handling included

# 📌 Assumptions

* Authentication is mocked using user_id
* Roles are predefined
* No frontend included

# ⭐ Future Improvements

* JWT Authentication
* Pagination
* Search functionality
* Unit testing

# 🚀 User Management API

A modern, fast, and efficient user management REST API built with FastAPI.

## ✨ Features

- CRUD operations for user management
- Email validation
- User deactivation functionality
- Input validation and error handling
- Async request handling
- OpenAPI (Swagger) documentation

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://docs.pydantic.dev/) - Data validation using Python type annotations
- [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server

## 🚦 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository

```bash
git clone <repository-url>
cd user-management-api
```

2. Create and activate a virtual environment

```bash
## Create .venv
uv venv
## Activate
source .venv/bin/activate
## INstall
uv pip install -r requirements.txt -r requirements-dev.txt
## Start
bash start.sh
```

### 📚 API Documentation

Once the server is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## 🔍 API Endpoints

- `POST /users/` - Create a new user
- `GET /users/` - List all users
- `GET /users/{user_id}` - Get a specific user
- `PATCH /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Delete a user
- `POST /users/{user_id}/deactivate` - Deactivate a user

## 🧪 Development

### Running Tests
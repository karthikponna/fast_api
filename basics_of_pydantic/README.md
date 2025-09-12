# 🚀 FastAPI Pydantic Basics - User Registration API

This is a FastAPI application that demonstrates the fundamentals of Pydantic data validation in a real-world user registration system. The app showcases essential Pydantic features including field validation, custom validators, email validation, and automatic API documentation generation.

## Features

- **Email Validation:** Validates email addresses using Pydantic's EmailStr type
- **Password Validation:** Enforces password length constraints and custom validation rules
- **Age Validation:** Ensures age is within reasonable bounds (18-100 years)
- **UUID Generation:** Automatically generates unique user IDs using UUID4
- **Custom Validators:** Implements custom field validators to prevent common security issues

## Setup

### Requirements

1. **Python 3.8+:** Ensure you have Python 3.8 or higher installed
2. **Dependencies:** FastAPI, Pydantic, and email-validator

### Installation
1. Clone this repository:
```bash
git clone https://github.com/karthikponna/fast_api.git
cd fast_api/basics_of_pydantic
```

2. Install the required Python packages:
```bash
uv sync
```

### Running the App

1. **Start the FastAPI server:**
```bash
uvicorn main:app --reload
```

### Open your browser and navigate to:
- **API Documentation:** http://localhost:8000/docs (Swagger UI)

## API Endpoints

### POST /users/

Creates a new user with validation.

**Request Body:**

```bash
{
  "email": "user@example.com",
  "password": "mypassword123",
  "age": 25
}
```

**Response (201 Created):**

```bash
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "password": "mypassword123",
  "age": 25
}
```
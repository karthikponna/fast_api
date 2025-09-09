<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

This repository contains practical implementations covering the essential aspects of FastAPI development.

## **📂 Featured Implementations**

*   [FastAPI with Pydantic](basics_of_pydantic)
*   [FastAPI with Pytest](fastapi_pytest)
*   [FastAPI with Jinja2](jinja2)
*   [FastAPI with MongoDB](mongo_db)
*   [FastAPI with MySQL](mysql)
*   [FastAPI with Postgresql](postgresql)
*   [FastAPI with Redis](redis)
*   [FastAPI with SQLAlchemy](sqlalchemy)

## 📚 **Core Concepts**

- **Pydantic Integration**: Data validation, parsing, and serialization
- **Database Connectivity**: Multiple database implementations
- **Template Rendering**: Dynamic HTML generation with Jinja2
- **Testing**: Comprehensive API testing with pytest
- **Modern Python**: Type hints, async/await, and best practices

## 🛠️ **Tech Stack**

- **Framework**: FastAPI
- **Python**: 3.13+
- **Data Validation**: Pydantic 
- **Databases**: 
  - PostgreSQL 
  - MySQL
  - MongoDB
  - SQLite
- **Caching**: Redis
- **Templates**: Jinja2 
- **Testing**: pytest 
- **Server**: Uvicorn 

## **Prerequisites**

- Python 3.13 or higher
- uv package manager 

## **Installation**

1. **Install uv**:
```bash
# For macOS:
brew update
brew install uv

# For Windows - Open PowerShell as Administrator and run the below command:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# For more on installation guide:
👉 https://docs.astral.sh/uv/getting-started/installation/

```

## Local Setup 👨🏼‍💻

1. **Clone the repository**:
```bash
git clone https://github.com/karthikponna/fast_api.git
cd fast_api
uv sync
```


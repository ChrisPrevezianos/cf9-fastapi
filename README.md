# cf9-fastapi

A collection of educational FastAPI projects and examples developed in Python to practice modern API development concepts.

This repository contains chapter-based examples that gradually introduce FastAPI features, request handling, validation, dependency injection, authentication, database integration, and application architecture.

The examples are organized as independent learning modules, with each folder focusing on a specific topic.

---

## Tech Stack

* Python 3.14
* FastAPI
* Pydantic v2
* SQLModel
* SQLAlchemy
* SQLite
* Uvicorn
* HTTPX
* Jinja2
* python-jose
* passlib

---

## Topics Covered

### FastAPI Fundamentals

* Creating API endpoints
* Request and response lifecycle
* Interactive API documentation

### Request Handling

* Path parameters
* Query parameters
* Request body validation
* Response models

### Application Structure

* Dependency injection
* Lifespan events
* Sync vs Async execution

### Database Integration

* SQLModel ORM
* SQLAlchemy integration
* SQLite database usage
* CRUD operations

### Authentication & Security

* JWT creation and validation
* Password hashing with bcrypt
* Authentication building blocks

### Error Handling

* HTTP exceptions
* Custom exception handlers
* JSON error responses

---

## Repository Structure

```text
cf9-fastapi
│
├── examples/
│   ├── 01_getting_started/
│   ├── 02_parameters/
│   ├── 03_request_bodies/
│   ├── 04_responses/
│   ├── 05_errors/
│   ├── 06_dependencies/
│   ├── 07_sync_async/
│   ├── 08_database/
│   └── 09_auth/
│
├── app/
│   ├── config.py
│   ├── db.py
│   ├── routers/
│   ├── schemas/
│   └── models/
│
└── requirements.txt
```

## Note

The `app/` package is included as a structural reference to demonstrate a typical FastAPI application organization.

During the course, implementation concepts were explored primarily through the independent examples located under `examples/`.

Folder responsibilities:

* **examples/** → Educational examples organized by topic
* **app/** → Reference project structure for organizing FastAPI applications
* **routers/** → API endpoint organization
* **schemas/** → Request and response models
* **models/** → Data models
* **db.py** → Database configuration examples
* **config.py** → Application configuration examples

---

## Features

* Multiple standalone FastAPI examples
* Automatic OpenAPI generation
* Swagger UI and ReDoc documentation
* Dependency injection examples
* Database CRUD examples
* JWT demonstration
* Password hashing
* Custom exception handling
* Sync and Async endpoint patterns

---

## API Documentation

FastAPI automatically provides interactive documentation:

```text
Swagger UI → /docs
ReDoc → /redoc
```

Example:

```text
http://127.0.0.1:8000/docs
```

---

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Additional packages for authentication examples (if required):

```bash
pip install python-jose passlib[bcrypt]
```

---

## Run Examples

Navigate to an example folder:

```bash
cd examples/08_database
```

Start FastAPI:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Educational Purpose

This repository was created for practice and learning in:

* FastAPI
* REST API design
* Dependency Injection
* Pydantic validation
* SQLModel and SQLAlchemy
* Authentication fundamentals
* Error handling
* FastAPI project organization

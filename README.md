# Inventory Management System

A full-stack Inventory Management System built with FastAPI (backend) and React (frontend).

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy
- **Frontend:** React, JavaScript, CSS
- **Database:** PostgreSQL

## Features

- Add, view, update and delete products
- Product details: name, description, price, quantity
- REST API with FastAPI
- React frontend interface

## Project Structure

FAST_API/
├── main.py
├── models.py
├── database.py
├── database_models.py
├── frontend/
│   └── src/
│       ├── App.js
│       ├── App.css
│       └── ...


## Getting Started

### Backend
```bash
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## API Docs
Once the server is running, visit:
`http://127.0.0.1:8000/docs`

##  Note
Backend is fully developed using FastAPI. Frontend is built using React and integrated with the backend APIs.

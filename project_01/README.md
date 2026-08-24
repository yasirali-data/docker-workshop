# 🌆 Smart City AQI API

A simple **FastAPI-based Smart City API** built and containerized using Docker.

## 🛠️ Technologies

- Python 3.11
- FastAPI
- Uvicorn
- Docker
- Docker Compose

## 🚀 Run the Project

```bash
docker compose up --build

The API will run on:
http://localhost:8000

🔍 Health Check
GET /health

Test it with:
curl http://localhost:8000/health

📖 API Documentation
FastAPI Swagger UI:
http://localhost:8000/docs

📁 Structure
project_01/
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

👨‍💻 Author
Yasir Ali

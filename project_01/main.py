from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Smart City AQI API")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Smart City AQI API",
        "timestamp": datetime.utcnow().isoformat()
    }
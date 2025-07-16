from fastapi import FastAPI
from backend.logging_config import setup_logger
from loguru import logger

setup_logger()

app = FastAPI()

@app.get("/health")
def health_check():
    logger.info("Health check endpoint was hit.")
    return {"status": "ok"}
  
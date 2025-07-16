from fastapi import FastAPI
from backend.logging_config import setup_logger
from backend.api.routes import router as planner_router
from loguru import logger

setup_logger()

app = FastAPI(title="AutoDevX API", version="0.1")

app.include_router(planner_router, prefix="/planner", tags=["PlannerAgent"])

@app.get("/health")
def health_check():
    logger.info("Health check endpoint was hit.")
    return {"status": "ok"}
  
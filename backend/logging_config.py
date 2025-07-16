from loguru import logger
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logger.add(
        "logs/autodevx.log",
        rotation="1 MB",
        retention="10 days",
        compression="zip",
        enqueue=True,
        backtrace=True,
        diagnose=True,
        level="INFO"
    )

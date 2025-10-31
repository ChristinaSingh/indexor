from loguru import logger
import os

os.makedirs("logs", exist_ok=True)
# simple local log file with rotation
logger.add("logs/agent.log", rotation="1 MB", enqueue=True, level="INFO")

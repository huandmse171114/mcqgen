import logging
import os
from datetime import datetime

# Create log file name
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), "logs") #cwd: current working directory

# Create logs directory
os.makedirs(log_path, exist_ok=True)

# Create log file path inside logs directory
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    level = logging.INFO,
    filename = LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)



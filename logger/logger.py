import logging
from logging.handlers import TimedRotatingFileHandler
import os

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_DIR = "/Users/qrios/Desktop/Final_exam_altschool/Final_exam/Logs/"
LOG_FILENAME = "hospital.log"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(filename=os.path.join(LOG_DIR, LOG_FILENAME), when="midnight", backupCount=7)
handler.setFormatter(logging.Formatter(LOG_FORMAT))

logger.addHandler(handler)

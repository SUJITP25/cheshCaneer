import logging 
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root 
from datetime import datetime 


LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
MAX_LOG_SIZE =5 * 1024 * 1024
BACKUP_COUNT = 3 

log_dir_path= os.path.join(from_root(),LOG_DIR)
os.makedirs(log_dir_path,exist_ok=True)
log_file_path=os.path.join(log_dir_path,LOG_FILE)


def configure_logger(): 
    logger = logging.getLogger()
    logger.setLevel("DEBUG")


    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")

    file_handler = RotatingFileHandler(log_file_path,backupCount=BACKUP_COUNT,maxBytes=MAX_LOG_SIZE)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)


    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)


    logger.addHandler(console_handler)
    logger.addHandler(console_handler)


configure_logger()





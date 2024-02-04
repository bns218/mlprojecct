import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.logs_path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok==True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filenade=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineni)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO


)

if __name__=="__main__":
    logging.info("Logging has started")
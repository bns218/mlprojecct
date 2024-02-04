import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
<<<<<<< HEAD
logs_path = os.logs_path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok==True)
=======
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
>>>>>>> a9b94a26ee951cb1ba00f8e77dc00e1f4d64f3f4

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
<<<<<<< HEAD
    filenade=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineni)d %(name)s - %(levelname)s - %(message)s",
=======
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
>>>>>>> a9b94a26ee951cb1ba00f8e77dc00e1f4d64f3f4
    level=logging.INFO


)

<<<<<<< HEAD
if __name__=="__main__":
    logging.info("Logging has started")
=======
>>>>>>> a9b94a26ee951cb1ba00f8e77dc00e1f4d64f3f4

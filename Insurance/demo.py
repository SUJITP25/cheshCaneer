# from src.logger import logging 
# logging.debug("This is DEBUG Message")
# logging.info("This is info message")
# logging.warning("This is Warning Message")
# logging.error("This is Error Message")
# logging.critical("This is Critical Message")


from src.logger import logging 
from src.exception import MyException 
import sys 


try: 
    a = 1 + "z"
except Exception as e: 
    logging.info(e)
    raise MyException(e,sys) from e
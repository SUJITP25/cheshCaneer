import dill 
import yaml 
import os
import sys
from pandas import DataFrame 
from src.exception import MyException 
from src.logger import logging 
import numpy as np

def read_yaml_file(filepath): 
    try: 
        with open(filepath,"rb") as yaml_file: 
            return yaml.safe_load(yaml_file) 
    except Exception as e:
        raise MyException(e,sys) from e 
    

def write_yaml_file(filepath,content,replace): 
    try: 
        if replace: 
            if os.file.exists(filepath): 
                os.remove(filepath)
        os.makedirs(filepath,exist_ok=True)
        with open(filepath, "w") as file: 
            yaml.dump(content,file)
    except Exception as e: 
        raise MyException(e,sys) from e 
    
# load object is basically used for loadig model
def load_object(filepath): 
    try: 
        with open(filepath , "rb") as file_obj: 
            obj = dill.load(file_obj)
        return obj
    except Exception as e: 
        raise MyException(e,sys) from e
    

def save_numpy_array_data(file_path,array): 
    try: 
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open (file_path) as file_obj:
            np.save(file_obj,array) 
    except Exception as e: 
        raise MyException(e,sys) from e
    

def load_numpy_array_data(filepath): 
    try: 
        with open(filepath,"rb") as file_obj: 
            return np.load(file_obj)
    except Exception as e: 
        raise MyException(e,sys) from e
    

def save_object(filepath,obj): 
    try: 
        logging.info("Enteringh the Objectg saving method of utils.py")
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath, "rb") as file_obj: 
            dill.dump(obj,file_obj)
        logging.info("Existed the Save object Method of the Object saving")
    except Exception as e: 
        raise MyException(e,sys) from e
import os 
import sys 

import numpy as np 
import dill 
import yaml 
from pandas import DataFrame 

from mlops.exception import MLOpsException 
from mlops.logger import logging 



def read_yaml_file(filepath): 
    try: 
        with open(filepath,"rb") as yaml_file: 
            return yaml.safe_load(yaml_file)
    except Exception as e: 
        raise MLOpsException(e,sys) from e
    

def write_yaml_file(filepath,content,replace): 
    try: 
        if replace: 
            if os.path.exists(filepath): 
                os.remove(filepath)
            os.makedirs(os.path.dirname(filepath),exist_ok=True)
            with open(filepath,"w") as file:
                yaml.dump(content,file)
    except Exception as e: 
        raise MLOpsException(e.sys) from e
    

    
    
def load_object(filepath): 
    try: 
        logging.info("Starting the Process of Loading Data from Model")
        with open(filepath, "rb") as file: 
            obj = dill.load(file)
            logging.info("Data loaded Successdfully")
            return obj
    except Exception as e: 
        raise MLOpsException(e,sys) from e



def save_numpy_arary(filepath,array): 
    try: 
        file_dir = os.path.dirname(filepath)
        os.makedirs(file_dir,exist_ok=True)
        with open(filepath,"wb") as file: 
            np.save(file,array)
    except Exception as e: 
        raise MLOpsException(e,sys) from e
    

def load_data_from_numpy_array(filepath):
    try: 
       with open(filepath, "rb") as file: 
           return np.load(file)     
    except Exception as e: 
        raise MLOpsException(e,sys) from e 
    

def save_object(filepath,object): 
    try: 
        logging.info("Enter the save Object")
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath,"wb") as file: 
            dill.dump(object,filepath)
    except Exception as e: 
        raise MLOpsException(e,sys) from e  
    

def drop_columns(df,cols): 
    try: 
        df = df.drop(columns=cols,axis=1)
        return df
    except Exception as e: 
        raise MLOpsException(e,sys) from e
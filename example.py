import os 
import warnings 
import sys 
import pandas as pd 
import numpy as np 
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import ElasticNet 
from urllib.parse import urlparse 
import mlflow 
from mlflow.models.signature import infer_signature 
import mlflow.sklearn 
import logging 

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def eval_metrics(actual,predict): 
    rmse = np.sqrt(mean_squared_error(actual,predict))
    mae = mean_absolute_error(actual,predict)
    r2 = r2_score(actual,predict)
    return rmse,mae,r2

if __name__ =="__main__": 
    warnings.filterwarnings("ignore")
    np.random.seed(42)


    csv_url =""
    try: 
       data= pd.read_csv(csv_url,sep=";")
    except FileNotFoundError as e: 
       logging.error("Error While loading the File")

    train,test = train_test_split(data)

    
    # Write the Whole flow like this 



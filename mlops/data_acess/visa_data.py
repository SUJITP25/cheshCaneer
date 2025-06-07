from mlops.configuration.mongo_db_connection import MongoDBClient  
from mlops.constants import DB_NAME
from mlops.exception import MLOpsException 
import pandas as pd 
import os 
import sys 
from typing import Optional 
import numpy as np  



class UsVisaData: 
    def __init__(self): 
        try: 
            self.mongo_client = MongoDBClient(database_name=DB_NAME)
        except Exception as e: 
            raise MLOpsException(e,sys) from e 
    
    def export_connection_as_dataframe(self,collection_name,database_name): 
        try: 
            if database_name is None: 
                collection = self.mongo_client.database[collection_name]
            else: 
                self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list(): 
                df = df.drop(columns=["_id"],axis=1)
            df.replace("na":np.nan,inplace=True)
            return df 
        except Exception as e: 
            raise MLOpsException (e,sys) from e 
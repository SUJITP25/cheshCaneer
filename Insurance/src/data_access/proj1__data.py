import sys 
import pandas as pd 
import numpy as np 
from typing import Optional 

from src.configuration.mongo_db_connection import MongoDBClient 
from src.constants import DATABASE_NAME 
from src.exception import MyException 


class Proj1Data: 
    def __init__(self): 
        try: 
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e: 
            raise MyException(e,sys)
        
    def export_collection(self,collection_name,database_name): 
        try: 
            if database_name is None: 
                collection = self.mongo_client.database[collection_name]
            else: 
                collection = self.mongo_client[database_name][collection_name]
            
            print("fetching Data Succcessfuklly")
            df = pd.DataFrame(list(collection_name.find()))
            print(f"data fetched with length : {len(df)}")
            if "id" in df.columns.to_list(): 
                df= df.drop(columns=["id"],axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e: 
            raise MyException(e,sys)
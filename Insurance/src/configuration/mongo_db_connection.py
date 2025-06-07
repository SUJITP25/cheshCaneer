import os 
import certifi 
import pymongo 
import sys


from src.exception import MyException 
from src.logger import logging 
from src.constants import DATABASE_NAME,MONGODB_URL_KEY


# load certificate authority file to avoid the timeout error when connecting to mongoDB 

ca = certifi.where() 

class MongoDBClient: 
    def __init__(self,database_name = DATABASE_NAME):
        try: 
            if MongoDBClient.client is None: 
                # get the database url from the environment file
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None: 
                    raise Exception(f"Environmaent Variable", {MONGODB_URL_KEY} is not set) 
                #Establish Connection Between MongoDB Client 
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlfCaFile=ca)
            self.client = MongoDBClient.client 
            self.database = self.client[database_name]
            self.database_name = self.database
            logging.info("MongoDB Connection Successful")
        except Exception as e: 
            print(f'{logging.error},',e)
            raise MyException(e,sys) 
        
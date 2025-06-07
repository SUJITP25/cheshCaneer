import os 
from mlops.exception import MLOpsException 
from mlops.logger import logging 
import certifi 
import os 
import sys
import pymongo 
from mlops.constants import DB_NAME,CONNECTION_URL,COLLECTION_NAME


ca = certifi.where()

class MongoDBClient: 
    client = None 
    def __init__(self,database_name=DB_NAME):
        try:
            if MongoDBClient.client is None: 
                mongo_db_url = os.getenv(CONNECTION_URL)
                if mongo_db_url is None: 
                    raise Exception (f"Environment Ley: {CONNECTION_URL} is not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFILE=ca) 
            self.client = MongoDBClient.client 
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info('Conenction Sucecssful') 
        except Exception as e: 
            raise MLOpsException(e,sys) from e
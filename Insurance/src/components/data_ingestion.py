import os 
import sys 
from pandas import DataFrame 
from sklearn.model_selection import train_test_split 
from src.entity.config_entity import DataIngestionConfig 
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception import MyException 
from src.logger import logging 
from src.data_access.proj1__data import Proj1Data 


class DataIngestion: 
    def __init__(self,data_ingestion_config):
        try: 
            self.data_ingestion_config = data_ingestion_config
        except Exception as e: 
            raise MyException(e,sys)
        
    def export_data_info_feature_store(self): 
        try: 
            logging.info(f'Exporting Data from MongoDB')
            my_data = Proj1Data()
            dataFrame = my_data.export_collection(collection_name=self.data_ingestion_config.collection_name) 
            logging.info(f"Shape of DataFrame : {dataFrame.shape}")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path 
            dir_path =os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into featuyre store in filepath {feature_store_file_path}")
            dataFrame.to_csv(feature_store_file_path,index=False,header=True)
            return dataFrame
        except Exception as e: 
            raise MyException(e,sys)
        
    
    def train_test_split(self,dataFrame): 
        logging.info(f"Entering into the proecess of the train_test_split")
        try: 
            train_set,test_set = train_test_split(dataFrame,self.data_ingestion_config.train_test_split_ratio)
            logging.info("performed Train_test_split on Data Frame")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info("Exporting Train and test file Path")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
            logging.info("Exported Data into Train amd test Split")
        except Exception as e: 
            raise MyException(e,sys) 
        

    def intialize_data_ingestion(self): 
        try: 
            dataFrame = self.export_data_info_feature_store()
            logging.info("Got the Data From Mongodb")
            self.train_test_split(dataFrame)
            logging.info("Performed Train_test_split")
            data_ingestion_artifact= DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,test_file_path=self.data_ingestion_config.testing_file_path)
            logging.info(f"Data ingestion artifact : {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e: 
            raise MyException(e,sys)
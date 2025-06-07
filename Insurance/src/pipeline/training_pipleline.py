import os 
import sys
from src.logger import logging 
from src.exception import MyException 
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation

from src.entity.config_entity import DataIngestionConfig,DataValidationConfig
from src.entity.artifact_entity import DataIngestionArtifact ,DataValidationArtifact


class TrainPipeline: 
    def __init__(self): 
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_cofig = DataValidationConfig()


    def start_data_ingestion(self):
        try: 
            logging.info("Enter the start data ingestion methid")
            logging.info("Getting Data From MongoDB")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.intialize_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e,sys) from e 
    

    def start_data_validation(self,data_ingestion_artifest)):
        try: 
            logging.info("Starting Data Validation Method")
            data_validation = DataValidation(data_ingestion_artifest,data_validation_config=self.data_validation_cofig)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Perform Data validation Method")
            return data_validation_artifact
        except Exception as e: 
            raise MyException(e,sys) from e

    def run_pipeline(self): 
        try: 
            data_ingestion_artifest = self.start_data_ingestion()
            data_validation_artifest = self.start_data_validation(data_ingestion_artifest=data_ingestion_artifest)
           
        except Exception as e: 
            raise MyException(e,sys) from e
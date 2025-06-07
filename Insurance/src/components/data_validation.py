import json 
import sys 
import os  

import pandas as pd 
from pandas import DataFrame 
from src.exception import MyException 
from src.logger import logging 
from src.utils.main_utils import read_yaml_file,write_yaml_file  
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact 
from src.entity.config_entity import DataValidationConfig 
from src.constants import SCHEMA_FILE_PATH 


class DataValidation: 
    def __init__(self,data_ingestion_artifest,data_validation_config): 
        try: 
            self.data_ingestion_artifest = data_ingestion_artifest 
            self.data_validation_config = data_validation_config 
            self.schema_config = read_yaml_file(filepath=SCHEMA_FILE_PATH)
        except Exception as e: 
            raise MyException(e,sys) from e
        
    def validate_number_of_columns(self,dataFrame): 
        try: 
            logging.info('Checking Status for Number of Columns in DataFrame')
            status = len(dataFrame.columns) == len(self.schema_config["columns"])
            logging.info(f"Is required Columns are Present : {status}")
            return status
        except Exception as e: 
            raise MyException(e,sys) from e
        
    def is_column_present(self,dataFrame): 
        try:   
            missing_numerical_columns = []
            missing_categorical_columns = []
            for column in self.schema_config["numerical_columns"]: 
                if column not in dataFrame.columns: 
                    missing_numerical_columns.append(column)
            
            if len(missing_numerical_columns) > 0: 
                logging.info(f"Missing Numerical Columns {missing_numerical_columns}")

            for column in self.schema_config["categorical_columns"]: 
                if column not in dataFrame.columns: 
                    missing_categorical_columns.append(column)

            if len(missing_categorical_columns) > 0: 
                logging.info(f'Missimng Categoical Columns {missing_categorical_columns}')

            return False if len(missing_categorical_columns)> 0 or len(missing_numerical_columns)> 0 else True
        except Exception as e: 
            raise MyException(e,sys) from e
        
    
    @staticmethod 
    def read_data(filepath): 
        try: 
            return pd.read_csv(filepath)
        except Exception as e: 
            raise MyException(e,sys)
        

    
    def initiate_data_validation(self): 
        try:
            validation_error_msg =""
            logging.info("Starting Validation Method")
            train_df,test_df = (DataValidation.read_data(filepath=self.data_ingestion_artifest.trained_file_path),DataValidation.read_data(filepath=self.data_ingestion_artifest.test_file_path))

            status = self.validate_number_of_columns(dataFrame=train_df)
            if not status: 
                validation_error_msg = "Columns are missing in Training dataFrame"
            else: 
                logging.info("All Coumns are present in Training Dataframe")
            
            status = self.validate_number_of_columns(dataFrame=test_df)
            if not status: 
                validation_error_msg = "Coluns are missing in test DataFrame"
            else: 
                logging.info("All Columns are present in test DataFrame")

            # validating col dtype 

            status = self.is_column_present(dataFrame=train_df)
            if not status: 
                validation_error_msg = "Coluns are missing in Training DataFrame"
            else: 
                logging.info("All Columns are present in Training DataFrame")


            status = self.is_column_present(dataFrame=test_df)
            if not status: 
                validation_error_msg = "Coluns are missing in Testing DataFrame"
            else: 
                logging.info("All Columns are present in Testing DataFrame")
            
            
            validation_status = len(validation_error_msg) == 0 

            data_validation_artifact = DataIngestionArtifact(
                validation_status = validation_status, 
                message = validation_error_msg, 
                validation_report_file_path = self.data_validation_config.validation_report_file_path
            )

            # Ensure that the directory of the validation_report_file_path exists 

            report_dir = os.path.dirname(self.data_validation_config.validation_report_file_path)

            os.makedirs(report_dir,exist_ok=True)
            

            # save Validation report 
            validation_report = {
                "validation_status": validation_status, 
                "message" : validation_error_msg.strip()
            }


            with open(self.data_validation_config.validation_report_file_path, "w") as report_file: 
                json.dump(validation_report,report_file,indent=4)

            logging.info("Data Validation artifact created and saved top JSON File")

            return data_validation_artifact


            
        except Exception as e:
            raise MyException(e,sys)

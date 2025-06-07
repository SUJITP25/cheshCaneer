import os 
from datetime import date

# Common Constants

DB_NAME="visa"
COLLECTION_NAME="visa_data"
CONNECTION_URL="database_url"

PIPELINE_NAME="visa"
ARTIFACT_DIR ="artifact"
MODEL_FILE_PATH="model.pkl"
FILE_NAME = "EasyVisa.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME ="test.csv"

# DataIngestions Constants 
DATA_INGESTION_COLLECTION_NAME = "visa_data"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2
from housing.entity.config_entity import DataIngestionConfig
import os, sys
from housing.logger import logging
from housing.exception import Housing_Exception

class DataIngestion :
    def __init__(self, data_ingestion_config:DataIngestionConfig):

        try :
            logging.info(f"{'='*20}Data Ingestion log started. {'='*20}")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e :
            raise Housing_Exception(e, sys) from e
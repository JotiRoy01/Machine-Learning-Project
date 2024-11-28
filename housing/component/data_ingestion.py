from housing.entity.config_entity import DataIngestionConfig
import os, sys
from housing.logger import logging
from housing.exception import Housing_Exception
import tarfile
from six.moves import urllib

class DataIngestion :
    def __init__(self, data_ingestion_config:DataIngestionConfig):

        try :
            logging.info(f"{'='*20}Data Ingestion log started. {'='*20}")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e :
            raise Housing_Exception(e, sys) from e
        
    def download_housing_data(self) :
        try :
            #Extraction remote url to dowload dataset
            dowload_url = self.data_ingestion_config.dataset_download_url
            # Folder location to dowload file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
        except 
    
    def extract_tgz_file(self) :
        pass

    def split_data_as_train_test(self) :
        pass

    def initiate_data_ingestion(self) -> DataIngestionArtifact :
        try :
            pass
        except Exception as e :
            raise Housing_Exception(e, sys) from e
        
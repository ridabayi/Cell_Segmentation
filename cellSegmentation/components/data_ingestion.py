import os
import sys
import zipfile
import gdown
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.entity.config_entity import DataIngestionConfig
from cellSegmentation.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig)
        try: self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppException(e, sys)
        

    def donwload_data(self) -> str:
        '''
        Download the dataset from Google Drive and extract it to the specified directory.
        '''
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.mkdir(zip_download_dir, exist_ok=True)
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.indo(f'Dowloading data from {dataset_url} into file {zip_file_path}')


            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_file_path)
            logging.info(f'Data downloaded successfully into {zip_file_path}')
            return zip_file_path
        
        except Exception as e:
            raise AppException(e, sys)
        
    
    def extract_zip_file(self, zip_file_path: str) -> str:
        '''
        Extract the zip file to the specified directory.
        '''
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.mkdir(feature_store_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)
            logging.info(f'Extracted zip file {zip_file_path} into {feature_store_path}')
            return feature_store_path
        
        except Exception as e:
            raise AppException(e, sys)
        

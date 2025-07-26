import os
import sys
from src.exception import CustomException
from src.logging import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str=os.path.join("raw file", "data.csv")

@dataclass    
class DataIngestionArtifact:
    raw_data_path: str=os.path.join("raw file", "data.csv")
    train_data_path: str=os.path.join("artifacts", "train.csv")
    test_data_path: str=os.path.join("artifacts", "test.csv")
    validation_data_path: str=os.path.join("artifacts", "validation.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        self.artifact_config=DataIngestionArtifact()
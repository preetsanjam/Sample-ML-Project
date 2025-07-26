from src.logging import logger
from src.exception.exception import ProjectException
import sys

from src.components.dataingestion import DataIngestion
from src.components.dataingestion import DataIngestionArtifact
from src.components.dataingestion import DataIngestionConfig

# Executing all funcationalities 
if __name__=="__name__":
    
    # Initializing Data Ingestion
    data_ingestion=DataIngestion()
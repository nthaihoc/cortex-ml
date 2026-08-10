import os
from abc import ABC, abstractmethod
import pandas as pd
from typing import Dict, Any
from loguru import logger

from cortexml.application.splitters.base import BaseSplitter
from cortexml.application.storage.metadata import MetadataStorage

class BaseDatasetParser(ABC):
    """
    Abstract Base Parser defining the extraction interface.
    """
    @abstractmethod
    def extract(self) -> pd.DataFrame:
        """
        Extracts raw data into a structured pandas DataFrame.
        
        Concrete implementations should define and document their specific Data Contract 
        (e.g., expected columns). While a standard image classification parser might 
        return ['filepath', 'label', 'split'], subclasses dealing with other data types 
        can freely define or extend these fields as needed.
        """
        pass

class PipelineBaseParser(BaseDatasetParser):
    """
    Template Method pattern for dataset parsing.
    Defines the standard linear workflow.
    """
    def __init__(self, data_path: str, splitter: BaseSplitter, storage: MetadataStorage):
        # By the time this is called, data_path has already been validated and extracted
        # by the orchestrator. It represents the extracted dataset root.
        self.data_path = os.path.abspath(data_path)
        self.splitter = splitter
        self.storage = storage
        self.extracted_path = self.data_path

    def run_pipeline(self, output_dir: str = None) -> Dict[str, Any]:
        """
        The Template Method defining the exact linear flow.
        """
        df = self.extract()
        df_split = self.splitter.split(df)
        
        if output_dir is None:
            output_dir = self.extracted_path
            logger.warning(f"Output directory not specified, saving metadata to default: {output_dir}")
            
        stats = self.storage.save(df_split, output_dir)
        
        return stats
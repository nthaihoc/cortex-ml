from typing import Any

from cortexml.application.parsers import StructureScanner, ParserDispatcher
from cortexml.application.storage import MetadataStorage
from cortexml.application.splitters import SplitterDispatcher
from cortexml.utils import extract_archive

class DataIngestionPipeline:
    """
    Pipeline for ingesting, validating, and splitting datasets.
    """
    def __init__(
        self,
        data_path: str, 
        output_dir: str | None = None, 
        split_type: str = "random", 
        split_ratios: dict[str, float] | None = None
    ) -> None:
        self.data_path = data_path
        self.output_dir = output_dir
        self.split_type = split_type
        self.split_ratios = split_ratios

    def run(self) -> dict[str, Any]:
        """
        Executes the data ingestion pipeline.
        """
        # Step 0: Validate and Extract
        extracted_path = extract_archive(self.data_path, self.output_dir)
        
        # Step 1: Detect pattern
        pattern = StructureScanner.detect(extracted_path)
        
        # Step 2: Initialize Splitter and Storage
        splitter = (SplitterDispatcher.build()
                    .register_random()
                    .register_stratified()
                    .register_keep()
                    .get_splitter(self.split_type, self.split_ratios))
        storage = MetadataStorage()
        
        # Step 3: Get Parser from Factory
        parser = (ParserDispatcher.build()
                  .register_flat_classes()
                  .register_partitioned_classes()
                  .get_parser(pattern, extracted_path, splitter, storage))
        
        # Step 4: Run the pipeline
        stats = parser.run_pipeline(output_dir=self.output_dir)
        
        return stats

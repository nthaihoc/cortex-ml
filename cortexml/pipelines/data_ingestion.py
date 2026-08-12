from typing import Any

from cortexml.application.parsers import StructureScanner, ParserDispatcher
from cortexml.application.storage import MetadataStorage
from cortexml.application.splitters import SplitterDispatcher
from cortexml.utils import extract_archive

class DataIngestionPipeline:
    """Pipeline for ingesting, validating, and splitting datasets.
    
    This pipeline acts as the orchestrator for the entire data ingestion flow,
    coordinating between extractors, splitters, and storage components.
    
    Args:
        data_path: Path to the raw dataset (archive or directory).
        output_dir: Directory to save the extracted data and metadata. Defaults to None.
        split_type: The strategy used for splitting data ('random', 'stratified', 'keep').
        split_ratios: Dictionary defining train/val/test split ratios. Defaults to None.
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
        """Executes the data ingestion pipeline.
        
        Returns:
            A dictionary containing ingestion statistics (e.g., total_samples, splits, labels).
        """

        extracted_path = extract_archive(self.data_path, self.output_dir)
        

        pattern = StructureScanner.detect(extracted_path)
        

        splitter = (SplitterDispatcher.build()
                    .register_random()
                    .register_stratified()
                    .register_keep()
                    .get_splitter(self.split_type, self.split_ratios))
        storage = MetadataStorage()
        

        parser = (ParserDispatcher.build()
                  .register_flat_classes()
                  .register_partitioned_classes()
                  .get_parser(pattern, extracted_path, splitter, storage))
        

        stats = parser.run_pipeline(output_dir=self.output_dir)
        
        return stats

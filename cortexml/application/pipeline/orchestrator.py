from typing import Dict, Any, Optional

from cortexml.application.pipeline.detector import StructureScanner
from cortexml.application.storage.metadata import MetadataStorage
from cortexml.application.parsers.factory import ParserDispatcher
from cortexml.application.splitters.dispatcher import SplitterDispatcher
from cortexml.utils import extract_archive

def main(
    data_path: str, 
    output_dir: str, 
    split_type: str = "random", 
    split_ratios: Optional[Dict[str, float]] = None
) -> Dict[str, Any]:
    """
    Entrypoint for the Data Ingestion Module.
    """
    # Step 0: Validate and Extract
    extracted_path = extract_archive(data_path, output_dir)
    
    # Step 1: Detect pattern
    pattern = StructureScanner.detect(extracted_path)
    
    # Step 2: Initialize Splitter and Storage
    splitter = (SplitterDispatcher.build()
                .register_random()
                .register_stratified()
                .register_keep()
                .get_splitter(split_type, split_ratios))
    storage = MetadataStorage()
    
    # Step 3: Get Parser from Factory
    parser = (ParserDispatcher.build()
              .register_flat_classes()
              .register_partitioned_classes()
              .get_parser(pattern, extracted_path, splitter, storage))
    
    # Step 4: Run the pipeline
    stats = parser.run_pipeline(output_dir=output_dir)
    
    return stats

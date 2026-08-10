from dateutil import relativedelta
import os
from pathlib import Path
import pandas as pd
from typing import List, Optional, Generator
from loguru import logger

from cortexml.application.parsers import PipelineBaseParser
from cortexml.exceptions import DatasetStructureError, InvalidInputPathError
from cortexml.utils import get_valid_dirs, get_valid_files

class ImageBaseParser(PipelineBaseParser):
    """
    Base parser for images that provides common validation and initialization logic.
    """
    def __init__(self, data_path: str, splitter, storage, valid_extensions: Optional[tuple] = None) -> None:
        super().__init__(data_path, splitter, storage)
        self.valid_extensions = valid_extensions or ('.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tif', '.tiff')

class ImageFlatClassesParser(ImageBaseParser):
    """
    Parser for flat_classes: root/class_name/file.ext
    Defaults split to 'unassigned'.
    """
    def extract(self) -> pd.DataFrame:
        data: List[dict] = []
        root_path = Path(self.extracted_path).resolve()
        
        for class_dir in get_valid_dirs(root_path, "class label"):
            for file_path in get_valid_files(class_dir, valid_extensions=self.valid_extensions, check_size=True):
                data.append({
                    'filepath': str(file_path.relative_to(root_path.parent)),
                    'label': class_dir.name,
                    'split': 'unassigned'
                })
                        
        if not data:
            raise DatasetStructureError(f"No valid files found matching flat_classes in {root_path}")
            
        return pd.DataFrame(data, columns=['filepath', 'label', 'split'])

class ImagePartitionedClassesParser(ImageBaseParser):
    """
    Parser for partitioned_classes: root/split_name/class_name/file.ext
    Takes split from the top-level directory name.
    """
    def extract(self) -> pd.DataFrame:
        data: List[dict] = []
        root_path = Path(self.extracted_path).resolve()
        
        for split_dir in get_valid_dirs(root_path, "split"):
            for class_dir in get_valid_dirs(split_dir, "class label"):
                for file_path in get_valid_files(class_dir, valid_extensions=self.valid_extensions, check_size=True):
                    data.append({
                        'filepath': str(file_path.relative_to(root_path.parent)),
                        'label': class_dir.name,
                        'split': split_dir.name
                    })
                                
        if not data:
            raise DatasetStructureError(f"No valid files found matching partitioned_classes in {root_path}")
            
        return pd.DataFrame(data, columns=['filepath', 'label', 'split'])
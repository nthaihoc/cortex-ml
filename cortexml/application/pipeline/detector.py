import os
from pathlib import Path
from cortexml.exceptions import DatasetStructureError

class StructureScanner:
    """
    Scanner to detect the directory structure pattern.
    """
    
    @staticmethod
    def detect(data_path: str) -> str:
        """
        Scans the directory and returns the pattern type.
        PATTERN_A: root/class_1/img.jpg (depth=2)
        PATTERN_B: root/train/class_1/img.jpg (depth=3)
        PATTERN_C: Everything else.
        """
        root_path = Path(data_path).resolve()
        
        if not root_path.is_dir():
            raise DatasetStructureError(f"Data path is not a directory: {data_path}")

        # Find the first valid file to determine the depth
        first_file = None
        for root, dirs, files in os.walk(root_path):
            # Skip hidden directories so we don't traverse them
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for f in files:
                if not f.startswith('.'):
                    file_path = Path(root) / f
                    # Skip empty files to align with parser validation
                    if file_path.stat().st_size > 0:
                        first_file = file_path
                        break
            if first_file:
                break
        
        if not first_file:
            raise DatasetStructureError(f"No valid files found in {data_path}")
            
        # calculate depth relative to root_path
        # example: first_file = root/class_1/img.jpg, relative_parts = ('class_1', 'img.jpg'), len = 2
        depth = len(first_file.relative_to(root_path).parts)
        
        if depth == 2:
            return "flat_classes"
        elif depth == 3:
            return "partitioned_classes"
        else:
            raise DatasetStructureError(f"unsupported_depth: Unsupported structure with depth {depth}")

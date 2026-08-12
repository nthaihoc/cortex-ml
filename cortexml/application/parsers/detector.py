from pathlib import Path
from typing import Generator
from collections import Counter
from cortexml.exceptions import DatasetStructureError
from cortexml.utils import get_valid_dirs, get_valid_files

class StructureScanner:
    """Scanner to detect the directory structure pattern robustly."""
    
    @staticmethod
    def detect(data_path: str, valid_extensions: list | tuple | None = None, sample_size: int = 3) -> str:
        """Scans the directory and returns the pattern type.
        
        Args:
            data_path: Path to the dataset directory.
            valid_extensions: A list or tuple of valid file extensions (e.g., ['.jpg', '.png']). Defaults to None.
            sample_size: Number of files to sample for cross-validating the hierarchy depth. Defaults to 3.

        Returns:
            A string representing the detected pattern type ('flat_classes' or 'partitioned_classes').
            
        Raises:
            DatasetStructureError: If the structure is inconsistent or unsupported.
        """
        root_path = Path(data_path).resolve()
        
        if not root_path.is_dir():
            raise DatasetStructureError(f"Data path is not a directory: {data_path}")

        _exts_tuple = tuple(valid_extensions) if valid_extensions else None

        def _yield_valid_files(current_dir: Path) -> Generator[Path, None, None]:
            for file_path in get_valid_files(current_dir, valid_extensions=_exts_tuple, check_size=True):
                yield file_path
                
            for sub_dir in get_valid_dirs(current_dir):
                yield from _yield_valid_files(sub_dir)

        sampled_files = []
        scanner = _yield_valid_files(root_path)
        
        try:
            for _ in range(sample_size):
                sampled_files.append(next(scanner))
        except StopIteration:
            pass

        if not sampled_files:
            raise DatasetStructureError(f"No valid data files found in {data_path} with extensions {valid_extensions}")
            
        depths = [len(f.relative_to(root_path).parts) for f in sampled_files]
        
        if len(set(depths)) > 1:
            depth_counts = Counter(depths)
            raise DatasetStructureError(
                f"Inconsistent dataset structure detected. Found conflicting depths: {dict(depth_counts)}. "
                f"Please ensure all data files are placed at the same directory level."
            )
            
        standard_depth = depths[0]
        
        if standard_depth == 2:
            return "flat_classes"
        elif standard_depth == 3:
            return "partitioned_classes"
        else:
            raise DatasetStructureError(f"Unsupported structure with depth {standard_depth}")

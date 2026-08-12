import os
import zipfile
import tarfile
from pathlib import Path
from typing import Generator, Optional
from loguru import logger

from cortexml.exceptions import InvalidInputPathError

def extract_archive(data_path: str, output_dir: str | None = None) -> str:
    """Extract an archive file (.zip, .tar, .gz) to the specified directory.

    Args:
        data_path: The path to the file or directory.
        output_dir: The directory where the archive should be extracted. Defaults to None.

    Returns:
        The path to the extracted folder if it was an archive, otherwise returns the original data_path.
    
    Raises:
        InvalidInputPathError: If the data_path does not exist.
    """

    if not os.path.exists(data_path):
        raise InvalidInputPathError(f"Path does not exist: {data_path}")

    if os.path.isfile(data_path):
        valid_exts = ['.zip', '.rar', '.tar', '.gz']
        if not any(data_path.lower().endswith(ext) for ext in valid_exts):
            return data_path

        if zipfile.is_zipfile(data_path):
            logger.info(f"Extracting zip file: {data_path}")
            extracted_folder = os.path.splitext(os.path.basename(data_path))[0]
            target_path = os.path.join(output_dir or os.path.dirname(data_path), extracted_folder)
            
            os.makedirs(target_path, exist_ok=True)
            with zipfile.ZipFile(data_path, 'r') as zip_ref:
                zip_ref.extractall(target_path)
                
            return target_path
            
        elif tarfile.is_tarfile(data_path):
            logger.info(f"Extracting tar file: {data_path}")
            extracted_folder = os.path.splitext(os.path.basename(data_path))[0]
            target_path = os.path.join(output_dir or os.path.dirname(data_path), extracted_folder)
            
            os.makedirs(target_path, exist_ok=True)
            with tarfile.open(data_path, 'r') as tar_ref:
                tar_ref.extractall(target_path)
            
            return target_path
        else:
            logger.warning(f"File {data_path} has an archive extension but is not a recognized archive format.")
            return data_path
    
    return data_path

def get_valid_dirs(parent_dir: Path, expected_type: str = "directory") -> Generator[Path, None, None]:
    """Yield valid subdirectories from a given parent directory, ignoring hidden ones.

    Args:
        parent_dir: The parent directory to scan.
        expected_type: The expected type of item (used for logging warnings). Defaults to "directory".

    Yields:
        Path objects representing valid subdirectories.
    """
    for item in parent_dir.iterdir():
        if item.name.startswith('.'):
            continue
        if not item.is_dir():
            logger.warning(f"Expected a directory for {expected_type}, but found file: {item}")
            continue
        yield item

def get_valid_files(
    parent_dir: Path, 
    valid_extensions: tuple | list | None = None, 
    check_size: bool = False
) -> Generator[Path, None, None]:
    """Yield valid files from a given directory based on extensions and size criteria.

    Args:
        parent_dir: The directory to scan.
        valid_extensions: A tuple or list of valid file extensions (e.g., ('.jpg', '.png')). Defaults to None.
        check_size: If True, skips files that are exactly 0 bytes. Defaults to False.

    Yields:
        Path objects representing valid files.
    """
    for item in parent_dir.iterdir():
        if item.name.startswith('.'):
            continue
        if not item.is_file():
            continue
            
        if check_size and item.stat().st_size == 0:
            logger.warning(f"Empty file detected and skipped: {item}")
            continue
            
        if valid_extensions and item.suffix.lower() not in valid_extensions:
            continue
            
        yield item

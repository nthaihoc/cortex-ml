"""
CortexML Custom Exception Hierarchy.

All domain-specific exceptions inherit from CortexError.
Core modules ONLY raise these exceptions — they never call logger.error().
The CLI entrypoint (cli.py) is the ONLY place that catches and logs them.

Exception Tree:
    CortexError
    ├── InvalidInputPathError    (State 1: bad path, wrong file type)
    ├── DatasetStructureError    (State 1: invalid folder hierarchy)
    ├── PreprocessingError       (State 2: feature engineering failures)
    ├── ExecutionError           (State 3: model/algorithm failures)
    └── StorageError             (State 4: save/export failures)
"""


class CortexError(Exception):
    """Base exception for all CortexML errors."""
    pass


class InvalidInputPathError(CortexError):
    """Raised when the input path does not exist or is not a valid format."""
    pass


class DatasetStructureError(CortexError):
    """Raised when the dataset directory structure is invalid or non-standard."""
    pass


class PreprocessingError(CortexError):
    """Raised when a preprocessing strategy fails."""
    pass


class ExecutionError(CortexError):
    """Raised when core execution (model training, statistics, etc.) fails."""
    pass


class StorageError(CortexError):
    """Raised when saving metadata, CSV, or other outputs fails."""
    pass

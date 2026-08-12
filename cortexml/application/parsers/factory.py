from typing import Type
from loguru import logger

from .base_parser import PipelineBaseParser
from .image_parsers import ImageFlatClassesParser, ImagePartitionedClassesParser
from cortexml.application.splitters import BaseSplitter
from cortexml.application.storage import MetadataStorage
from cortexml.exceptions import DatasetStructureError

class ParserDispatcher:
    """Dispatcher to instantiate the correct parser based on pattern type."""
    def __init__(self) -> None:
        self._parsers: dict[str, Type[PipelineBaseParser]] = {}

    @classmethod
    def build(cls) -> "ParserDispatcher":
        dispatcher = cls()
        return dispatcher

    def register_flat_classes(self) -> "ParserDispatcher":
        self.register("flat_classes", ImageFlatClassesParser)
        return self

    def register_partitioned_classes(self) -> "ParserDispatcher":
        self.register("partitioned_classes", ImagePartitionedClassesParser)
        return self

    def register(self, pattern_type: str, parser_class: Type[PipelineBaseParser]) -> None:
        self._parsers[pattern_type] = parser_class

    def get_parser(
        self,
        pattern_type: str, 
        data_path: str, 
        splitter: BaseSplitter, 
        storage: MetadataStorage
    ) -> PipelineBaseParser:
        """Returns the appropriate parser object based on the detected pattern.
        
        Args:
            pattern_type: The detected structure pattern (e.g., 'flat_classes').
            data_path: Path to the dataset directory.
            splitter: The BaseSplitter instance to use.
            storage: The MetadataStorage instance to use.
            
        Returns:
            An instantiated PipelineBaseParser object.
            
        Raises:
            DatasetStructureError: If the pattern_type is not registered.
        """
        parser_class = self._parsers.get(pattern_type)
        if not parser_class:
            raise DatasetStructureError(f"Unknown pattern type: {pattern_type}")
            
        return parser_class(data_path, splitter, storage)

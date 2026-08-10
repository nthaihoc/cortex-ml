from typing import Dict, Type
from loguru import logger

from cortexml.application.parsers.base_parser import PipelineBaseParser
from cortexml.application.parsers.image_parsers import ImageFlatClassesParser, ImagePartitionedClassesParser
from cortexml.application.splitters.base import BaseSplitter
from cortexml.application.storage.metadata import MetadataStorage
from cortexml.exceptions import DatasetStructureError

class ParserDispatcher:
    """
    Dispatcher to instantiate the correct parser based on pattern type.
    """
    def __init__(self) -> None:
        self._parsers: Dict[str, Type[PipelineBaseParser]] = {}

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
        """
        Returns the appropriate parser object based on the detected pattern.
        """
        parser_class = self._parsers.get(pattern_type)
        if not parser_class:
            raise DatasetStructureError(f"Unknown pattern type: {pattern_type}")
            
        return parser_class(data_path, splitter, storage)

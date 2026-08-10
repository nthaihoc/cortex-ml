from typing import Dict, Type, Optional
from loguru import logger

from cortexml.application.splitters.base import BaseSplitter
from cortexml.application.splitters.strategies import RandomSplitter, StratifiedSplitter, KeepOriginalSplitter

class SplitterDispatcher:
    """
    Dispatcher to instantiate the correct splitter based on split type.
    """
    def __init__(self) -> None:
        self._splitters: Dict[str, Type[BaseSplitter]] = {}

    @classmethod
    def build(cls) -> "SplitterDispatcher":
        dispatcher = cls()
        return dispatcher

    def register_random(self) -> "SplitterDispatcher":
        self.register("random", RandomSplitter)
        return self

    def register_stratified(self) -> "SplitterDispatcher":
        self.register("stratified", StratifiedSplitter)
        return self

    def register_keep(self) -> "SplitterDispatcher":
        self.register("keep", KeepOriginalSplitter)
        return self

    def register(self, split_type: str, splitter_class: Type[BaseSplitter]) -> None:
        self._splitters[split_type] = splitter_class

    def get_splitter(self, split_type: str, ratios: Optional[Dict[str, float]] = None) -> BaseSplitter:
        """
        Returns the appropriate splitter object.
        """
        splitter_class = self._splitters.get(split_type)
        if not splitter_class:
            raise ValueError(f"Unsupported split_type: {split_type}")
            
        if split_type == "keep":
            return splitter_class()
        return splitter_class(ratios)

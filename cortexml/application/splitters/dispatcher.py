from typing import Callable
from loguru import logger

from .base import BaseSplitter
from .strategies import RandomSplitter, StratifiedSplitter, KeepOriginalSplitter

class SplitterDispatcher:
    """
    Dispatcher to instantiate the correct splitter based on split type.
    """
    def __init__(self) -> None:
        self._splitters: dict[str, Callable[..., BaseSplitter]] = {}

    @classmethod
    def build(cls) -> "SplitterDispatcher":
        dispatcher = cls()
        return dispatcher

    def register_random(self) -> "SplitterDispatcher":
        self.register("random", lambda ratios, seed: RandomSplitter(ratios, seed))
        return self

    def register_stratified(self) -> "SplitterDispatcher":
        self.register("stratified", lambda ratios, seed: StratifiedSplitter(ratios, seed))
        return self

    def register_keep(self) -> "SplitterDispatcher":
        self.register("keep", lambda ratios, seed: KeepOriginalSplitter())
        return self

    def register(self, split_type: str, factory: Callable[..., BaseSplitter]) -> None:
        self._splitters[split_type] = factory

    def get_splitter(self, split_type: str, ratios: dict[str, float] | None = None, seed: int = 42) -> BaseSplitter:
        """
        Returns the appropriate splitter object.
        """
        factory = self._splitters.get(split_type)
        if not factory:
            raise ValueError(f"Unsupported split_type: {split_type}")
            
        return factory(ratios, seed)

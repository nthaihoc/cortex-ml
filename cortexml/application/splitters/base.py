from abc import ABC, abstractmethod
import pandas as pd

class BaseSplitter(ABC):
    """
    Abstract interface for splitting strategies.
    """
    
    @abstractmethod
    def split(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Splits the dataset according to the specific strategy.
        Modifies the 'split' column in the DataFrame in-place or returns a new one.
        
        Args:
            df: The DataFrame following the Data Contract.
            
        Returns:
            pd.DataFrame: The DataFrame with the 'split' column updated.
        """
        pass

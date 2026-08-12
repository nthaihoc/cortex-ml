from abc import ABC, abstractmethod
import pandas as pd

class BaseSplitter(ABC):

    """Abstract interface for splitting strategies."""
    
    @abstractmethod
    def split(self, df: pd.DataFrame) -> pd.DataFrame:
        
        """Splits the dataset according to the specific strategy.
        
        Modifies the 'split' column in the DataFrame. The strategy applies
        only to rows where the 'split' column is 'unassigned', preserving
        any pre-existing splits.
        
        Args:
            df: The input DataFrame containing at least a 'split' column.
            
        Returns:
            The DataFrame with the 'split' column updated.
        """
        ...

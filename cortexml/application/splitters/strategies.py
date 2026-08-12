import pandas as pd
import numpy as np

from loguru import logger
from sklearn.model_selection import train_test_split

from .base import BaseSplitter

class KeepOriginalSplitter(BaseSplitter):
    """
    Does not change the splits. Keeps whatever was extracted.
    """
    def split(self, df: pd.DataFrame) -> pd.DataFrame:
        return df

class RatioBasedSplitter(BaseSplitter):
    """
    Intermediate base class that handles ratio initialization and normalization.
    """
    def __init__(self, ratios: dict[str, float] | None = None, seed: int = 42):
        self.seed = seed
        if ratios is None:
            logger.info(f"No ratios provided to {self.__class__.__name__}. Using default: {{'train': 0.8, 'val': 0.1, 'test': 0.1}}")
            self.ratios = {'train': 0.8, 'val': 0.1, 'test': 0.1}
        else:
            self.ratios = ratios
            
        total = sum(self.ratios.values())
        self.ratios = {k: v / total for k, v in self.ratios.items()}

class RandomSplitter(RatioBasedSplitter):
    """
    Randomly splits only 'unassigned' data into train/val/test according to ratios.
    Uses sklearn's train_test_split.
    """
    def split(self, df: pd.DataFrame) -> pd.DataFrame:
        unassigned_mask = df['split'] == 'unassigned'
        unassigned_idx = df[unassigned_mask].index.tolist()
        
        if not unassigned_idx:
            return df
            
        remaining_idx = unassigned_idx
        remaining_ratio = 1.0
        
        splits_keys = list(self.ratios.keys())
        for i, split_name in enumerate(splits_keys):
            if i == len(splits_keys) - 1 or not remaining_idx:
                if remaining_idx:
                    df.loc[remaining_idx, 'split'] = split_name
                break
                
            current_ratio = self.ratios[split_name]
            fraction = current_ratio / remaining_ratio if remaining_ratio > 0 else 0
            
            n_remaining = len(remaining_idx)
            n_split = int(n_remaining * min(fraction, 1.0))
            
            if n_split == 0:
                continue
            if n_split == n_remaining:
                df.loc[remaining_idx, 'split'] = split_name
                remaining_idx = []
            else:
                split_idx, remaining_idx = train_test_split(
                    remaining_idx, 
                    train_size=n_split, 
                    shuffle=True,
                    random_state=self.seed
                )
                df.loc[split_idx, 'split'] = split_name
                
            remaining_ratio -= current_ratio
            
        return df

class StratifiedSplitter(RatioBasedSplitter):
    
    """
    Stratified split to maintain class label distribution among splits.
    Applies only to 'unassigned' data.
    Uses sklearn's train_test_split with stratify parameter.
    """

    def split(self, df: pd.DataFrame) -> pd.DataFrame:
        unassigned_mask = df['split'] == 'unassigned'
        unassigned_df = df[unassigned_mask]
        
        if unassigned_df.empty:
            return df
            
        remaining_idx = unassigned_df.index.tolist()
        remaining_labels = unassigned_df['label'].tolist()
        remaining_ratio = 1.0
        
        splits_keys = list(self.ratios.keys())
        for i, split_name in enumerate(splits_keys):
            if i == len(splits_keys) - 1 or not remaining_idx:
                if remaining_idx:
                    df.loc[remaining_idx, 'split'] = split_name
                break
                
            current_ratio = self.ratios[split_name]
            fraction = current_ratio / remaining_ratio if remaining_ratio > 0 else 0
            
            n_remaining = len(remaining_idx)
            n_split = int(n_remaining * min(fraction, 1.0))
            
            if n_split == 0:
                continue
            if n_split == n_remaining:
                df.loc[remaining_idx, 'split'] = split_name
                remaining_idx = []
                remaining_labels = []
            else:
                try:
                    split_idx, remaining_idx, _, remaining_labels = train_test_split(
                        remaining_idx, remaining_labels,
                        train_size=n_split, 
                        stratify=remaining_labels, 
                        shuffle=True,
                        random_state=self.seed
                    )
                except ValueError as e:
                    logger.warning(f"Stratified split failed: {e}. Falling back to random split for '{split_name}'.")
                    split_idx, remaining_idx, _, remaining_labels = train_test_split(
                        remaining_idx, remaining_labels,
                        train_size=n_split, 
                        shuffle=True,
                        random_state=self.seed
                    )
                    
                df.loc[split_idx, 'split'] = split_name
                
            remaining_ratio -= current_ratio
            
        return df

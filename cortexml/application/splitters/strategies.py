import pandas as pd
import numpy as np
from typing import Dict, Optional
from cortexml.application.splitters.base import BaseSplitter

class KeepOriginalSplitter(BaseSplitter):
    """
    Does not change the splits. Keeps whatever was extracted.
    """
    def split(self, df: pd.DataFrame) -> pd.DataFrame:
        return df

class RandomSplitter(BaseSplitter):
    """
    Randomly splits only 'unassigned' data into train/val/test according to ratios.
    """
    def __init__(self, ratios: Optional[Dict[str, float]] = None):
        self.ratios = ratios or {'train': 0.8, 'val': 0.1, 'test': 0.1}
        # Normalize ratios to sum to 1
        total = sum(self.ratios.values())
        self.ratios = {k: v / total for k, v in self.ratios.items()}
        
    def split(self, df: pd.DataFrame) -> pd.DataFrame:
        unassigned_mask = df['split'] == 'unassigned'
        unassigned_idx = df[unassigned_mask].index.tolist()
        
        if not unassigned_idx:
            return df
            
        np.random.shuffle(unassigned_idx)
        
        n = len(unassigned_idx)
        start = 0
        
        # Iterate and assign splits
        splits_keys = list(self.ratios.keys())
        for i, split_name in enumerate(splits_keys):
            ratio = self.ratios[split_name]
            end = start + int(n * ratio)
            
            # Ensure the last split gets all remaining elements (handles rounding issues)
            if i == len(splits_keys) - 1:
                end = n
                
            split_idx = unassigned_idx[start:end]
            df.loc[split_idx, 'split'] = split_name
            start = end
            
        return df

class StratifiedSplitter(BaseSplitter):
    """
    Stratified split to maintain class label distribution among splits.
    Applies only to 'unassigned' data.
    """
    def __init__(self, ratios: Optional[Dict[str, float]] = None):
        self.ratios = ratios or {'train': 0.8, 'val': 0.1, 'test': 0.1}
        total = sum(self.ratios.values())
        self.ratios = {k: v / total for k, v in self.ratios.items()}
        
    def split(self, df: pd.DataFrame) -> pd.DataFrame:
        unassigned_mask = df['split'] == 'unassigned'
        
        if not unassigned_mask.any():
            return df
            
        def stratify_group(group: pd.DataFrame) -> pd.DataFrame:
            idx = group.index.tolist()
            np.random.shuffle(idx)
            n = len(idx)
            start = 0
            
            splits_keys = list(self.ratios.keys())
            for i, split_name in enumerate(splits_keys):
                ratio = self.ratios[split_name]
                end = start + int(n * ratio)
                if i == len(splits_keys) - 1:
                    end = n
                    
                split_idx = idx[start:end]
                group.loc[split_idx, 'split'] = split_name
                start = end
            return group

        # Apply on unassigned data grouped by label
        unassigned_df = df[unassigned_mask]
        
        # We need to suppress the DeprecationWarning for group_keys in pandas 2.0+
        # In recent pandas, apply on grouped df doesn't add group keys if they match index,
        # but to be safe and avoid index mismatch, we re-assign carefully.
        stratified = unassigned_df.groupby('label', group_keys=False).apply(stratify_group)
        
        df.loc[unassigned_mask] = stratified
        return df

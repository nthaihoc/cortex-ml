import json
import os
from pathlib import Path
import pandas as pd
from typing import Dict, Any

class MetadataStorage:
    """
    Handles saving the dataset metadata and statistics.
    """
    
    def save(self, df: pd.DataFrame, output_dir: str) -> Dict[str, Any]:
        """
        Saves the metadata (logical paths) and statistics.
        Does NOT copy the physical files to save space.
        
        Args:
            df: DataFrame following Data Contract (filepath, label, split)
            output_dir: Directory to save metadata files.
            
        Returns:
            Dict containing the dataset statistics.
        """
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        
        # Calculate statistics
        stats: Dict[str, Any] = {
            "total_samples": len(df),
            "splits": {},
            "labels": {}
        }
        
        if not df.empty:
            # Count by split
            split_counts = df['split'].value_counts().to_dict()
            stats["splits"] = {str(k): int(v) for k, v in split_counts.items()}
            
            # Count by label
            label_counts = df['label'].value_counts().to_dict()
            stats["labels"] = {str(k): int(v) for k, v in label_counts.items()}
            
        # Save metadata.json
        json_path = out_path / "metadata.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=4)
            
        # Save metadata.csv
        csv_path = out_path / "metadata.csv"
        df.to_csv(csv_path, index=False)
        
        return stats

import pandas as pd
from cortexml.application.splitters import RandomSplitter

def test_random_splitter():
    df = pd.DataFrame({
        'filepath': ['f1', 'f2', 'f3', 'f4', 'f5'],
        'label': ['A', 'A', 'B', 'B', 'C'],
        'split': ['unassigned'] * 5
    })
    
    splitter = RandomSplitter({'train': 0.6, 'val': 0.2, 'test': 0.2})
    df_split = splitter.split(df)
    
    assert 'unassigned' not in df_split['split'].values
    assert set(df_split['split'].unique()).issubset({'train', 'val', 'test'})

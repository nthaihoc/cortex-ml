import os
import pytest
import pandas as pd
from pathlib import Path

from cortexml.application import StructureScanner, run_ingestion
from cortexml.application.splitters import RandomSplitter, StratifiedSplitter, KeepOriginalSplitter
from cortexml.application.storage import MetadataStorage
from cortexml.application.parsers import ParserFactory, ImagePatternAParser, ImagePatternBParser
from cortexml.exceptions import DatasetStructureError

@pytest.fixture
def pattern_a_dir(tmp_path):
    # root/class_1/img.jpg
    d = tmp_path / "pattern_a"
    (d / "class_1").mkdir(parents=True)
    (d / "class_1" / "img1.jpg").touch()
    (d / "class_1" / "img2.jpg").touch()
    (d / "class_2").mkdir(parents=True)
    (d / "class_2" / "img3.jpg").touch()
    return d

@pytest.fixture
def pattern_b_dir(tmp_path):
    # root/train/class_1/img.jpg
    d = tmp_path / "pattern_b"
    (d / "train" / "class_1").mkdir(parents=True)
    (d / "train" / "class_1" / "img1.jpg").touch()
    (d / "val" / "class_1").mkdir(parents=True)
    (d / "val" / "class_1" / "img2.jpg").touch()
    return d

def test_structure_scanner(pattern_a_dir, pattern_b_dir, tmp_path):
    assert StructureScanner.detect(str(pattern_a_dir)) == "PATTERN_A"
    assert StructureScanner.detect(str(pattern_b_dir)) == "PATTERN_B"
    
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()
    with pytest.raises(DatasetStructureError):
        StructureScanner.detect(str(empty_dir))

def test_image_pattern_a_parser(pattern_a_dir):
    storage = MetadataStorage()
    splitter = KeepOriginalSplitter()
    parser = ParserFactory.get_parser("PATTERN_A", str(pattern_a_dir), splitter, storage)
    assert isinstance(parser, ImagePatternAParser)
    
    parser._validate_input()
    df = parser.extract()
    
    assert len(df) == 3
    assert set(df.columns) == {'filepath', 'label', 'split'}
    assert set(df['label'].unique()) == {'class_1', 'class_2'}
    assert set(df['split'].unique()) == {'unassigned'}

def test_image_pattern_b_parser(pattern_b_dir):
    storage = MetadataStorage()
    splitter = KeepOriginalSplitter()
    parser = ParserFactory.get_parser("PATTERN_B", str(pattern_b_dir), splitter, storage)
    assert isinstance(parser, ImagePatternBParser)
    
    parser._validate_input()
    df = parser.extract()
    
    assert len(df) == 2
    assert set(df.columns) == {'filepath', 'label', 'split'}
    assert set(df['split'].unique()) == {'train', 'val'}

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
    
def test_main_pipeline(pattern_a_dir, tmp_path):
    output_dir = tmp_path / "out"
    output_dir.mkdir()
    
    stats = run_ingestion(
        data_path=str(pattern_a_dir),
        output_dir=str(output_dir),
        split_type="random",
        split_ratios={'train': 0.6, 'val': 0.4}
    )
    
    assert stats["total_samples"] == 3
    assert "train" in stats["splits"] or "val" in stats["splits"]
    
    # Check if metadata was saved
    assert (output_dir / "metadata.json").exists()
    assert (output_dir / "metadata.csv").exists()

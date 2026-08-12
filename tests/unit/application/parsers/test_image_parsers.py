import pytest
from pathlib import Path
from cortexml.application.parsers import ParserDispatcher, ImageFlatClassesParser, ImagePartitionedClassesParser
from cortexml.application.splitters import KeepOriginalSplitter
from cortexml.application.storage import MetadataStorage

def test_image_pattern_a_parser(pattern_a_dir: Path):
    storage = MetadataStorage()
    splitter = KeepOriginalSplitter()
    parser = ParserDispatcher.build().register_flat_classes().get_parser("flat_classes", str(pattern_a_dir), splitter, storage)
    assert isinstance(parser, ImageFlatClassesParser)
    
    df = parser.extract()
    
    assert len(df) == 3
    assert set(df.columns) == {'filepath', 'label', 'split'}
    assert set(df['label'].unique()) == {'class_1', 'class_2'}
    assert set(df['split'].unique()) == {'unassigned'}

def test_image_pattern_b_parser(pattern_b_dir: Path):
    storage = MetadataStorage()
    splitter = KeepOriginalSplitter()
    parser = ParserDispatcher.build().register_partitioned_classes().get_parser("partitioned_classes", str(pattern_b_dir), splitter, storage)
    assert isinstance(parser, ImagePartitionedClassesParser)
    
    df = parser.extract()
    
    assert len(df) == 2
    assert set(df.columns) == {'filepath', 'label', 'split'}
    assert set(df['split'].unique()) == {'train', 'val'}

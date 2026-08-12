import pytest
from pathlib import Path
from cortexml.application.parsers import StructureScanner
from cortexml.exceptions import DatasetStructureError

def test_structure_scanner(pattern_a_dir: Path, pattern_b_dir: Path, tmp_path: Path):
    assert StructureScanner.detect(str(pattern_a_dir)) == "flat_classes"
    assert StructureScanner.detect(str(pattern_b_dir)) == "partitioned_classes"
    
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()
    with pytest.raises(DatasetStructureError):
        StructureScanner.detect(str(empty_dir))

import pytest
from pathlib import Path

@pytest.fixture
def pattern_a_dir(tmp_path: Path):
    d = tmp_path / "pattern_a"
    (d / "class_1").mkdir(parents=True)
    (d / "class_1" / "img1.jpg").write_text("dummy")
    (d / "class_1" / "img2.jpg").write_text("dummy")
    (d / "class_2").mkdir(parents=True)
    (d / "class_2" / "img3.jpg").write_text("dummy")
    return d

@pytest.fixture
def pattern_b_dir(tmp_path: Path):
    d = tmp_path / "pattern_b"
    (d / "train" / "class_1").mkdir(parents=True)
    (d / "train" / "class_1" / "img1.jpg").write_text("dummy")
    (d / "val" / "class_1").mkdir(parents=True)
    (d / "val" / "class_1" / "img2.jpg").write_text("dummy")
    return d

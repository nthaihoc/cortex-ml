"""
Unit tests for the base parser module using explicit manual stubbing.
This module strictly follows PEP8 and professional testing standards.
"""

from pathlib import Path
from typing import Any, Dict

import pandas as pd
import pytest

from cortexml.application.parsers import PipelineBaseParser
from cortexml.application.splitters import BaseSplitter
from cortexml.application.storage import MetadataStorage


class _StubSplitter(BaseSplitter):
    """Stub implementation for the dataset splitting strategy."""

    def __init__(self) -> None:
        self.split_called = False

    def split(self, df: pd.DataFrame) -> pd.DataFrame:
        self.split_called = True
        return pd.DataFrame({"dummy": [1]})


class _StubStorage(MetadataStorage):
    """Stub implementation for metadata storage that records arguments."""

    def __init__(self) -> None:
        self.saved_kwargs: Dict[str, Any] | None = None

    def save(self, df: pd.DataFrame, output_dir: str) -> Dict[str, str]:
        self.saved_kwargs = {"df": df, "output_dir": output_dir}
        return {"status": "success"}


class _DummyParser(PipelineBaseParser):
    """Dummy concrete implementation of the abstract PipelineBaseParser."""

    def extract(self) -> pd.DataFrame:
        return pd.DataFrame({
            "filepath": ["test.jpg"],
            "label": ["cat"],
            "split": ["train"]
        })


def _build_parser(data_path: str) -> _DummyParser:
    """Assembles a parser with stubbed dependencies for testing."""
    splitter = _StubSplitter()
    storage = _StubStorage()
    return _DummyParser(data_path, splitter, storage)


def test_run_pipeline_uses_explicit_output_directory(tmp_path: Path) -> None:
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    parser = _build_parser(str(data_dir))
    out_dir = str(tmp_path / "custom_out")

    stats = parser.run_pipeline(out_dir)

    assert parser.splitter.split_called is True
    assert parser.storage.saved_kwargs is not None
    assert parser.storage.saved_kwargs["output_dir"] == out_dir
    assert stats == {"status": "success"}


def test_run_pipeline_falls_back_to_extracted_path_when_output_dir_is_none(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    parser = _build_parser(str(data_dir))

    warnings = []

    def fake_warning(msg: str) -> None:
        warnings.append(msg)

    import cortexml.application.parsers.base_parser
    monkeypatch.setattr(cortexml.application.parsers.base_parser.logger, "warning", fake_warning)

    stats = parser.run_pipeline(output_dir=None)

    assert any("Output directory not specified" in w for w in warnings)
    assert parser.splitter.split_called is True
    assert parser.storage.saved_kwargs is not None
    assert parser.storage.saved_kwargs["output_dir"] == parser.extracted_path
    assert stats == {"status": "success"}

from pathlib import Path
from cortexml.pipelines import DataIngestionPipeline

def test_main_pipeline(pattern_a_dir: Path, tmp_path: Path):
    output_dir = tmp_path / "out"
    output_dir.mkdir()
    
    pipeline = DataIngestionPipeline(
        data_path=str(pattern_a_dir),
        output_dir=str(output_dir),
        split_type="random",
        split_ratios={'train': 0.6, 'val': 0.4}
    )
    stats = pipeline.run()
    
    assert stats["total_samples"] == 3
    assert "train" in stats["splits"] or "val" in stats["splits"]
    
    assert (output_dir / "metadata.json").exists()
    assert (output_dir / "metadata.csv").exists()
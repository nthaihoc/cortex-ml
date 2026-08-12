import sys
import click
from loguru import logger

from cortexml.exceptions import CortexError
from cortexml.pipelines import DataIngestionPipeline

@click.command()
@click.option("--data-path", type=click.Path(exists=True), required=True, help="Input dataset path (.zip, .tar.gz, or directory)")
@click.option("--output-dir", type=click.Path(), default=None, help="Output directory for metadata and extracted files")
@click.option("--split-type", type=click.Choice(["random", "stratified", "keep"]), default="random", help="Type of split to apply")
@click.option("--train-ratio", type=float, default=0.8, help="Ratio of data for training (e.g. 0.8)")
@click.option("--val-ratio", type=float, default=0.1, help="Ratio of data for validation (e.g. 0.1)")
@click.option("--test-ratio", type=float, default=0.1, help="Ratio of data for testing (e.g. 0.1)")
def main(data_path: str, output_dir: str | None, split_type: str, train_ratio: float, val_ratio: float, test_ratio: float) -> None:
    """
    CortexML - Refactored ML Platform CLI.
    Delegates all business logic to the Application layer (DataIngestionPipeline).
    """
    try:

        if split_type != "keep":
            total = train_ratio + val_ratio + test_ratio
            if abs(total - 1.0) > 1e-5:
                logger.warning(f"Split ratios ({train_ratio}, {val_ratio}, {test_ratio}) do not sum to 1.0 (Sum: {total}).")

        split_ratios = {
            "train": train_ratio,
            "val": val_ratio,
            "test": test_ratio
        }

        logger.info(f"Starting CortexML Ingestion Pipeline for {data_path}...")
        
        pipeline = DataIngestionPipeline(
            data_path=data_path,
            output_dir=output_dir,
            split_type=split_type,
            split_ratios=split_ratios
        )
        stats = pipeline.run()
        
        logger.success(f"Pipeline execution completed successfully! Results: {stats}")
        
    except CortexError as e:
        logger.error(str(e))
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Critical system error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

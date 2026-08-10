import sys
import argparse
from loguru import logger

from cortexml.exceptions import CortexError
from cortexml.application import run_ingestion

def main() -> None:
    """
    CLI Entrypoint. 
    Strictly handles command-line arguments and config loading.
    Delegates all business logic to the Application layer (run_ingestion).
    """
    parser = argparse.ArgumentParser(
        description="CortexML - Refactored ML Platform",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument("--data-path", type=str, required=True, help="Input dataset path")
    parser.add_argument("--output-dir", type=str, default=None, help="Output directory")
    parser.add_argument("--split-type", type=str, default="random", choices=["random", "stratified", "keep"], help="Type of split to apply")
    
    args, unknown = parser.parse_known_args()
    
    try:
        logger.info(f"Starting CortexML Ingestion Pipeline for {args.data_path}...")
        
        stats = run_ingestion(
            data_path=args.data_path,
            output_dir=args.output_dir or ".",
            split_type=args.split_type,
            # Hardcoded split ratios for now. In a real app this could be passed via args.
            split_ratios={"train": 0.8, "val": 0.1, "test": 0.1}
        )
        
        logger.success(f"Pipeline execution completed successfully! Results: {stats}")
        
    except CortexError as e:
        logger.error(str(e))
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Critical system error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

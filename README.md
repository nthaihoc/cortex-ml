# 🧠 CortexML

CortexML is a robust, modular, and extensible Machine Learning Platform designed to streamline the end-to-end ML lifecycle. Currently, the platform focuses on providing a highly reliable **Data Ingestion Engine** that automatically detects, parses, and splits datasets with strict data contracts.

## 🌟 Key Features

- **Intelligent Structure Detection:** Automatically identifies whether your dataset is structured as `flat_classes` (e.g., `class_name/image.png`) or `partitioned_classes` (e.g., `train/class_name/image.png`) without manual intervention.
- **Robust Parsing Engine:** Built with the Factory and Dispatcher design patterns, making it trivial to extend support for new data types beyond images.
- **Smart Splitting Strategies:** Supports `random`, `stratified`, and `keep` splitting strategies. It includes safety mechanisms to prevent accidental overwriting of pre-partitioned datasets.
- **Modern CLI:** A beautiful, intuitive command-line interface powered by `click`.
- **Test-Driven Architecture:** Engineered following the Test Pyramid methodology, ensuring high reliability through isolated Unit Tests and End-to-End Integration Tests.

## 🚀 Quick Start

### Installation
Ensure you have `uv` (the ultrafast Python package installer) installed, then run:
```bash
uv sync
```

### Usage
Run the Data Ingestion pipeline via the CLI:
```bash
uv run cortexml --data-path /path/to/your/dataset --output-dir /path/to/output --split-type random --train-ratio 0.8 --val-ratio 0.1 --test-ratio 0.1
```

Get help on available CLI options:
```bash
uv run cortexml --help
```

## 🏗 Architecture Overview

The system is decoupled into discrete layers:
1. **Pipeline Layer (`cortexml.pipelines`)**: The orchestrator that glues business logic together (e.g., `DataIngestionPipeline`).
2. **Application Layer (`cortexml.application`)**: The core engine containing logic for Parsers, Splitters, and Metadata Storage.
3. **CLI Layer (`cortexml.cli`)**: The entry point that delegates user inputs to the Pipeline layer.

## 🛠 Development & Testing

Run the test suite using `pytest`:
```bash
uv run pytest
```

---
*Note: This is a temporary overview. Comprehensive documentation for the entire system will be provided in the `docs/` directory as the platform evolves.*

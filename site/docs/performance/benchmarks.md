---
title: Performance Benchmarks
description: Measured performance benchmarks for the IDP Platform.
---

# :material-timer-outline: Performance Benchmarks

---

## :material-cpu-64-bit: Test Environment

Measured **2026-08-04** on:

- **OS:** Windows
- **CPU:** AMD Ryzen 7 5700U
- **RAM:** 5.8 GiB available
- **Python:** 3.13.2
- **Node.js:** 24.15.0

!!! info "Reproducibility"
    These are deterministic synthetic chain catalogs, not production hardware claims. Results on your machine will vary based on hardware and OS.

---

## :material-table: Backend Benchmark Results

| Catalog Size | Startup Time | Focus p50 | Focus p95 | Mounted Nodes |
|:---:|---:|---:|---:|:---:|
| **1,000 entities** | 510.86 ms | 3.83 ms | 4.85 ms | 3 |
| **5,000 entities** | 2,631.21 ms | 28.48 ms | 87.15 ms | 3 |

**All within milestone targets:**

- ✅ 1,000 entities startup: 510 ms < 2,000 ms target
- ✅ 5,000 entities startup: 2,631 ms < 10,000 ms target
- ✅ 5,000 entities focus p95: 87 ms < 100 ms target
- ✅ Mounted nodes: always 3 (root + 2 neighbors in chain topology)

---

## :material-magnify: Catalog Search Benchmarks

| Search Type | Catalog Size | Mean Latency |
|-------------|:---:|---:|
| Canonical reference search | 5,000 entities | 19.12 ms |
| Display text search | 5,000 entities | 19.20 ms |

✅ Both < 50 ms target.

---

## :material-microsoft-visual-studio-code: LSP Response Benchmark

| Metric | Measured | Target |
|--------|----------|--------|
| Unsaved edit → focused LSP response | 304.08 ms | < 500 ms |

This includes the full 300 ms debounce period plus workspace re-validation and response generation.

✅ Within target.

---

## :material-run: Reproducing Benchmarks

=== "Backend"

    ```bash
    cd idp-platform/backend
    .venv/bin/python -m scripts.benchmark_catalog
    ```

=== "Frontend"

    ```bash
    cd idp-platform/frontend
    npm run benchmark
    ```

=== "Generate a large catalog"

    ```bash
    cd idp-platform/backend
    python -m scripts.generate_catalog --count 5000 --output ./.generated-catalog
    CATALOG_ROOT=./.generated-catalog python -m app.local_catalog
    ```

---

## :material-link: Further Reading

- [Scalability Notes](scalability.md)
- [Performance Documentation (original)](../../docs/performance.md)

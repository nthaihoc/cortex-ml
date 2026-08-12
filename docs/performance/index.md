---
title: Performance
description: Performance benchmarks and scalability targets for the IDP Platform.
---

# :material-gauge: Performance

The IDP Platform is designed to handle catalog sizes up to **5,000 entities** with sub-second focused topology responses.

<div class="grid cards" markdown>

-   :material-timer-outline:{ .lg .middle } **Benchmarks**

    Measured startup, focus, and search performance numbers.

    [:octicons-arrow-right-24: View Benchmarks](benchmarks.md)

-   :material-scale-balance:{ .lg .middle } **Scalability**

    Design decisions that keep the viewer fast regardless of catalog size.

    [:octicons-arrow-right-24: Scalability Notes](scalability.md)

</div>

---

## :material-check: Milestone Targets

| Metric | Target |
|--------|--------|
| 1,000 entities: startup | < 2 seconds |
| 1,000 entities: focused topology p95 | < 50 ms |
| 5,000 entities: startup | < 10 seconds |
| 5,000 entities: focused topology p95 | < 100 ms |
| 5,000 entities: catalog search | < 50 ms |
| Unsaved edit → LSP response | < 500 ms |
| One-hop focused graph: max nodes | ≤ 3 (root + immediate neighbors) |

---

## :material-run: Running Benchmarks

```bash
# Backend (Python)
cd backend
python -m scripts.benchmark_catalog

# Frontend (TypeScript)
cd frontend
npm run benchmark
```

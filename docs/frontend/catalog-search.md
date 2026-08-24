---
title: Catalog Search
description: Full-text catalog search implementation in the frontend.
---

# :material-text-search: Catalog Search

The frontend provides a search bar to find entities by name, reference, or description. Because the catalog is local and relatively small, **search runs entirely in the browser**.

**Location:** `frontend/src/topology/catalogSearch.ts`

---

## How Search Works

1. On startup (and when the revision changes), the frontend fetches the **full catalog snapshot** via `GET /api/v1/catalog/snapshot`.
2. The snapshot is stored in memory.
3. When you type in the search box, the search function filters the in-memory snapshot immediately.
4. When you select a result, the `TopologyViewer` re-focuses on that entity's canonical reference.

---

## Ranking Algorithm

Search results are ranked based on where the match was found:

1. **Exact match on reference:** e.g., typing `component:platform/payment`
2. **Match on display name:** e.g., typing `Payment Gateway`
3. **Match on description:** e.g., typing `handles credit cards`

The search is **case-insensitive** and uses simple substring matching.

---

## Performance Limits

In benchmarks (`frontend/src/topology/catalogSearch.bench.ts`), the in-browser search filters 5,000 entities in **under 3 ms**.

For local workspaces, 5,000 entities is well beyond typical sizes (usually < 500), so the in-browser approach is both simple and extremely fast.

---

## Further Reading

- [Topology Viewer](topology-viewer.md) — What happens when you select a search result
- [Performance Benchmarks](../performance/benchmarks.md) — Search and render timings

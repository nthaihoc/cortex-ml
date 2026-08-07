---
title: Catalog Search
description: Full-text catalog search implementation in the frontend.
---

# :material-magnify: Catalog Search

**File:** `frontend/src/topology/catalogSearch.ts`

The catalog search provides **full-text search over the entire catalog snapshot** — including both resolved entities and drafts.

---

## :material-search-web: Search Scope

The search index is built from:

- **Canonical references** — `component:platform/payment-gateway`
- **Display names** — `"Payment Gateway Service"`

Both canonical reference search and display-text search are independently searchable.

---

## :material-information-outline: Performance

| Catalog Size | Search Latency (mean) |
|-------------|----------------------|
| 5,000 entities | 19.12 ms (canonical) |
| 5,000 entities | 19.20 ms (display text) |

These benchmarks run via `npm run benchmark` in the `frontend/` directory.

---

## :material-code-braces: Implementation

The search is a lightweight linear scan optimized for the bounded graph exploration model:

- The full snapshot is fetched once on load and cached
- SSE events trigger a snapshot re-fetch
- Search runs client-side against the cached snapshot
- React Flow only mounts nodes from the **focused topology** response

!!! tip "Why not a full-text index?"
    A bounded catalog (max ~5,000 entities in practice) makes linear scan with pre-computed string normalization fast enough (< 20 ms) without the complexity of an inverted index.

---

## :material-link: Further Reading

- [Topology Viewer](topology-viewer.md)
- [Performance Benchmarks](../performance/benchmarks.md)
- [ReactFlow Documentation](https://reactflow.dev/)

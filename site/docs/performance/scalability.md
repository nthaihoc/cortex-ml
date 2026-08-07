---
title: Scalability
description: Design decisions that keep the IDP Platform viewer fast at scale.
---

# :material-scale-balance: Scalability Notes

---

## :material-lightbulb-outline: Key Design Decisions

### 1. One-Hop Fixed Depth

The topology viewer is **intentionally fixed at depth=1**. A single focused query returns at most:

- 1 root node
- N immediate incoming/outgoing neighbors
- Their connecting relations

For a linear chain of 5,000 entities, the focused view mounts exactly **3 nodes**, independent of catalog size.

Navigation continues by clicking related nodes — each becomes the new focused root for the next one-hop query.

### 2. Separate Search and Graph Indexes

- **Search** operates over the full in-memory snapshot (`/api/v1/catalog/snapshot`)
- **Graph rendering** uses only the focused topology response (`/api/v1/catalog/topology`)

This means the React Flow canvas never mounts the full catalog, regardless of catalog size.

### 3. In-Memory Only

All catalog data is held in Python dictionaries. No ORM, no query planner, no I/O on the critical path for focused topology queries.

### 4. Revision-Gated Refetch

SSE events carry a revision number. The browser compares the received revision with its current state and refetches only when necessary. No full-catalog pushes.

### 5. Per-File Debounce

File changes are debounced per-file key (300 ms). Rapid burst saves (e.g., auto-format on save) apply only the final version once.

---

## :material-alert-outline: Known Scalability Limits

| Limit | Threshold | Notes |
|-------|----------|-------|
| Startup time | ~5,000 entities | Linear scan; no lazy loading |
| In-memory footprint | ~5,000 entities | All descriptors held in RAM |
| File size | 1 MB per descriptor | Enforced by `DEFAULT_MAX_DESCRIPTOR_SIZE_BYTES` |
| Topology depth | Fixed at 1 hop | Architectural constraint |
| Concurrent users | 1 (loopback only) | Local development tool, not a production server |

---

## :material-link: Further Reading

- [Benchmarks](benchmarks.md)
- [Architecture Overview](../architecture/index.md)
- [Performance Documentation (original)](../../docs/performance.md)

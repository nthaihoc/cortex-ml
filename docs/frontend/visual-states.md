---
title: Visual States
description: Node and edge visual states used throughout the topology viewer.
---

# :material-palette-outline: Visual States

The topology viewer uses colors, borders, and icons to communicate the **health**, **freshness**, and **state** of every node.

**Location:** `frontend/src/topology/` and `frontend/src/styles.css`

---

## Health States

Based on the `health` field returned by the API.

| Health | Visual | Meaning |
|--------|--------|---------|
| **Healthy** | Normal colors | No diagnostics, or only `info` diagnostics. |
| **Warning** | :material-alert: Yellow border | Entity has `warning` diagnostics (non-blocking). |
| **Error** | :material-close-circle: Red border | Entity has `error` diagnostics (blocking). |

---

## Freshness States

Based on the `freshness` field returned by the API.

| Freshness | Visual | Meaning |
|-----------|--------|---------|
| **Current** | Solid lines | The data matches the current file on disk. |
| **Stale** | Dashed lines / Faded | The file was broken by a recent edit. We are showing the **last valid state**. |

---

## Node Types

Based on the `state` field of the topology node.

| State | Visual | Meaning |
|-------|--------|---------|
| **Entity** | Solid background | A fully valid, resolved entity. |
| **Draft** | Yellow background, dashed border | A file with blocking errors that has *never* been valid before. |
| **Conflict** | Red background, thick border | Two or more files are fighting over this identity. |
| **Unresolved** | Gray background, dotted border | A relation target (like `dependsOn`) that does not exist in the catalog. |

---

## Edge Types

Relations (edges) also have states based on their provenance.

| State | Visual | Meaning |
|-------|--------|---------|
| **Valid** | Solid line | The relation was declared in a valid file. |
| **Stale** | Dashed line | The relation was declared in a file that is now broken. |
| **Provisional** | Dotted line | Reserved for future use (e.g., inferred relations). |

When you **hover** over an edge, it highlights and displays a tooltip with the `protocol` and `reason` (if they were declared in the YAML).

---

## Further Reading

- [State Management](../architecture/state.md) — How these states are tracked in the backend
- [Topology Viewer](topology-viewer.md) — The ReactFlow component that renders these states

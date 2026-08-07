---
title: Visual States
description: Node and edge visual states used throughout the topology viewer.
---

# :material-palette-outline: Visual States

The IDP Platform viewer uses **health badges, icons, and edge styles** to communicate entity and relation state. Visual states never rely on color alone — text and icon badges are always present.

---

## :material-cube-outline: Node States

| State | Badge | Description |
|-------|-------|-------------|
| `entity` + `healthy` | :material-check-circle: Green | Fully resolved, valid entity |
| `entity` + `warning` | :material-alert-circle: Amber | Entity has non-blocking warnings (e.g., Location kind) |
| `entity` + `error` + `stale` | :material-clock-alert: Red / Strikethrough | Last-valid entity; current descriptor is invalid |
| `draft` | :material-pencil-circle: Red | Document never successfully validated |
| `unresolved` | :material-help-circle-outline: Amber dashed | Referenced entity not found in catalog |
| `conflict` | :material-alert-decagram: Red | Duplicate canonical identity — no entity wins |

---

## :material-relation-many-to-many: Relation (Edge) States

| State | Style | Description |
|-------|-------|-------------|
| `healthy` + `current` | Solid green | Both endpoints resolved and valid |
| `healthy` + `warning` | Dashed amber | Target entity not found (missing target) |
| `error` + `provisional` | Dotted red | Source is invalid, conflicted, or in a draft |

---

## :material-cube: Node Additional Information

Nodes may display supplementary badges:

| Badge | Source | Description |
|-------|--------|-------------|
| **Component type** | `spec.type` | e.g., `service`, `gateway`, `worker` |
| **System** | `spec.system` / `metadata.system` | Parent system reference |
| **Owners** | `spec.owners.members[*].user` / `spec.owner` | Owner email(s) |

---

## :material-eye: Inspector Panel

Selecting a node opens an **inspector panel** showing:

- Full canonical reference
- Document provenance (file path + field path)
- All active diagnostics for that entity
- Relation provenance for each edge

---

## :material-link: Further Reading

- [Topology Viewer](topology-viewer.md)
- [Diagnostics Guide](../diagnostics/index.md)
- [Architecture: State Management](../architecture/state.md)

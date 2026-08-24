---
title: Severity & Blocking
description: Understanding error vs warning severity and blocking diagnostics.
---

# :material-shield-alert: Severity & Blocking

Every diagnostic has a **Severity** and a **Blocking** flag. Understanding the difference between these is crucial for fixing catalog issues.

---

## Severity

Severity determines **how the diagnostic is presented** to the user.

| Severity | VS Code | Webview | API (`health`) |
|----------|---------|---------|----------------|
| `error` | Red squiggly line | Red border | `"error"` |
| `warning` | Yellow squiggly line | Yellow border | `"warning"` |

The API computes the overall `health` of an entity by taking the highest severity diagnostic attached to it. If an entity has both a warning and an error, its health is `"error"`.

---

## Blocking Flag

The `blocking` boolean flag determines **whether the entity is registered** in the catalog.

### `blocking: true` (Draft or Stale)
If a file has *any* blocking diagnostic, the `CatalogWorkspace` rejects it. 
- If the file was never valid before, it becomes a **Draft**.
- If the file was previously valid, it becomes **Stale** (we keep showing the last valid state).

*Example:* A YAML syntax error (`YAML_SYNTAX_ERROR`) means we literally cannot read the file. We have to block it.

### `blocking: false` (Registered)
If a file has *only* non-blocking diagnostics (warnings), it is successfully registered in the catalog and appears as a normal entity.

*Example:* Referencing an entity that doesn't exist yet (`REFERENCE_TARGET_NOT_FOUND`) is non-blocking. The entity is registered, and the missing target appears as an `Unresolved` node in the topology.

---

## Matrix

Most diagnostics are blocking errors. There are currently no blocking warnings.

| Type | Blocking (`true`) | Non-Blocking (`false`) |
|------|------------------|-----------------------|
| **Error** | 20 codes (e.g., `SCHEMA_FIELD_INVALID`) | 0 codes |
| **Warning** | 0 codes | 1 code (`REFERENCE_TARGET_NOT_FOUND`) |

*Note: The platform is designed so that future custom validators could emit non-blocking errors (e.g., a mandatory company policy violation that shouldn't break the graph).*

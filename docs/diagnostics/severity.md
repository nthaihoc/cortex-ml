---
title: Severity Guide
description: Understanding diagnostic severity, blocking status, and their effects on catalog resolution.
---

# :material-alert-circle-outline: Severity Guide

---

## :material-format-list-bulleted: Severity Levels

| Severity | Description | Effect on Entity |
|----------|-------------|-----------------|
| `error` | A structural or semantic problem | May prevent entity resolution (if `blocking: true`) |
| `warning` | A non-critical issue | Entity remains resolved |

---

## :material-toggle-switch: Blocking vs. Non-Blocking

| `blocking` | Effect |
|-----------|--------|
| `true` | Entity **cannot be resolved** — it becomes a draft (or stale/last-valid if it was previously valid) |
| `false` | Entity **remains resolved** — the issue is visible but does not prevent catalog inclusion |

### Examples

| Code | Blocking | Entity State |
|------|----------|-------------|
| `YAML_SYNTAX_ERROR` | ✅ | Draft |
| `SCHEMA_FIELD_REQUIRED` | ✅ | Draft (or stale if previously valid) |
| `ENTITY_DUPLICATE_REF` | ✅ | Conflict (no entity wins) |
| `REFERENCE_TARGET_NOT_FOUND` | ❌ | Resolved with warning relation |
| `LOCATION_KIND_NOT_SUPPORTED` | ❌ | Resolved with warning |

---

## :material-clock-alert: Stale vs. Draft

| State | Meaning | Has Snapshot? |
|-------|---------|--------------|
| **Draft** | Never successfully validated | ❌ No |
| **Stale (last-valid)** | Was valid, now has blocking errors | ✅ Yes (last-valid) |

When a document goes from valid to invalid:
- Its **last-valid entity is kept** with `health: error, freshness: stale`
- Topology continues to show the last-valid graph for navigation
- Diagnostics point to the **current (invalid)** content

When the document is fixed:
- The draft/stale entity is replaced with the new healthy entity
- Relations are re-projected and freshness becomes `current`

---

## :material-microsoft-visual-studio-code: VS Code Diagnostic Colors

| Severity | VS Code Color |
|----------|--------------|
| Error | 🔴 Red underline + red gutter icon |
| Warning | 🟡 Amber underline + amber gutter icon |

The VS Code status bar shows:

- 🟢 `VSF catalog · valid` — no diagnostics
- 🟡 `VSF catalog · N warnings` — warnings only
- 🔴 `VSF catalog · N errors` — one or more errors

---

## :material-link: Further Reading

- [Diagnostic Codes](codes.md)
- [State Management](../architecture/state.md)
- [VS Code Language Diagnostics](https://code.visualstudio.com/api/language-extensions/programmatic-language-features#provide-diagnostics)

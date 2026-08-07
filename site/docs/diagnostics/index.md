---
title: Diagnostics
description: Overview of the IDP Platform diagnostic system.
---

# :material-stethoscope: Diagnostics

The IDP Platform produces **structured, stable diagnostics** for every validation issue found in catalog descriptors. Diagnostics are produced by the Python validation engine and surfaced identically in the browser viewer, VS Code editor, and HTTP API.

<div class="grid cards" markdown>

-   :material-code-tags:{ .lg .middle } **Diagnostic Codes**

    Complete reference of all diagnostic codes with descriptions and resolution steps.

    [:octicons-arrow-right-24: Codes Reference](codes.md)

-   :material-alert-circle-outline:{ .lg .middle } **Severity Guide**

    When to act on errors vs. warnings, and how blocking/non-blocking affects entity resolution.

    [:octicons-arrow-right-24: Severity Guide](severity.md)

</div>

---

## :material-format-list-bulleted: Diagnostic Structure

Every diagnostic has the same structure regardless of where it appears:

```json
{
  "code": "SCHEMA_FIELD_REQUIRED",
  "severity": "error",
  "blocking": true,
  "message": "spec.owners.members requires at least one techlead",
  "provenance": {
    "source_uri": "file:///path/to/catalog-info.yaml",
    "relative_path": "my-service/catalog-info.yaml",
    "document_version": "a3f4...",
    "field_path": "spec.owners.members"
  },
  "entity_ref": null,
  "target_ref": null,
  "suggested_action": null,
  "details": null
}
```

---

## :material-information-outline: Key Properties

| Property | Description |
|----------|-------------|
| `code` | **Stable** machine-readable identifier |
| `severity` | `"error"` or `"warning"` |
| `blocking` | If `true`, the entity cannot be resolved |
| `message` | Human-readable description |
| `provenance.field_path` | Dot-notation path to the problematic field |
| `suggested_action` | Optional remediation hint |
| `details` | Structured additional context (e.g., line/column numbers) |

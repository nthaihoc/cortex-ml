---
title: Data Schemas
description: JSON schema reference for all data types used in the HTTP API.
---

# :material-code-json: Data Schemas

All schemas are defined in [`openapi/openapi.yaml`](https://github.com/truongabc-group1/idp/blob/main/idp-platform/openapi/openapi.yaml).

---

## :material-identifier: Core Value Types

### `Health`

```json
{ "type": "string", "enum": ["healthy", "warning", "error"] }
```

| Value | Meaning |
|-------|---------|
| `"healthy"` | Entity/relation is fully resolved and valid |
| `"warning"` | Entity/relation has a non-blocking issue (e.g., missing target) |
| `"error"` | Entity/relation has a blocking issue or is in conflict |

### `Freshness`

```json
{ "type": "string", "enum": ["current", "stale"] }
```

| Value | Meaning |
|-------|---------|
| `"current"` | Represents the most recently validated version |
| `"stale"` | Represents the last-valid state; current content is invalid |

### `TopologyDirection`

```json
{ "type": "string", "enum": ["incoming", "outgoing", "both"] }
```

---

## :material-map-marker: `DocumentProvenance`

Tracks the origin of any catalog artifact back to its source file and field.

```json
{
  "source_uri": "file:///absolute/path/to/catalog-info.yaml",
  "relative_path": "my-service/catalog-info.yaml",
  "document_version": "sha256hexstring",
  "field_path": "spec.owners.members"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `source_uri` | `string (uri)` | Absolute file URI |
| `relative_path` | `string` | Path relative to Catalog Root |
| `document_version` | `string \| null` | Content-derived version identifier |
| `field_path` | `string \| null` | Dot-notation path to the specific field |

---

## :material-cube-outline: `CatalogEntity`

```json
{
  "reference": "component:platform/payment-gateway",
  "display_name": "Payment Gateway Service",
  "descriptor": { "specVersion": "vsf-idp.io/v2", "..." : "..." },
  "provenance": { "..." : "..." },
  "health": "healthy",
  "freshness": "current"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `reference` | `string` | Canonical entity reference |
| `display_name` | `string` | Human-readable display name |
| `descriptor` | `object` | The full normalized descriptor content |
| `provenance` | `DocumentProvenance` | Source file information |
| `health` | `Health` | Current health state |
| `freshness` | `Freshness` | Current/stale status |

---

## :material-relation-many-to-many: `CatalogRelation`

```json
{
  "source": "component:platform/payment-gateway",
  "target": "component:platform/auth-service",
  "relation_type": "dependsOn",
  "provenance": { "..." : "..." },
  "health": "healthy",
  "freshness": "current",
  "provisional": false,
  "protocol": "gRPC",
  "reason": "Token validation"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `source` | `string` | Source entity reference |
| `target` | `string` | Target entity reference |
| `relation_type` | `string` | One of the 7 relation types |
| `provenance` | `DocumentProvenance` | Declaring file and field |
| `health` | `Health` | Relation health |
| `freshness` | `Freshness` | Current/stale status |
| `provisional` | `boolean` | True if source is invalid/conflicted |
| `protocol` | `string \| null` | Optional transport protocol |
| `reason` | `string \| null` | Optional human-readable reason |

### Relation Types

| Value | Meaning |
|-------|---------|
| `"partOf"` | Entity belongs to a system, domain, or group |
| `"dependsOn"` | Entity depends on another component/resource |
| `"providesApi"` | Entity provides this API |
| `"consumesApi"` | Entity consumes this API |
| `"publishesTo"` | Entity publishes to this event |
| `"consumesFrom"` | Entity consumes from this event |
| `"contains"` | Entity contains this module or function |

---

## :material-stethoscope: `CatalogDiagnostic`

```json
{
  "code": "REFERENCE_TARGET_NOT_FOUND",
  "severity": "warning",
  "blocking": false,
  "message": "The declared relation target is not currently resolved",
  "provenance": { "..." : "..." },
  "entity_ref": "component:platform/payment-gateway",
  "target_ref": "component:platform/missing-service",
  "suggested_action": "Add a descriptor for the target entity",
  "details": null
}
```

| Field | Type | Description |
|-------|------|-------------|
| `code` | `string` | Stable diagnostic code |
| `severity` | `"error" \| "warning"` | Severity level |
| `blocking` | `boolean` | True means entity cannot be resolved |
| `message` | `string` | Human-readable diagnostic message |
| `provenance` | `DocumentProvenance` | File and field location |
| `entity_ref` | `string \| null` | Affected entity reference |
| `target_ref` | `string \| null` | Referenced (missing) target |
| `suggested_action` | `string \| null` | Remediation hint |
| `details` | `object \| null` | Structured additional details |

---

## :material-content-copy: `CatalogSnapshot`

The full catalog state at a single revision.

| Field | Type | Description |
|-------|------|-------------|
| `revision` | `integer` | Monotonic revision counter |
| `entities` | `object` | Map of reference → `CatalogEntity` |
| `relations` | `array` | All resolved `CatalogRelation` objects |
| `conflicts` | `object` | Map of reference → `IdentityConflict` |
| `drafts` | `object` | Map of URI → `DraftEntity` |
| `diagnostics` | `array` | All `CatalogDiagnostic` objects |

---

## :material-alert: `IdentityConflict`

```json
{
  "reference": "component:platform/payment-gateway",
  "sources": [
    { "source_uri": "file:///a/catalog-info.yaml", "relative_path": "a/catalog-info.yaml", "..." : "..." },
    { "source_uri": "file:///b/catalog-info.yaml", "relative_path": "b/catalog-info.yaml", "..." : "..." }
  ]
}
```

---

## :material-pencil: `DraftEntity`

Represents a document that has never successfully validated.

| Field | Type | Description |
|-------|------|-------------|
| `source_uri` | `string (uri)` | Source file URI |
| `display_name` | `string` | Display name (from relative path if no name parsed) |
| `provenance` | `DocumentProvenance` | Source file information |
| `entity_ref` | `string \| null` | Partially-resolved canonical reference if available |
| `health` | `Health` | Always `"error"` for drafts |
| `freshness` | `Freshness` | Freshness state |
| `has_snapshot` | `boolean` | True if a last-valid snapshot exists |

---

## :material-link: Further Reading

- [Endpoints Reference](endpoints.md)
- [Diagnostic Codes](../diagnostics/codes.md)
- [OpenAPI Specification](https://github.com/truongabc-group1/idp/blob/main/idp-platform/openapi/openapi.yaml)

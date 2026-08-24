---
title: Data Schemas
description: JSON schema reference for all data types used in the HTTP API.
---

# :material-code-json: Data Schemas

This page defines the JSON schemas used in the HTTP API responses.

---

## CatalogEntity

A fully resolved catalog entity. Found in the `/api/v1/catalog/snapshot` response.

```json
{
  "reference": "component:platform/payment-gateway",
  "display_name": "Payment Gateway Service",
  "descriptor": { 
    "specVersion": "vsf-idp.io/v2",
    "metadata": { "..." : "..." },
    "spec": { "..." : "..." }
  },
  "provenance": {
    "source_uri": "file:///path/to/catalog-info.yaml",
    "relative_path": "payment-gateway/catalog-info.yaml",
    "document_version": "a3f4b2c1...",
    "field_path": null
  },
  "health": "healthy",
  "freshness": "current"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `reference` | `string` | The canonical identity of the entity |
| `display_name` | `string` | The display name (from `spec.name` or `metadata.title`) |
| `descriptor` | `object` | The raw descriptor data after parsing |
| `provenance` | `object` | Where this entity came from (see below) |
| `health` | `"healthy"`, `"warning"`, or `"error"` | Highest severity diagnostic on this entity |
| `freshness` | `"current"` or `"stale"` | `"stale"` means the file was edited and is now invalid, but we are showing the last valid state |

---

## CatalogRelation

A connection between two entities.

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
| `source` | `string` | Canonical reference of the source entity |
| `target` | `string` | Canonical reference of the target entity |
| `relation_type` | `string` | One of: `partOf`, `dependsOn`, `providesApi`, `consumesApi`, `publishesTo`, `consumesFrom`, `contains` |
| `protocol` | `string` or `null` | Optional protocol string |
| `reason` | `string` or `null` | Optional reason string |
| `provisional` | `boolean` | Always `false` (reserved for future use) |

---

## DocumentProvenance

Describes exactly where data came from in a source file. Used for entities, relations, and diagnostics.

```json
{
  "source_uri": "file:///path/to/catalog-info.yaml",
  "relative_path": "payment-gateway/catalog-info.yaml",
  "document_version": "a3f4b2c1...",
  "field_path": "spec.topology[0].ref"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `source_uri` | `string` | Absolute `file://` URI to the file |
| `relative_path` | `string` | Path relative to the `CATALOG_ROOT` |
| `document_version` | `string` or `null` | Content hash (SHA-256) of the file when parsed |
| `field_path` | `string` or `null` | JSON path to the specific field (e.g., `spec.owners`) |

---

## CatalogDiagnostic

A validation error or warning.

```json
{
  "code": "SCHEMA_FIELD_REQUIRED",
  "severity": "error",
  "blocking": true,
  "message": "spec.owners.members requires at least one techlead",
  "provenance": { "..." : "..." },
  "entity_ref": null,
  "target_ref": null,
  "suggested_action": null,
  "details": null
}
```

| Field | Type | Description |
|-------|------|-------------|
| `code` | `string` | Stable error code (see [Diagnostic Codes](../diagnostics/codes.md)) |
| `severity` | `"error"` or `"warning"` | How serious the problem is |
| `blocking` | `boolean` | If `true`, the entity is not registered (becomes draft/stale) |
| `message` | `string` | Human-readable explanation |
| `entity_ref` | `string` or `null` | Entity reference this issue belongs to (if resolved) |
| `target_ref` | `string` or `null` | Target reference (if it's a relation issue like `REFERENCE_TARGET_NOT_FOUND`) |
| `suggested_action` | `string` or `null` | How to fix the problem |
| `details` | `object` or `null` | Extra structured data about the issue |

---

## IdentityConflict

Represents two or more files fighting over the same entity reference.

```json
{
  "reference": "component:platform/payment-gateway",
  "sources": [
    {
      "source_uri": "file:///path/a/catalog-info.yaml",
      "relative_path": "a/catalog-info.yaml",
      "document_version": "...",
      "field_path": null
    },
    {
      "source_uri": "file:///path/b/catalog-info.yaml",
      "relative_path": "b/catalog-info.yaml",
      "document_version": "...",
      "field_path": null
    }
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `reference` | `string` | The canonical reference being claimed |
| `sources` | `array` | List of `DocumentProvenance` pointing to the conflicting files |

---

## DraftEntity

A file that has blocking errors and was never valid before.

```json
{
  "source_uri": "file:///path/to/broken.yaml",
  "display_name": "unknown",
  "provenance": { "..." : "..." },
  "entity_ref": "component:platform/broken-service",
  "health": "error",
  "freshness": "current",
  "has_snapshot": false
}
```

| Field | Type | Description |
|-------|------|-------------|
| `entity_ref` | `string` or `null` | May be `null` if the error prevented computing the reference |
| `has_snapshot` | `boolean` | Always `false` for drafts |

---

## Further Reading

- [Endpoints Reference](endpoints.md) — Where these schemas are used
- [OpenAPI Specification](https://github.com/truongabc-group1/idp/blob/main/idp-platform/openapi/openapi.yaml) — The full OpenAPI 3.1 contract

---
title: API Endpoints Reference
description: Detailed request and response documentation for each HTTP API endpoint.
---

# :material-api: Endpoints Reference

## `GET /health` — Runtime Health {#get-health}

Returns the current runtime status and catalog statistics.

**Response `200 OK`:**

```json
{
  "status": "ok",
  "revision": 42,
  "entity_count": 150,
  "diagnostic_count": 3
}
```

| Field | Type | Description |
|-------|------|-------------|
| `status` | `"ok"` | Always `"ok"` when the server is running |
| `revision` | `integer` | Monotonically increasing catalog revision |
| `entity_count` | `integer` | Number of fully resolved entities |
| `diagnostic_count` | `integer` | Total active diagnostics across all documents |

---

## `GET /api/v1/catalog/snapshot` — Full Snapshot {#get-apiv1catalogsnapshot}

Returns the complete in-memory catalog snapshot.

**Response `200 OK`:**

```json
{
  "revision": 42,
  "entities": {
    "component:platform/payment-gateway": {
      "reference": "component:platform/payment-gateway",
      "display_name": "Payment Gateway Service",
      "descriptor": { ... },
      "provenance": {
        "source_uri": "file:///path/to/catalog-info.yaml",
        "relative_path": "payment-gateway/catalog-info.yaml",
        "document_version": "a3f4...",
        "field_path": null
      },
      "health": "healthy",
      "freshness": "current"
    }
  },
  "relations": [ ... ],
  "conflicts": {},
  "drafts": {},
  "diagnostics": []
}
```

---

## `GET /api/v1/catalog/topology` — Focused Topology {#get-apiv1catalogtopology}

Returns a one-hop focused topology view centered on a given entity reference.

**Query Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `root` | `string` | ✅ | — | Canonical entity reference to focus on |
| `direction` | `string` | — | `"both"` | `"incoming"`, `"outgoing"`, or `"both"` |
| `depth` | `integer` | — | `1` | Must be exactly `1` |

**Example Request:**

```
GET /api/v1/catalog/topology?root=component:platform/payment-gateway&direction=both
```

**Response `200 OK`:**

```json
{
  "root": "component:platform/payment-gateway",
  "direction": "both",
  "depth": 1,
  "nodes": {
    "component:platform/payment-gateway": {
      "reference": "component:platform/payment-gateway",
      "display_name": "Payment Gateway Service",
      "state": "entity",
      "health": "healthy",
      "freshness": "current",
      "provenance": { ... },
      "conflict_sources": []
    },
    "component:platform/auth-service": {
      "reference": "component:platform/auth-service",
      "display_name": "Auth Service",
      "state": "entity",
      "health": "healthy",
      "freshness": "current",
      "provenance": { ... },
      "conflict_sources": []
    }
  },
  "relations": [
    {
      "source": "component:platform/payment-gateway",
      "target": "component:platform/auth-service",
      "relation_type": "dependsOn",
      "provenance": { ... },
      "health": "healthy",
      "freshness": "current",
      "provisional": false,
      "protocol": "gRPC",
      "reason": "Token validation"
    }
  ]
}
```

**Error Responses:**

| Code | Description |
|------|-------------|
| `422` | Invalid `root`, unsupported `direction`, or `depth` ≠ 1 |

---

## `GET /api/v1/catalog/diagnostics` — Diagnostics {#get-apiv1catalogdiagnostics}

Returns all current diagnostics across all catalog documents.

**Response `200 OK`:**

```json
{
  "revision": 42,
  "diagnostics": [
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
  ]
}
```

---

## `GET /api/v1/catalog/events` — SSE Stream {#get-apiv1catalogevents}

Streams catalog revision change notifications as Server-Sent Events.

**Response `200 OK`** (content-type: `text/event-stream`):

```
data: {"revision":43,"changed_source_uris":["file:///path/to/catalog-info.yaml"],"removed_source_uris":[]}

data: {"revision":44,"changed_source_uris":[],"removed_source_uris":["file:///old/catalog-info.yaml"]}
```

!!! tip "Usage pattern"
    On receiving an event, clients should **refetch** the current snapshot or focused topology using the latest revision. The event payload is metadata only, not a semantic delta.

---

## `GET /api/v1/catalog/source` — Read Source {#get-apiv1catalogsource}

Reads the raw UTF-8 content of a discovered catalog descriptor.

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `relative_path` | `string` | ✅ | Root-relative path to the descriptor file |

**Response `200 OK`:**

```json
{
  "relative_path": "my-service/catalog-info.yaml",
  "source_uri": "file:///path/to/my-service/catalog-info.yaml",
  "content": "specVersion: vsf-idp.io/v2\n...",
  "document_version": "a3f4b2c1d5..."
}
```

| Code | Description |
|------|-------------|
| `404` | File not found, outside root, or is a symlink |
| `422` | File is not valid UTF-8 |

---

## `PUT /api/v1/catalog/source` — Update Source {#put-apiv1catalogsource}

Atomically saves new content to a discovered catalog descriptor.

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `relative_path` | `string` | ✅ | Root-relative path to the descriptor file |

**Request Body:**

```json
{
  "content": "specVersion: vsf-idp.io/v2\n...",
  "expected_version": "a3f4b2c1d5..."
}
```

| Field | Description |
|-------|-------------|
| `content` | New UTF-8 content to write |
| `expected_version` | SHA-256 hash of current content (from prior GET) for optimistic locking |

**Response `200 OK`:** Same as GET `/api/v1/catalog/source`.

**Error Responses:**

| Code | Description |
|------|-------------|
| `404` | File not found or not a discovered descriptor |
| `409` | `expected_version` mismatch — file changed since last read |
| `413` | Content exceeds 1 MB limit |

!!! info "Atomic write"
    The PUT endpoint writes to a temporary file and performs an atomic `os.replace()` to prevent partial writes from reaching the filesystem watcher.

---

## :material-link: Further Reading

- [Data Schemas](schemas.md)
- [SSE Events](events.md)
- [OpenAPI Specification](https://github.com/truongabc-group1/idp/blob/main/idp-platform/openapi/openapi.yaml)
- [Optimistic Concurrency Control](https://en.wikipedia.org/wiki/Optimistic_concurrency_control)

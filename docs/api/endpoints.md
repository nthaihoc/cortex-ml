---
title: API Endpoints Reference
description: Detailed request and response documentation for each HTTP API endpoint.
---

# :material-api: Endpoints Reference

All endpoints are served on `http://127.0.0.1:8000`.

---

## `GET /health` — Runtime Health {#get-health}

Returns the server status and catalog statistics.

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
| `revision` | `integer` | Current catalog revision (increases with every change) |
| `entity_count` | `integer` | Number of fully resolved entities |
| `diagnostic_count` | `integer` | Total active diagnostics across all documents |

---

## `GET /api/v1/catalog/snapshot` — Full Snapshot {#get-snapshot}

Returns the complete in-memory catalog state: all entities, relations, conflicts, drafts, and diagnostics.

**Response `200 OK`:**

```json
{
  "revision": 42,
  "entities": {
    "component:platform/payment-gateway": {
      "reference": "component:platform/payment-gateway",
      "display_name": "Payment Gateway Service",
      "descriptor": { "..." : "..." },
      "provenance": {
        "source_uri": "file:///path/to/catalog-info.yaml",
        "relative_path": "payment-gateway/catalog-info.yaml",
        "document_version": "a3f4b2c1...",
        "field_path": null
      },
      "health": "healthy",
      "freshness": "current"
    }
  },
  "relations": [
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
  ],
  "conflicts": {},
  "drafts": {},
  "diagnostics": []
}
```

---

## `GET /api/v1/catalog/topology` — Focused Topology {#get-topology}

Returns a one-hop focused topology view centered on a given entity.

**Query Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `root` | `string` | ✅ | — | Canonical entity reference to focus on |
| `direction` | `string` | — | `"both"` | `"incoming"`, `"outgoing"`, or `"both"` |
| `depth` | `integer` | — | `1` | Must be exactly `1` |

**Example:**

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
      "display_name": "Payment Gateway",
      "state": "entity",
      "health": "healthy",
      "freshness": "current",
      "provenance": { "..." : "..." },
      "conflict_sources": []
    }
  },
  "relations": [ "..." ]
}
```

**Node states:** `entity` (valid), `unresolved` (target not found), `conflict` (duplicate identity), `draft` (never valid).

| Error | Description |
|-------|-------------|
| `422` | Invalid `root`, unsupported `direction`, or `depth ≠ 1` |

---

## `GET /api/v1/catalog/diagnostics` — All Diagnostics {#get-diagnostics}

Returns all active diagnostics across all catalog documents.

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

## `GET /api/v1/catalog/events` — SSE Stream {#get-events}

Streams catalog change notifications as Server-Sent Events. The connection stays open until the client disconnects.

**Response `200 OK`** (content-type: `text/event-stream`):

```
data: {"revision":43,"changed_source_uris":["file:///path/to/catalog-info.yaml"],"removed_source_uris":[]}

data: {"revision":44,"changed_source_uris":[],"removed_source_uris":["file:///old/catalog-info.yaml"]}
```

!!! tip "How to use SSE events"
    When you receive an event, **refetch** the snapshot or topology endpoint to get the latest data. The event only tells you *that* something changed, not *what* changed.

See [SSE Events](events.md) for more details.

---

## `GET /api/v1/catalog/source` — Read a Descriptor {#get-source}

Reads the raw UTF-8 content of a discovered catalog descriptor file.

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

| Error | Description |
|-------|-------------|
| `404` | File not found, outside root, or is a symlink |
| `422` | File is not valid UTF-8 |

---

## `PUT /api/v1/catalog/source` — Update a Descriptor {#put-source}

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
| `expected_version` | SHA-256 hash from the previous GET (for optimistic locking) |

**Response `200 OK`:** Same format as GET `/api/v1/catalog/source`.

| Error | Description |
|-------|-------------|
| `404` | File not found or not a discovered descriptor |
| `409` | `expected_version` mismatch — file changed since your last read |
| `413` | Content exceeds 1 MB limit |

!!! info "Atomic write"
    The PUT endpoint writes to a temporary file first, then uses `os.replace()` to atomically swap the content. This prevents partial writes from reaching the file watcher.

---

## Further Reading

- [Data Schemas](schemas.md) — JSON type definitions
- [SSE Events](events.md) — Real-time notifications
- [OpenAPI Specification](https://github.com/truongabc-group1/idp/blob/main/idp-platform/openapi/openapi.yaml) — Full contract

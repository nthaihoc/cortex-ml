---
title: HTTP API Reference
description: Complete REST API reference for the IDP Platform Local Catalog HTTP endpoints.
---

# :material-api: HTTP API Reference

The Local Catalog HTTP API is a **loopback-only REST API** exposing catalog data to the browser viewer and any local tooling.

---

!!! warning "Loopback Only"
    The server binds exclusively to `127.0.0.1:8000`. It is **never** exposed over the network. No authentication is required or supported.

---

## :material-table: Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Runtime status, revision, entity and diagnostic counts |
| `GET` | `/api/v1/catalog/snapshot` | Complete catalog snapshot |
| `GET` | `/api/v1/catalog/topology` | Focused one-hop topology |
| `GET` | `/api/v1/catalog/diagnostics` | Current diagnostics |
| `GET` | `/api/v1/catalog/events` | SSE change stream |
| `GET` | `/api/v1/catalog/source` | Read a descriptor source file |
| `PUT` | `/api/v1/catalog/source` | Update a descriptor source file |

---

## :material-link: Detailed References

- [Endpoints Reference](endpoints.md) — Full request/response details for each endpoint
- [Data Schemas](schemas.md) — JSON schema reference for all data types
- [Server-Sent Events](events.md) — SSE stream format and usage

---

## :material-format-list-bulleted: General Conventions

- **Field names:** `snake_case` throughout
- **Canonical references:** lowercase `kind:namespace/name`
- **Nullable values:** explicit `null`, never omitted
- **Arrays and maps:** always present (never omitted), may be empty
- **Health:** `"healthy" | "warning" | "error"`
- **Freshness:** `"current" | "stale"`
- **Direction:** `"incoming" | "outgoing" | "both"`

---

## :material-open-in-app: OpenAPI Specification

The canonical contract is defined in [`openapi/openapi.yaml`](https://github.com/truongabc-group1/idp/blob/main/idp-platform/openapi/openapi.yaml):

```yaml
openapi: 3.1.0
info:
  title: Local Catalog Topology API
  version: 0.1.0
  description: Loopback-only catalog API with guarded local descriptor editing.
servers:
  - url: http://127.0.0.1:8000
```

---

## :material-link: Further Reading

- [OpenAPI 3.1 Specification](https://spec.openapis.org/oas/v3.1.0)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Server-Sent Events (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

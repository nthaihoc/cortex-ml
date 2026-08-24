---
title: HTTP API
description: REST API reference for the Local Catalog Topology server.
---

# :material-api: HTTP API

The backend serves a loopback-only REST API at `http://127.0.0.1:8000`. This API provides catalog snapshots, topology views, diagnostics, file operations, and a real-time event stream.

---

## Overview

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Server health and catalog statistics |
| `/api/v1/catalog/snapshot` | GET | Full catalog state |
| `/api/v1/catalog/topology` | GET | Focused one-hop topology view |
| `/api/v1/catalog/diagnostics` | GET | All active validation issues |
| `/api/v1/catalog/events` | GET | Real-time SSE change stream |
| `/api/v1/catalog/source` | GET | Read a descriptor file |
| `/api/v1/catalog/source` | PUT | Update a descriptor file |

All endpoints return `application/json` except the SSE stream which returns `text/event-stream`.

---

<div class="grid cards" markdown>

-   :material-format-list-bulleted:{ .lg .middle } **Endpoints Reference**

    Detailed request/response docs for every endpoint.

    [:octicons-arrow-right-24: Endpoints](endpoints.md)

-   :material-code-json:{ .lg .middle } **Data Schemas**

    JSON schema definitions for all API types.

    [:octicons-arrow-right-24: Schemas](schemas.md)

-   :material-broadcast:{ .lg .middle } **Server-Sent Events**

    Real-time catalog change notifications.

    [:octicons-arrow-right-24: SSE Events](events.md)

</div>

---

## Quick Test

After starting the backend, test the API with curl:

```bash
# Health check
curl http://127.0.0.1:8000/health

# Get full catalog snapshot
curl http://127.0.0.1:8000/api/v1/catalog/snapshot

# Get focused topology
curl "http://127.0.0.1:8000/api/v1/catalog/topology?root=component:platform/my-service"

# Get diagnostics
curl http://127.0.0.1:8000/api/v1/catalog/diagnostics
```

---

## OpenAPI Specification

The full API contract is defined in `openapi/openapi.yaml` using OpenAPI 3.1 format. You can use this spec with tools like Swagger UI, Postman, or code generators.

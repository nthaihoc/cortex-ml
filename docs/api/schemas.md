---
title: Data Schemas
description: Cấu trúc dữ liệu chính trong HTTP API response.
---

# :material-code-json: Data Schemas

Tất cả schema được định nghĩa trong `openapi/openapi.yaml`. Dưới đây là các schema quan trọng nhất.

---

## `CatalogSnapshot`

```json
{
  "revision": 42,
  "entities": { "component:platform/payment-gateway": { "..." } },
  "relations": [ { "..." } ],
  "conflicts": {},
  "drafts": {},
  "diagnostics": []
}
```

| Field | Type | Mô tả |
|---|---|---|
| `revision` | `integer` | Monotonically increasing revision counter |
| `entities` | `map<string, CatalogEntity>` | Entity đã resolve, key = canonical `EntityReference` |
| `relations` | `CatalogRelation[]` | Tất cả `CatalogRelation` đã resolve |
| `conflicts` | `map<string, IdentityConflict>` | `IdentityConflict` theo reference |
| `drafts` | `map<string, DraftEntity>` | `DraftEntity` theo `source_uri` |
| `diagnostics` | `CatalogDiagnostic[]` | Tất cả diagnostics hiện tại |

---

## `CatalogEntity`

```json
{
  "reference": "component:platform/payment-gateway",
  "display_name": "Payment Gateway Service",
  "descriptor": { "specVersion": "vsf-idp.io/v2", "..." },
  "provenance": { "..." },
  "health": "healthy",
  "freshness": "current"
}
```

| Field | Type | Mô tả |
|---|---|---|
| `reference` | `string` | Canonical `EntityReference` |
| `display_name` | `string` | Tên hiển thị |
| `descriptor` | `object` | Parsed descriptor object |
| `provenance` | `DocumentProvenance` | Metadata nguồn gốc |
| `health` | `Health` | `healthy` / `warning` / `error` |
| `freshness` | `Freshness` | `current` / `stale` |

---

## `CatalogRelation`

```json
{
  "source": "component:platform/payment-gateway",
  "target": "component:platform/auth-service",
  "relation_type": "dependsOn",
  "provenance": { "..." },
  "health": "healthy",
  "freshness": "current",
  "provisional": false,
  "protocol": "gRPC",
  "reason": "Token validation"
}
```

| Field | Type | Mô tả |
|---|---|---|
| `relation_type` | `RelationType` | `partOf`, `dependsOn`, `providesApi`, `consumesApi`, `publishesTo`, `consumesFrom`, `contains` |
| `provisional` | `boolean` | `true` nếu target chưa resolve |
| `protocol` | `string?` | Giao thức kết nối (tuỳ chọn) |
| `reason` | `string?` | Lý do quan hệ (tuỳ chọn) |

---

## `DocumentProvenance`

```json
{
  "source_uri": "file:///path/to/catalog-info.yaml",
  "relative_path": "my-service/catalog-info.yaml",
  "document_version": "a3f4b2c1...",
  "field_path": "spec.topology[0].ref"
}
```

---

## `TopologyNode`

```json
{
  "reference": "component:platform/auth-service",
  "display_name": "Auth Service",
  "state": "entity",
  "health": "healthy",
  "freshness": "current",
  "provenance": { "..." },
  "conflict_sources": []
}
```

| `state` | `TopologyNodeState` |
|---|---|
| `entity` | `CatalogEntity` đã resolve |
| `draft` | `DraftEntity` (chưa bao giờ valid) |
| `conflict` | `IdentityConflict` (duplicate reference) |
| `unresolved` | Relation target không tìm thấy |

---

## `CatalogDiagnostic`

```json
{
  "code": "SCHEMA_FIELD_REQUIRED",
  "severity": "error",
  "blocking": true,
  "message": "spec.owners.members requires at least one techlead",
  "provenance": { "..." },
  "entity_ref": null,
  "target_ref": null,
  "suggested_action": null,
  "details": null
}
```

---

## `FocusedTopology`

```json
{
  "root": "component:platform/payment-gateway",
  "direction": "both",
  "depth": 1,
  "nodes": { "...": { "..." } },
  "relations": [ { "..." } ]
}
```

---

## :material-link: Đọc thêm

- [Tham chiếu Endpoints](endpoints.md)
- [Bảng mã Diagnostic](../diagnostics/codes.md)
- [OpenAPI 3.1 Specification](https://spec.openapis.org/oas/v3.1.0)

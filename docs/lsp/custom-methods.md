---
title: Custom Methods
description: Các LSP custom methods mở rộng của CatalogLanguageServer.
---

# :material-puzzle: Custom Methods

`CatalogLanguageServer` mở rộng LSP với 11 custom methods cho topology, field editing, owner management, relation management, và completion.

---

## :material-graph: Topology

### `catalog/topologyForDocument`

Trả về `FocusedTopology` cho document đang mở.

**Params:**
```json
{
  "documentUri": "file:///path/to/catalog-info.yaml",
  "direction": "both"
}
```

**Response:** `FocusedTopology` (cùng cấu trúc với HTTP API, nhưng dùng `camelCase`).

### `catalog/revisionChanged`

**Notification** (server → client) khi `CatalogWorkspace` revision thay đổi.

```json
{"catalogRevision": 43}
```

---

## :material-pencil: Field Editing

### `catalog/fieldEdit`

Sửa một scalar field trong external entity descriptor.

**Params:**
```json
{
  "reference": "component:platform/payment-gateway",
  "fieldPath": "spec.name",
  "value": "New Service Name",
  "expectedVersion": "2026-08-26T..."
}
```

---

## :material-account-group: Owner Management

### `catalog/ownerAppend`

Thêm owner member vào entity.

```json
{
  "reference": "component:platform/payment-gateway",
  "user": "dev@vinsmartfuture.tech",
  "role": "maintainer",
  "expectedVersion": "..."
}
```

### `catalog/ownerRemove`

Xóa owner member theo index.

```json
{
  "reference": "component:platform/payment-gateway",
  "ownerIndex": 1,
  "expectedVersion": "..."
}
```

---

## :material-relation-many-to-many: Relation Management

### `catalog/relationTargets`

Tìm entity phù hợp cho relation type. Dùng cho autocomplete khi thêm topology entry.

```json
{
  "query": "auth",
  "kinds": ["component"],
  "limit": 12
}
```

### `catalog/relationOptions`

Trả về danh sách `RelationType` options khả dụng.

### `catalog/relationAppend`

Thêm relation mới vào `spec.topology[]`.

```json
{
  "reference": "component:platform/payment-gateway",
  "ref": "component:platform/auth-service",
  "protocol": "gRPC",
  "reason": "Token validation",
  "expectedVersion": "..."
}
```

### `catalog/relationReplace`

Thay thế relation tại index trong `spec.topology[]`.

### `catalog/relationRemove`

Xóa relation tại index trong `spec.topology[]`.

---

## :material-lightbulb-on: Completion

### `catalog/completion`

Completion items cho source creator drawer (khác với standard `textDocument/completion`).

```json
{
  "text": "specVersion: vsf-idp.io/v2\n...",
  "offset": 42
}
```

Response cùng format với `POST /api/v1/catalog/completion` HTTP endpoint.

---

## :material-transfer: Quy ước đặt tên

Tất cả custom methods sử dụng `camelCase`:

| Python (`CatalogLanguageService`) | LSP Method |
|---|---|
| `focused_topology_for_document()` | `catalog/topologyForDocument` |
| `entity_ref` | `entityRef` |
| `document_version` | `documentVersion` |
| `field_path` | `fieldPath` |
| `expected_version` | `expectedVersion` |
| `owner_index` | `ownerIndex` |

`CatalogLanguageService` chuyển đổi tường minh giữa `snake_case` (Python) và `camelCase` (LSP/extension).

---

## :material-link: Đọc thêm

- [Giao thức LSP](protocol.md)
- [VS Code Extension](../vscode/index.md)
- [HTTP Runtime](../backend/local-catalog.md)

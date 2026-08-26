---
title: Server-Sent Events
description: Real-time notifications qua CatalogChangeFeed.
---

# :material-broadcast: Server-Sent Events

`CatalogChangeFeed` phát SSE events khi `CatalogWorkspace` revision thay đổi. Browser client kết nối endpoint này để nhận cập nhật real-time.

---

## :material-connection: Endpoint

```
GET /api/v1/catalog/events
Content-Type: text/event-stream
```

---

## :material-email-outline: Format Event

```
data: {"revision":43,"changed_source_uris":["file:///path/to/catalog-info.yaml"],"removed_source_uris":[]}

data: {"revision":44,"changed_source_uris":[],"removed_source_uris":["file:///old/catalog-info.yaml"]}
```

| Field | Type | Mô tả |
|---|---|---|
| `revision` | `integer` | Revision mới của `CatalogWorkspace` |
| `changed_source_uris` | `string[]` | URI của document thay đổi |
| `removed_source_uris` | `string[]` | URI của document bị xóa |

---

## :material-strategy: Cách sử dụng

```mermaid
sequenceDiagram
    participant C as Browser Client
    participant S as catalog_http

    C->>S: GET /api/v1/catalog/events
    S->>C: 200 OK (stream mở)
    Note over S: File thay đổi...
    S->>C: data: {"revision":43,...}
    C->>S: GET /api/v1/catalog/topology?root=...
    S->>C: FocusedTopology JSON
```

!!! tip "Metadata only"
    Event payload chỉ chứa metadata (revision + URIs), **không** chứa semantic delta. Client nhận event → **refetch** `CatalogSnapshot` hoặc `FocusedTopology` mới.

---

## :material-link: Đọc thêm

- [Tham chiếu Endpoints](endpoints.md)
- [`CatalogFileWatcher`](../backend/file-watcher.md)

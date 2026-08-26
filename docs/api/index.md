---
title: HTTP API
description: Tổng quan REST API loopback-only của IDP Platform.
---

# :material-api: HTTP API

REST API loopback-only (`127.0.0.1`) phục vụ `TopologyViewer` trên browser. Tất cả endpoint sử dụng `snake_case` theo `openapi.yaml`.

<div class="grid cards" markdown>

-   :material-format-list-bulleted: **Tham chiếu Endpoints**

    Tất cả endpoints với request/response chi tiết.

    [:octicons-arrow-right-24: Endpoints](endpoints.md)

-   :material-code-json: **Data Schemas**

    `CatalogEntity`, `CatalogRelation`, `TopologyNode`, và các schema khác.

    [:octicons-arrow-right-24: Schemas](schemas.md)

-   :material-broadcast: **Server-Sent Events**

    Real-time notifications qua `CatalogChangeFeed`.

    [:octicons-arrow-right-24: SSE Events](events.md)

</div>

---

## :material-server: Tổng quan

| Đặc điểm | Chi tiết |
|---|---|
| **Bind** | `127.0.0.1:8000` (loopback only) |
| **CORS** | Chỉ `VITE_ORIGIN` (mặc định `http://localhost:5173`) |
| **Auth** | Không — loopback-only by design |
| **Contract** | `openapi/openapi.yaml` (OpenAPI 3.1) |
| **Framework** | FastAPI |

## :material-format-list-numbered: Tóm tắt Endpoints

| Method | Path | Mô tả |
|---|---|---|
| `GET` | `/health` | Runtime health + revision |
| `GET` | `/api/v1/catalog/snapshot` | `CatalogSnapshot` đầy đủ |
| `GET` | `/api/v1/catalog/search` | Full-text search qua `CatalogSearchIndex` |
| `GET` | `/api/v1/catalog/suggestions` | Autocomplete suggestions |
| `GET` | `/api/v1/catalog/topology` | `FocusedTopology` one-hop |
| `GET` | `/api/v1/catalog/diagnostics` | `CatalogDiagnostic` hiện tại |
| `GET` | `/api/v1/catalog/events` | SSE stream |
| `GET` | `/api/v1/catalog/source` | Đọc source YAML |
| `POST` | `/api/v1/catalog/completion` | Completion items |
| `GET` | `/api/v1/catalog/relation-targets` | Entity phù hợp cho relation |
| `POST` | `/api/v1/catalog/sync-external` | Sync Supabase external catalog |
| `POST` | `/api/v1/catalog/entities` | Tạo entity external |
| `PUT` | `/api/v1/catalog/entities/{reference}` | Thay thế entity |
| `DELETE` | `/api/v1/catalog/entities/{reference}` | Xóa entity |
| `GET` | `/api/v1/catalog/entities/{reference}/source` | Đọc YAML source entity |
| `PATCH` | `/api/v1/catalog/entities/{reference}/field` | Sửa 1 field entity |
| `POST` | `/api/v1/catalog/entities/{reference}/owners` | Thêm owner |
| `DELETE` | `/api/v1/catalog/entities/{reference}/owners/{index}` | Xóa owner |

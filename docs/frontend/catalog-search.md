---
title: Tìm kiếm Catalog
description: Full-text search và autocomplete qua CatalogSearchIndex.
---

# :material-magnify: Tìm kiếm Catalog

## :material-database-search: `CatalogSearchIndex`

**Backend:** `backend/app/catalog_infra/search_index.py`

`CatalogSearchIndex` sử dụng SQLite FTS5 (Full-Text Search) cho việc tìm kiếm. Index này là derived cache — descriptor files là source of truth.

### Phạm vi tìm kiếm

- Canonical `EntityReference`
- `display_name`, `metadata.title`, `metadata.description`
- `metadata.tags`, `metadata.labels`, `metadata.annotations`
- `spec.type`, `spec.owners`
- Source paths
- `DraftEntity` và `IdentityConflict`

### Lifecycle

1. Xây dựng ban đầu từ `CatalogSnapshot` khi `CatalogRuntime` khởi động
2. Rebuild sau mỗi `CatalogFileWatcher` revision
3. Rebuild khi tạo entity mới qua Supabase
4. Xóa an toàn — tự tạo lại từ `CatalogSnapshot` hiện tại

---

## :material-web: `HttpCatalogClient`

**Frontend:** `frontend/src/catalog/HttpCatalogClient.ts`

Client HTTP gọi `CatalogSearchIndex` qua backend.

| Method | Endpoint | Mô tả |
|---|---|---|
| `search(q, limit)` | `GET /api/v1/catalog/search` | Full-text search |
| `suggestions(q, limit)` | `GET /api/v1/catalog/suggestions` | Autocomplete (mặc định 8 kết quả) |

### Fallback

Khi backend tạm thời không khả dụng, `HttpCatalogClient` có client-side fallback sử dụng cached `CatalogSnapshot`.

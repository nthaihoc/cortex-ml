---
title: Tham chiếu Endpoints
description: Tham chiếu toàn bộ HTTP API endpoints chia theo nhóm chức năng.
---

# :material-format-list-bulleted: Tham chiếu Endpoints

API của IDP Platform sử dụng chuẩn REST (chỉ hoạt động trên loopback `127.0.0.1:8000`). Tất cả dữ liệu truyền nhận dùng định dạng JSON và tuân theo kiểu chữ `snake_case`.

---

## :material-brain: Catalog Core

Các API cốt lõi lấy trạng thái và cấu trúc đồ thị của hệ thống.

### `GET /health` {#health}
**Mô tả:** Kiểm tra trạng thái runtime và thống kê catalog.  
**Response `200 OK`:**
```json
{"status": "ok", "revision": 42, "entity_count": 150, "diagnostic_count": 3}
```

### `GET /api/v1/catalog/snapshot` {#snapshot}
**Mô tả:** Trả về toàn bộ `CatalogSnapshot` in-memory.  
**Response `200 OK`:** Xem [Data Schemas](schemas.md) cho cấu trúc `CatalogSnapshot` chi tiết.

### `GET /api/v1/catalog/topology` {#topology}
**Mô tả:** Trả về one-hop topology (1 cấp độ) xoay quanh một entity gốc.

**Query Parameters:**

| Tham số | Bắt buộc | Kiểu | Mặc định | Mô tả |
|---|:---:|---|---|---|
| `root` | ✅ | `string` | — | Canonical `EntityReference` |
| `direction` | ❌ | `string` | `"both"` | `"incoming"`, `"outgoing"`, hoặc `"both"` |
| `depth` | ❌ | `int` | `1` | Bắt buộc phải là `1` |

**Response `200 OK`:** Trả về đối tượng `FocusedTopology`.  
**Error `422`:** Tham số không hợp lệ (ví dụ: `depth` khác `1`).

### `GET /api/v1/catalog/diagnostics` {#diagnostics}
**Mô tả:** Trả về danh sách tất cả `CatalogDiagnostic` (lỗi, cảnh báo) hiện tại.

---

## :material-magnify: Tìm kiếm & Gợi ý

Nhóm API hỗ trợ full-text search và autocomplete (dựa trên SQLite FTS5).

### `GET /api/v1/catalog/search` {#search}
**Mô tả:** Full-text search tìm kiếm entities.

**Query Parameters:**

| Tham số | Kiểu | Mặc định | Mô tả |
|---|---|---|---|
| `q` | `string` | `""` | Chuỗi từ khóa tìm kiếm |
| `limit` | `int` | `20` | Số lượng kết quả (tối đa 50) |

### `GET /api/v1/catalog/suggestions` {#suggestions}
**Mô tả:** Giống API `/search` nhưng tối ưu cho việc hiển thị dropdown autocomplete (mặc định `limit=8`).

### `GET /api/v1/catalog/relation-targets` {#relation-targets}
**Mô tả:** Tìm entity phù hợp làm đích (target) khi người dùng muốn tạo một Relation mới.

**Query Parameters:**

| Tham số | Kiểu | Mô tả |
|---|---|---|
| `q` | `string` | Chuỗi truy vấn |
| `kinds` | `string[]` | Lọc theo loại entity (VD: `["component", "system"]`) |

### `POST /api/v1/catalog/completion` {#completion}
**Mô tả:** Gợi ý (autocomplete) từ khóa ngay tại vị trí con trỏ (cursor) khi soạn thảo file YAML.

**Request Body:**
```json
{
  "text": "specVersion: vsf-idp.io/v2\n...",
  "offset": 42
}
```
**Response `200 OK`:**
```json
{
  "revision": 42,
  "items": [
    {"label": "service", "detail": "Component type", "insertText": "service", "category": "code"}
  ]
}
```

---

## :material-cloud-sync: External Catalog (Supabase)

Nhóm API quản lý dữ liệu lưu trên Supabase (Cloud). 

### `POST /api/v1/catalog/sync-external` {#sync-external}
**Mô tả:** Kích hoạt pull dữ liệu thủ công từ Supabase về local workspace.  
**Response `200 OK`:** `{"status": "ok", "synced_entities": 50, "synced_relations": 120}`  
**Error `503`:** Supabase chưa được cấu hình.

### `POST /api/v1/catalog/entities` {#create-entity}
**Mô tả:** Tạo một entity external mới từ nội dung YAML.

**Request Body:**
```json
{ "content": "specVersion: vsf-idp.io/v2\n..." }
```
**Error `409`:** Entity đã tồn tại.  
**Error `422`:** Validation YAML không thành công.

### `PUT /api/v1/catalog/entities/{reference}` {#replace-entity}
**Mô tả:** Thay thế toàn bộ descriptor (Cập nhật). Yêu cầu Identity (`kind:namespace/name`) không đổi.

**Request Body:**
```json
{
  "content": "specVersion: vsf-idp.io/v2\n...",
  "expected_version": "2026-08-26T14:00:00Z"
}
```
**Error `404`:** Reference không tồn tại.  
**Error `409`:** Lỗi Optimistic Concurrency (Có người khác đã cập nhật trước).

### `PATCH /api/v1/catalog/entities/{reference}/field` {#field-update}
**Mô tả:** Cập nhật nhanh một trường (scalar field) cụ thể.

**Request Body:**
```json
{
  "field_path": "spec.name",
  "value": "Tên Dịch Vụ Mới",
  "expected_version": "2026-08-26T14:00:00Z"
}
```

### `DELETE /api/v1/catalog/entities/{reference}` {#delete-entity}
**Mô tả:** Xóa một entity trên Supabase.

**Request Body:**
```json
{ "expected_version": "2026-08-26T14:00:00Z" }
```

---

## :material-account-group: Quản lý Owners

Nhóm API con dành riêng cho việc thay đổi danh sách chủ sở hữu (`spec.owners.members`).

### `POST /api/v1/catalog/entities/{reference}/owners` {#add-owner}
**Mô tả:** Thêm một owner mới.

**Request Body:**
```json
{
  "user": "dev@vinsmartfuture.tech",
  "role": "maintainer",
  "expected_version": "2026-08-26T14:00:00Z"
}
```

### `DELETE /api/v1/catalog/entities/{reference}/owners/{owner_index}` {#remove-owner}
**Mô tả:** Xóa một owner dựa theo vị trí (index) của họ trong mảng.

**Request Body:**
```json
{ "expected_version": "2026-08-26T14:00:00Z" }
```
**Error `422`:** Từ chối thao tác nếu việc xóa làm mất đi `techlead` cuối cùng.

---

## :material-file: Files & Events

### `GET /api/v1/catalog/source` {#source}
**Mô tả:** Đọc nội dung UTF-8 của file descriptor nằm trên Local.

**Query Parameters:**

| Tham số | Bắt buộc | Kiểu | Mô tả |
|---|:---:|---|---|
| `relative_path` | ✅ | `string` | Đường dẫn tương đối từ Catalog Root |

### `GET /api/v1/catalog/events` {#events}
**Mô tả:** Mở luồng Server-Sent Events (SSE) để nhận cập nhật tự động (Realtime).

**Response Stream (`text/event-stream`):**
```
data: {"revision": 43, "changed_source_uris": ["file:///..."], "removed_source_uris": []}
```

---

## :material-link: Đọc thêm
- [Data Schemas](schemas.md)
- [Cơ chế SSE Events](events.md)
- [HTTP Runtime Module](../backend/local-catalog.md)

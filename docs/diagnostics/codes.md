---
title: Bảng mã lỗi
description: Danh sách đầy đủ các mã lỗi (stable codes) trong IDP Platform.
---

# :material-format-list-checks: Bảng mã lỗi (Error Codes)

Hệ thống cung cấp mã lỗi tĩnh (`code` string) để dễ phân loại và tự động xử lý.

## :material-code-braces: Lỗi Parse YAML

Phát sinh từ `HardenedYamlParser`. Đều là lỗi **blocking** (`severity: error`).

| Code | Ý nghĩa |
|---|---|
| `YAML_INVALID_UTF8` | File không encode bằng UTF-8. |
| `YAML_SYNTAX_ERROR` | Lỗi cú pháp cơ bản của YAML. |
| `YAML_MULTIPLE_DOCUMENTS` | File chứa nhiều document (có dấu `---`). |
| `YAML_ROOT_NOT_MAPPING` | Gốc của YAML không phải là dict/object. |
| `YAML_ALIAS_UNSUPPORTED` | Cố tình sử dụng YAML aliases (khóa `*` hoặc `&`). |
| `YAML_NON_STRING_KEY` | Key của dict không phải chuỗi. |
| `YAML_DUPLICATE_KEY` | Có key bị trùng lặp trong cùng một object. |
| `YAML_TAG_UNSUPPORTED` | Dùng thẻ YAML custom (như `!!type`). |
| `YAML_TIMESTAMP_UNSUPPORTED` | Khai báo ngày giờ (timestamp bare value) — phải bọc trong chuỗi. |
| `YAML_NON_FINITE_NUMBER` | Sử dụng số vô cực hoặc NaN. |

---

## :material-file-document-outline: Lỗi Validation Schema

Phát sinh từ `CatalogValidationEngine`. Hầu hết là lỗi **blocking** (`severity: error`).

| Code | Ý nghĩa |
|---|---|
| `SCHEMA_MISSING_VERSION` | Thiếu `specVersion` (VSF) hoặc `apiVersion` (Backstage). |
| `SCHEMA_FIELD_REQUIRED` | Thiếu một trường bắt buộc (ví dụ `spec.name`, `metadata.namespace`). |
| `SCHEMA_INVALID_TYPE` | Trường có kiểu dữ liệu sai (ví dụ `spec.id` phải là string, lại truyền mảng). |
| `SCHEMA_INVALID_FORMAT` | Giá trị chuỗi không khớp regex quy định. |
| `SCHEMA_UNSUPPORTED_TYPE` | `spec.type` không nằm trong danh sách hỗ trợ (cho VSF v2). |
| `SCHEMA_OWNER_REQUIRED` | Cấu trúc owners không có ít nhất một `techlead`. |

---

## :material-graph: Lỗi Topology & Reference

Phát sinh trong quá trình Resolve hoặc Projection.

| Code | Severity | Blocking | Ý nghĩa |
|---|---|---|---|
| `REFERENCE_INVALID` | `error` | ✅ Có | Chuỗi reference (vd `spec.topology[].ref`) không đúng định dạng. |
| `TOPOLOGY_SELF_REFERENCE` | `warning` | ❌ Không | Entity đang tạo relation tới chính nó. |
| `REFERENCE_TARGET_NOT_FOUND` | `warning` | ❌ Không | Target reference không tồn tại trong `CatalogSnapshot`. |
| `ENTITY_DUPLICATE_REF` | `error` | ✅ Có | Hai hoặc nhiều file cùng định nghĩa chung một canonical reference (`IdentityConflict`). |

---

## :material-folder: Lỗi Filesystem

| Code | Severity | Ý nghĩa |
|---|---|---|
| `CATALOG_DESCRIPTOR_TOO_LARGE` | `error` | File vượt quá 1MB, bị bỏ qua. |
| `CATALOG_ROOT_NOT_FOUND` | `error` | Thư mục Catalog Root cấu hình không tồn tại. |

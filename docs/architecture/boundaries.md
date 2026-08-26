---
title: Ranh giới Module
description: Quy tắc ràng buộc và trách nhiệm của từng thành phần trong IDP Platform.
---

# :material-fence: Ranh giới Module

Mỗi thành phần có trách nhiệm rõ ràng và ràng buộc tường minh (explicit constraints).

---

## :material-brain: `CatalogWorkspace`

**Module:** `backend/app/catalog_workspace/`

| Ràng buộc | Chi tiết |
|---|---|
| **Lưu trữ** | Hoàn toàn in-memory; không persist |
| **Concurrency** | Single-threaded; caller chịu trách nhiệm serialization |
| **Traversal depth** | Cố định 1 hop (enforce trong `focused_topology()`) |
| **Authority** | Hai document cùng canonical `EntityReference` → `IdentityConflict`; không entity nào thắng |
| **Invariant** | Document chưa bao giờ valid = `DraftEntity`; document valid rồi invalid = giữ last-valid `CatalogEntity` (`Health.error`, `Freshness.stale`) |

---

## :material-folder-outline: Filesystem Adapter

**Module:** `backend/app/catalog_infra/filesystem.py`

| Ràng buộc | Chi tiết |
|---|---|
| **Target files** | Chỉ file có tên chính xác `catalog-info.yaml` |
| **Depth** | Quét đệ quy không giới hạn trong Catalog Root |
| **Loại trừ** | Thư mục ẩn (`.`-prefixed), `node_modules`, `__pycache__`, `.venv` |
| **Symlink** | Không bao giờ follow symlink và junction |
| **Kích thước** | File > 1 MB bị skip, phát sinh `CatalogDiagnostic` `CATALOG_DESCRIPTOR_TOO_LARGE` |

---

## :material-http: `catalog_http`

**Module:** `backend/app/catalog_http/`

| Ràng buộc | Chi tiết |
|---|---|
| **Bind address** | `127.0.0.1` — loopback only, không bao giờ `0.0.0.0` |
| **CORS** | Chỉ chấp nhận `VITE_ORIGIN` (mặc định `http://localhost:5173`) |
| **Authentication** | Không có — loopback-only by design |
| **Source writes** | Chỉ ghi vào file `catalog-info.yaml` đã discovered |
| **Entity writes** | Ghi entity external qua Supabase, validate bằng `CatalogValidationEngine` trước khi lưu |
| **Path traversal** | Ngăn chặn bằng `pathlib.resolve()` + `relative_to()` |
| **Optimistic concurrency** | SHA-256 `expected_version` cho PUT source; `updated_at` cho entity writes |
| **Kích thước** | PUT request > 1 MB → `413` |

---

## :material-language-python: `catalog_language_server`

**Module:** `backend/app/catalog_language_server/`

| Ràng buộc | Chi tiết |
|---|---|
| **Transport** | `stdio` — không mở network port |
| **Scope** | Một `CatalogScope` cho mỗi `CatalogLanguageServer` instance |
| **Document types** | Chỉ file `catalog-info.yaml` trong workspace folders |
| **Unsaved overlays** | Áp dụng sau 300 ms debounce; phiên bản cũ bị discard |
| **Depth** | Cố định `depth=1` cho topology requests |
| **Folder management** | Phản hồi `workspace/didChangeWorkspaceFolders` động |

---

## :material-microsoft-visual-studio-code: VS Code Extension

**Module:** `vscode-extension/src/`

| Ràng buộc | Chi tiết |
|---|---|
| **Catalog rules** | Extension **không** implement bất kỳ quy tắc validation nào |
| **Active editor follow** | Cập nhật focus khi editor thay đổi, trừ khi đang "pinned" |
| **Pin state** | Người dùng kiểm soát; ngăn tự động thay đổi focus |
| **Request cancellation** | Topology request cũ bị cancel khi có request mới |
| **Message validation** | Webview message được validate trước khi xử lý |
| **Trusted workspaces** | **Không** hỗ trợ untrusted workspace |

---

## :material-react: Frontend (React)

**Module:** `frontend/src/`

| Ràng buộc | Chi tiết |
|---|---|
| **Catalog rules** | Frontend **không** implement validation rules |
| **Graph scope** | `TopologyViewer` chỉ mount node từ `FocusedTopology` response |
| **Search** | `HttpCatalogClient` gọi `CatalogSearchIndex` qua backend; có client fallback cho transient failures |
| **Navigation** | Click node liên quan → đặt node đó làm root mới |
| **Real-time** | SSE-driven refetch qua `CatalogChangeFeed`; không áp dụng semantic delta |

---

## :material-database-search: `CatalogSearchIndex`

**Module:** `backend/app/catalog_infra/search_index.py`

| Ràng buộc | Chi tiết |
|---|---|
| **Database** | SQLite với FTS5; không cần database server |
| **Authority** | Chỉ là derived cache; descriptor files là source of truth |
| **Phạm vi tìm kiếm** | Canonical reference, tất cả descriptor fields, source paths, `DraftEntity`, `IdentityConflict` |
| **Đồng bộ** | Rebuild sau startup, sau mỗi `CatalogFileWatcher` revision, và khi tạo entity mới |
| **Lifecycle** | Xóa an toàn; tự tạo lại từ `CatalogSnapshot` hiện tại |

---

## :material-transfer: Quy ước đặt tên qua ranh giới

| Ranh giới | Quy ước | Ví dụ |
|---|---|---|
| Python internal | `snake_case` | `entity_ref`, `source_uri` |
| HTTP API (`openapi.yaml`) | `snake_case` | `entity_count`, `relative_path` |
| Custom LSP methods | `camelCase` | `catalogRevision`, `changedDocumentUri` |
| Webview protocol | `camelCase` | `displayName`, `relationType` |

!!! info "Explicit mapper"
    `CatalogLanguageService` trong `service.py` chuyển đổi tường minh giữa Python `snake_case` và LSP `camelCase`. Contract fixtures trong `contracts/examples/` kiểm thử các chuyển đổi này.

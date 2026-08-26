---
title: Khởi chạy nhanh
description: Từ fresh clone tới trình duyệt hiển thị topology trong dưới 5 phút.
---

# :material-play-circle-outline: Khởi chạy nhanh

## Bước 1 — Chạy Backend

```bash
cd idp-platform/backend
source .venv/bin/activate
python -m app.catalog_http
```

`CatalogRuntime` sẽ:

1. Tạo `CatalogWorkspace` với `CatalogScope` từ biến môi trường `CATALOG_ROOT`
2. Khởi động `CatalogFileWatcher` để quét và theo dõi tất cả file `catalog-info.yaml`
3. Xây dựng `CatalogSearchIndex` (SQLite FTS5) từ `CatalogSnapshot` ban đầu
4. Bind FastAPI lên `http://127.0.0.1:8000`

Kiểm tra:

```bash
curl http://127.0.0.1:8000/health
# → {"status":"ok","revision":1,"entity_count":0,"diagnostic_count":0}
```

---

## Bước 2 — Chạy Frontend

```bash
cd idp-platform/frontend
npm run dev
```

Mở trình duyệt tại `http://localhost:5173`. `TopologyViewer` sẽ hiển thị focused topology từ `CatalogSnapshot`.

---

## Bước 3 — Tạo file descriptor thử nghiệm

Tạo file `catalog-info.yaml` trong Catalog Root:

```yaml
specVersion: vsf-idp.io/v2
metadata:
  domain: "Platform Engineering"
  system: platform
  namespace: platform
spec:
  type: service
  id: payment-gateway
  name: Payment Gateway Service
  owners:
    members:
      - user: dev@vinsmartfuture.tech
        role: techlead
```

`CatalogFileWatcher` sẽ phát hiện file mới → `CatalogWorkspace` xử lý qua ingest pipeline → `CatalogChangeFeed` gửi SSE event → `TopologyViewer` tự động cập nhật.

---

## Bước 4 — Mở VS Code (tuỳ chọn)

```bash
code idp-platform/
```

Nếu đã cài extension, `CatalogLanguageServer` sẽ khởi động qua stdio khi mở file `catalog-info.yaml`. Editor hiển thị:

- **Diagnostics** inline (lỗi validation, `CatalogDiagnostic`)
- **Completion** cho field names, entity references, `spec.type`
- **Topology webview** ở sidebar (lệnh `Catalog: Open Topology Sidebar`)

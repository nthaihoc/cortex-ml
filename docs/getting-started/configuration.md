---
title: Cấu hình
description: Biến môi trường và tuỳ chỉnh cho IDP Platform.
---

# :material-cog-outline: Cấu hình

## :material-variable: Biến môi trường

### Backend (`catalog_http`)

| Biến | Bắt buộc | Mặc định | Mô tả |
|---|---|---|---|
| `CATALOG_ROOT` | Có | `.` | Đường dẫn tuyệt đối hoặc tương đối tới Catalog Root |
| `HOST` | Không | `127.0.0.1` | Bind address — luôn là loopback |
| `PORT` | Không | `8000` | Cổng HTTP |
| `VITE_ORIGIN` | Không | `http://localhost:5173` | Origin cho CORS |

### Supabase (tuỳ chọn)

| Biến | Bắt buộc | Mô tả |
|---|---|---|
| `SUPABASE_URL` | Có* | URL dự án Supabase |
| `SUPABASE_ANON_KEY` | Có* | Anon key cho Supabase |

_* Chỉ bắt buộc khi sử dụng external catalog._

### VS Code Extension

| Cài đặt | Mặc định | Mô tả |
|---|---|---|
| `catalogTopology.pythonPath` | `""` (auto-detect) | Đường dẫn Python executable. Khi trống, extension tìm `.venv` cùng cấp rồi fallback về `python` trên PATH |
| `catalogTopology.serverWorkingDirectory` | `""` (auto-detect) | Working directory cho `CatalogLanguageServer`. Mặc định là thư mục `backend/` cùng cấp |

---

## :material-file-cog-outline: File `.env`

Tất cả biến môi trường có thể đặt trong file `.env` ở thư mục `idp-platform/`:

```env
CATALOG_ROOT=/path/to/your/catalog
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
```

`CatalogRuntime` tự động đọc file `.env` qua `python-dotenv` khi khởi động.

---

## :material-shield-lock-outline: Bảo mật

| Quy tắc | Chi tiết |
|---|---|
| **Bind address** | Luôn là `127.0.0.1` — không bao giờ `0.0.0.0` |
| **CORS** | Chỉ chấp nhận origin từ `VITE_ORIGIN` |
| **Authentication** | Không có — loopback-only by design |
| **Source writes** | Chỉ ghi vào file `catalog-info.yaml` đã discovered trong Catalog Root |
| **Path traversal** | Ngăn chặn bằng `pathlib.resolve()` + `relative_to()` check |

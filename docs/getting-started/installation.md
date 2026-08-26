---
title: Hướng dẫn cài đặt
description: Từng bước cài đặt backend, frontend, và VS Code Extension.
---

# :material-download-circle-outline: Hướng dẫn cài đặt

## :material-numeric-1-circle: Clone repository

```bash
git clone https://github.com/truongabc-group1/idp.git
cd idp/idp-platform
```

---

## :material-numeric-2-circle: Backend

```bash
cd backend

# Tạo virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows

# Cài đặt dependency
pip install -r requirements.txt

# (Tuỳ chọn) Cài đặt dev tools
pip install -r requirements-dev.txt
```

### Cấu trúc sau cài đặt

```
backend/
├── .venv/                 # Virtual environment
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Dev + test dependencies
├── pyproject.toml
└── app/                   # Source code
    ├── catalog_workspace/
    ├── catalog_http/
    ├── catalog_language_server/
    └── ...
```

---

## :material-numeric-3-circle: Frontend

```bash
cd frontend

npm install
```

Frontend sử dụng Vite với React 19 và ReactFlow 11. Xem [`package.json`](https://github.com/truongabc-group1/idp/blob/main/idp-platform/frontend/package.json) cho danh sách dependency đầy đủ.

---

## :material-numeric-4-circle: VS Code Extension (tuỳ chọn)

```bash
cd vscode-extension

npm install
npm run build
```

Sau khi build, mở VS Code trong thư mục workspace chứa file `catalog-info.yaml` — extension sẽ tự kích hoạt.

!!! tip "Cài extension vào VS Code"
    Dùng lệnh sau để đóng gói và cài đặt:
    ```bash
    npx @vscode/vsce package --no-dependencies
    code --install-extension local-catalog-topology-vscode-0.1.0.vsix
    ```

---

## :material-numeric-5-circle: Cấu hình Supabase (tuỳ chọn)

Nếu cần tích hợp external catalog qua Supabase:

```bash
# Tạo file .env từ template
cp .env.example .env
```

Chỉnh sửa `.env`:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
```

!!! warning "Không bắt buộc"
    Nếu không cấu hình Supabase, hệ thống vẫn hoạt động bình thường với local catalog. Các endpoint liên quan tới external catalog sẽ trả về `503`.

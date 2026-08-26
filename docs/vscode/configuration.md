---
title: Cấu hình
description: Các tuỳ chỉnh settings.json cho extension.
---

# :material-cog: Cấu hình (Settings)

Extension có thể được cấu hình qua giao diện Settings của VS Code (`Ctrl+,` / `Cmd+,`) hoặc trực tiếp trong `.vscode/settings.json`.

## Các tham số cấu hình

| Cài đặt | Mặc định | Mô tả |
|---|---|---|
| `catalogTopology.pythonPath` | `""` | Đường dẫn tuyệt đối tới Python executable dùng để chạy LSP server. Nếu để trống, extension sẽ thử tìm `.venv` ở cùng cấp thư mục workspace, hoặc rơi về lệnh `python` trên PATH. |
| `catalogTopology.serverWorkingDirectory` | `""` | Thư mục làm việc (working directory) cho server. Nếu để trống, extension sẽ tự động tính toán (mặc định trỏ về thư mục `backend/` chứa mã nguồn Python). |

### Ví dụ `settings.json`

```json
{
  "catalogTopology.pythonPath": "/Users/me/workspace/idp/backend/.venv/bin/python",
  "catalogTopology.serverWorkingDirectory": "/Users/me/workspace/idp/backend"
}
```

!!! warning "Trusted Workspace"
    Extension này chạy một tiến trình Python bên dưới, do đó nó **yêu cầu** VS Code Workspace hiện tại phải là "Trusted". Extension sẽ không hoạt động trong chế độ Restricted Mode.

---
title: Các lệnh
description: Danh sách command (Command Palette) của extension.
---

# :material-console-line: Các lệnh (Commands)

Tất cả các lệnh của extension có thể được truy cập thông qua **Command Palette** (`Ctrl+Shift+P` / `Cmd+Shift+P`).

## Danh sách Lệnh

| Tên lệnh | Command ID | Chức năng |
|---|---|---|
| **Catalog: Open Topology Sidebar** | `catalogTopology.openSidebar` | Mở/focus vào Webview sidebar hiển thị biểu đồ topology tương tác. Biểu đồ sẽ thay đổi theo file `catalog-info.yaml` đang active. |
| **Catalog: Restart Server** | `catalogTopology.restartServer` | Khởi động lại tiến trình Python chạy `CatalogLanguageServer`. Hữu ích nếu server gặp lỗi hoặc bạn vừa cập nhật Python environment. |

!!! tip "Trạng thái Pin (Ghim)"
    Khi mở Topology Sidebar, bạn có một nút "Pin" (ghim). 
    - Nếu **không ghim**, sidebar sẽ tự động thay đổi nội dung (refetch topology) khi bạn chuyển sang chỉnh sửa file `catalog-info.yaml` khác.
    - Nếu **đã ghim**, sidebar sẽ đứng im với entity hiện tại dù bạn mở file nào.

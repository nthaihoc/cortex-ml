---
title: VS Code Extension
description: Tổng quan extension VS Code cho IDP Platform.
---

# :material-microsoft-visual-studio-code: VS Code Extension

Extension VS Code cung cấp live validation và one-hop topology preview trực tiếp trong editor, chạy `CatalogLanguageServer` qua giao thức stdio.

<div class="grid cards" markdown>

-   :material-download: **Cài đặt**

    Đóng gói và cài đặt extension vào VS Code.

    [:octicons-arrow-right-24: Cài đặt](installation.md)

-   :material-console-line: **Các lệnh**

    Danh sách lệnh VS Code (`Catalog: ...`).

    [:octicons-arrow-right-24: Lệnh](commands.md)

-   :material-cog: **Cấu hình**

    Thiết lập Python path, working directory.

    [:octicons-arrow-right-24: Cấu hình](configuration.md)

-   :material-api: **Giao thức Webview**

    Message passing giữa Extension Host và Webview React app.

    [:octicons-arrow-right-24: Webview Protocol](webview-protocol.md)

</div>

---

## :material-star: Tính năng

-   **Diagnostics**: Hiển thị lỗi validation ngay lập tức khi soạn thảo.
-   **Autocomplete**: Gợi ý các trường, `spec.type`, `EntityReference` cho mục topology.
-   **Topology Webview**: Sidebar hiển thị biểu đồ quan hệ 1-hop tương tác trực tiếp với editor hiện tại (ReactFlow).
-   **Debounce**: Xử lý mượt mà khi gõ, không cần lưu file mới thấy lỗi.
-   **Tự động nhận diện Workspace**: Tự động phát hiện `.venv` hoặc python path, theo dõi folder root.

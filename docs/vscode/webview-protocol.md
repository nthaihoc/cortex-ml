---
title: Giao thức Webview
description: Định dạng message trao đổi giữa Webview và Extension Host.
---

# :material-api: Giao thức Webview

VS Code Extension hiển thị đồ thị qua một Webview sidebar. Vì webview chạy trong môi trường sandbox riêng, nó giao tiếp với Extension Host (nơi giữ kết nối tới LSP server) thông qua cơ chế Message Passing.

Tất cả message sử dụng kiểu `camelCase`.

## :material-arrow-right: Từ Webview tới Extension (Requests)

Khi webview cần hành động, nó gọi `vscode.postMessage(msg)`:

### `fetchTopology`

Yêu cầu lấy topology mới nhất (thường gửi khi webview vừa load xong).

```json
{ "command": "fetchTopology" }
```

### `changeRoot`

Yêu cầu đổi root entity. Gửi khi user click vào một node trên biểu đồ.

```json
{ "command": "changeRoot", "reference": "component:platform/auth-service" }
```

### `openDocument`

Yêu cầu mở file tương ứng với entity reference trong trình soạn thảo.

```json
{ "command": "openDocument", "reference": "component:platform/auth-service" }
```

### `log`

Ghi log từ React webview vào Output panel của extension.

```json
{ "command": "log", "message": "Component mounted" }
```

---

## :material-arrow-left: Từ Extension tới Webview (Events)

Extension Host gửi dữ liệu vào Webview thông qua `webview.postMessage(msg)`:

### `updateTopology`

Cập nhật biểu đồ mới. Kích hoạt khi có dữ liệu từ LSP method `catalog/topologyForDocument` hoặc trả lời cho `changeRoot`.

```json
{
  "command": "updateTopology",
  "topology": {
    "root": "component:platform/payment-gateway",
    "direction": "both",
    "depth": 1,
    "nodes": { ... },
    "relations": [ ... ]
  }
}
```

### `pinStateChanged`

Báo cho Webview biết trạng thái Pin (ghim) đã thay đổi (người dùng bấm nút Pin trên header của view).

```json
{
  "command": "pinStateChanged",
  "isPinned": true
}
```

---

## :material-shield-check: Validation

Cả Webview và Extension Host đều validate thông điệp nhận được để tránh lỗi runtime (VD: thiếu field, sai type). Extension kiểm tra type safety cho mọi payload đến từ webview.

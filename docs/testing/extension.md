---
title: Extension Tests
description: Hướng dẫn chạy integration test trên VS Code Extension.
---

# :material-microsoft-visual-studio-code: Extension Tests

Môi trường extension khá phức tạp để test vì nó đòi hỏi khởi chạy cả một VS Code Headless instance.

## Chạy test (Integration)

```bash
cd vscode-extension
npm run test
```

Lệnh này sẽ tự động tải bản `vscode-test`, mở instance và chạy chuỗi test được định nghĩa trong `src/test/suite/`.

## Phạm vi kiểm thử

- **Activation**: Extension có thể activate thành công khi mở `catalog-info.yaml` không.
- **LSP Connection**: Extension Host có thiết lập thành công stdio communication tới Python backend không.
- **Webview Message**: Mock messages gửi qua lại và nhận assert output.

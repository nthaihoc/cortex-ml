---
title: Giao thức LSP
description: Standard LSP lifecycle events của CatalogLanguageServer.
---

# :material-protocol: Giao thức LSP

`CatalogLanguageServer` triển khai standard LSP lifecycle events để duy trì workspace state và cung cấp diagnostics.

---

## :material-power: `initialize`

Khi VS Code Extension khởi tạo `CatalogLanguageServer`:

- Tạo `CatalogWorkspace` bao gồm tất cả workspace folders trong một `CatalogScope`
- Discover và load tất cả file `catalog-info.yaml`
- Publish diagnostics ban đầu cho tất cả document đã load

---

## :material-folder-multiple: `workspace/didChangeWorkspaceFolders`

- **Folder thêm:** Discover, load, cập nhật scope
- **Folder xóa:** Remove document, cập nhật scope
- Gửi `catalog/revisionChanged` notification sau mỗi thay đổi

---

## :material-file-plus: `textDocument/didOpen`

- Đăng ký document trong open-documents map
- Lên lịch debounced analysis (300 ms)
- Chỉ xử lý file `catalog-info.yaml` trong workspace roots

---

## :material-file-edit: `textDocument/didChange`

- Cập nhật in-memory buffer với text mới nhất
- Lên lịch debounced analysis
- Bỏ qua thay đổi có version cũ hơn (lower version)

---

## :material-content-save: `textDocument/didSave`

- Cập nhật in-memory buffer với nội dung đã lưu
- Re-schedule analysis
- Thêm document URI vào root's known sources

---

## :material-file-remove: `textDocument/didClose`

- Xóa in-memory overlay
- Reload file on-disk và re-upsert vào `CatalogWorkspace`
- Nếu file không còn tồn tại → remove document
- Publish diagnostics clearing unsaved version

---

## :material-stethoscope: `textDocument/publishDiagnostics`

Sau mỗi document change, `CatalogLanguageService` publish diagnostics cho **tất cả document bị ảnh hưởng**:

```json
{
  "method": "textDocument/publishDiagnostics",
  "params": {
    "uri": "file:///path/to/catalog-info.yaml",
    "version": 5,
    "diagnostics": [{
      "range": {"start": {"line": 10, "character": 2}, "end": {"line": 10, "character": 2}},
      "severity": 1,
      "code": "SCHEMA_FIELD_REQUIRED",
      "source": "local-catalog",
      "message": "spec.owners.members requires at least one techlead"
    }]
  }
}
```

| LSP Severity | Mô tả |
|---|---|
| `1` (Error) | Blocking `CatalogDiagnostic` |
| `2` (Warning) | Non-blocking `CatalogDiagnostic` |

---

## :material-lightbulb-on: `textDocument/completion`

Completion cho file `catalog-info.yaml` đang soạn, context-aware:

- Field keys cho VSF IDP v2 và Backstage
- Giá trị cố định: `spec.type`, owner `role`, `specVersion`, `kind`
- Giá trị từ catalog: namespaces, systems, domains, `EntityReference` cho relation fields

---

## :material-link: Đọc thêm

- [Custom Methods](custom-methods.md)
- [LSP Specification — Lifecycle](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#lifeCycleMessages)

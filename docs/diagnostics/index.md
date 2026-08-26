---
title: Diagnostics
description: Tổng quan hệ thống thông báo lỗi và cảnh báo (Diagnostics) của IDP Platform.
---

# :material-stethoscope: Diagnostics

Hệ thống diagnostics của IDP Platform cung cấp các báo cáo chi tiết về lỗi syntax, lỗi schema, và lỗi topology. Những diagnostic này được dùng chung cho HTTP API và giao thức LSP trong VS Code.

<div class="grid cards" markdown>

-   :material-format-list-checks: **Bảng mã lỗi**

    Danh sách các mã lỗi ổn định (stable codes) và nguyên nhân.

    [:octicons-arrow-right-24: Bảng mã lỗi](codes.md)

-   :material-alert-circle-outline: **Hướng dẫn mức độ (Severity)**

    Phân loại mức độ lỗi: Error vs Warning.

    [:octicons-arrow-right-24: Mức độ lỗi](severity.md)

</div>

---

## Cấu trúc `CatalogDiagnostic`

Mỗi lỗi được thể hiện dưới dạng model `CatalogDiagnostic`:

```json
{
  "code": "SCHEMA_FIELD_REQUIRED",
  "severity": "error",
  "blocking": true,
  "message": "spec.id is required",
  "provenance": {
    "source_uri": "file:///path/to/catalog-info.yaml",
    "relative_path": "service/catalog-info.yaml",
    "document_version": "hash...",
    "field_path": "spec"
  },
  "entity_ref": null,
  "target_ref": null,
  "suggested_action": "Add the 'id' field under 'spec'",
  "details": null
}
```

- **`code`**: Chuỗi định danh cố định, giúp tool tự động xử lý.
- **`blocking`**: Nếu là `true`, lỗi này ngăn cản việc tạo ra entity. Descriptor sẽ bị rơi vào trạng thái `DRAFT` hoặc giữ last-valid state.
- **`provenance`**: Chứa `field_path` (ví dụ `spec.topology[0].ref`) giúp frontend hoặc editor highlight chính xác dòng lỗi.

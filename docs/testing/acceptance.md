---
title: Phạm vi chấp nhận
description: Các tiêu chí chấp nhận (Acceptance Criteria).
---

# :material-checkbox-marked-circle-outline: Phạm vi chấp nhận (Acceptance)

Bất kỳ thay đổi lớn (PR) nào vào hệ thống đều phải vượt qua bộ Acceptance Criteria sau:

| STT | Core Scenario | Kết quả kỳ vọng |
|---|---|---|
| 1 | Mở VS Code vào thư mục trống. Tạo file YAML v2. Gõ sai `spec.type`. | LSP Diagnostic hiện ngay lỗi sau 300ms. Lỗi là `SCHEMA_UNSUPPORTED_TYPE`. |
| 2 | Sửa `spec.type` lại cho đúng, gõ tiếp relation trỏ tới `component:a/b`. | Lỗi cũ mất đi. Báo cảnh báo (Warning) `REFERENCE_TARGET_NOT_FOUND`. |
| 3 | Mở web browser `TopologyViewer`. Tạo file YAML mới trên disk. | Browser tự động thêm node mới lên biểu đồ mà không cần user refresh trang. |
| 4 | Copy paste 1 file YAML làm hai bản (Xung đột định danh). | Graph đỏ lên, báo Conflict. Extension hiện 2 errors vào cả 2 file copy. |
| 5 | Gửi PUT API (sửa Entity) kèm `expected_version` cũ (đã có request ghi trước đó). | Server từ chối, trả về HTTP 409 (Optimistic concurrency). |

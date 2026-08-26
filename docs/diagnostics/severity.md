---
title: Hướng dẫn mức độ
description: Sự khác biệt giữa Error và Warning trong hệ thống Diagnostics.
---

# :material-alert-circle-outline: Hướng dẫn mức độ (Severity)

Trường `severity` trong `CatalogDiagnostic` chỉ định mức độ nghiêm trọng của vấn đề, ảnh hưởng trực tiếp đến trạng thái của entity.

## :material-close-circle: Error (Lỗi)

Mức độ `error` báo hiệu một lỗi vi phạm nghiêm trọng (syntax, schema, danh tính).

- Lỗi parse YAML.
- Lỗi thiếu trường bắt buộc (`spec.id`, `metadata.domain`).
- Lỗi cấu trúc sai (`spec` không phải object).
- Lỗi trùng lặp danh tính (`IdentityConflict`).

**Tác động:**
- Hầu hết `error` đi kèm với cờ `blocking = true`.
- Nếu file đang tạo entity lần đầu: Entity không thể hình thành, được xếp vào `DraftEntity`. (Frontend hiển thị màu xám).
- Nếu file đang cập nhật entity hợp lệ cũ: Hệ thống từ chối cập nhật, giữ nguyên dữ liệu cuối cùng hợp lệ ("last-valid state") và đánh dấu entity thành `Health.error`, `Freshness.stale`. (Frontend hiển thị nét đứt màu đỏ).

---

## :material-alert: Warning (Cảnh báo)

Mức độ `warning` báo hiệu dữ liệu vẫn hợp lệ để hệ thống hiểu, nhưng có yếu tố bất thường về mặt logic hoặc nghiệp vụ.

- **`REFERENCE_TARGET_NOT_FOUND`**: Entity khai báo gọi tới `component:platform/unknown`, nhưng không file nào chứa entity đó.
- **`TOPOLOGY_SELF_REFERENCE`**: Entity khai báo gọi tới chính nó.

**Tác động:**
- Cờ `blocking = false`.
- Entity vẫn được cập nhật bình thường vào `CatalogSnapshot`.
- Entity sẽ có trạng thái `Health.warning`, `Freshness.current`. (Frontend hiển thị viền liền màu vàng).
- Các relation "khuyết" (target not found) vẫn được đưa vào đồ thị nhưng nút mục tiêu hiển thị màu xám (`TopologyNodeState.unresolved`).

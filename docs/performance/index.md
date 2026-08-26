---
title: Hiệu năng
description: Tổng quan về hiệu năng xử lý (Performance) của IDP Platform.
---

# :material-gauge: Hiệu năng

Mục tiêu thiết kế của phần backend IDP Platform là tốc độ — phải đủ nhanh để cập nhật realtime cho trình duyệt và LSP client mà không bị "giật" (stutter).

<div class="grid cards" markdown>

-   :material-arrow-expand-all: **Khả năng mở rộng (Scalability)**

    Cách hệ thống xử lý bộ dataset khổng lồ.

    [:octicons-arrow-right-24: Scalability](scalability.md)

</div>

---

## Thiết kế hướng hiệu năng

1. **In-memory store:** Trạng thái hệ thống hoàn toàn chứa trong memory. `CatalogWorkspace` không có độ trễ network hay disk I/O khi duyệt topology.
2. **One-hop traversal:** Frontend không request toàn bộ đồ thị. API `/topology` giới hạn nghiêm ngặt `depth=1` giúp thời gian query là $O(E)$ cục bộ (số edge liên quan), độc lập với tổng size đồ thị.
3. **Hardened Parser:** Không dùng thư viện YAML tổng quát chậm chạp, mà sử dụng parser tối giản (subset) bỏ đi các tính năng nặng (alias, custom type).
4. **FTS SQLite:** Tìm kiếm full-text giao phó cho SQLite FTS5 (compiled C extension) chạy in-memory thay vì loop qua dict Python.

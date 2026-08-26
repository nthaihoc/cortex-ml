---
title: Quy ước Code
description: Quy chuẩn coding và đặt tên bắt buộc trong mã nguồn.
---

# :material-format-title: Quy ước Code (Conventions)

## 1. Naming Convention (Thuật ngữ)

Đây là quy tắc **RẤT QUAN TRỌNG**. Hãy xem bảng chi tiết tại [Bảng Quy ước tên](https://nthoc.github.io/idp/architecture/). Một số điều bắt buộc:

- **Tên Class Backend:** Luôn có tiền tố chỉ domain nếu cần. Sử dụng `CatalogWorkspace`, `CatalogValidationEngine`. (Tuyệt đối không viết tắt thành `Workspace` hay `Engine`).
- **Python Variables:** `snake_case`. (Ví dụ: `entity_ref`).
- **LSP Methods & REST Fields:** `camelCase` hoặc `snake_case` phải đồng nhất đúng theo OpenAPI (Tham chiếu file `openapi.yaml`).

## 2. Python (Backend)

- Format: `black` và `ruff`. (Chạy lệnh `ruff check . --fix`).
- Type Hints: 100% bắt buộc. `mypy --strict` phải pass. (Không dùng `Any` nếu không thật sự cần).
- Docstring: Cho tất cả các public method của các lớp quan trọng (`CatalogWorkspace`).

## 3. TypeScript (Frontend & VS Code)

- Format: `Prettier`.
- Dùng `interface` hoặc `type` rõ ràng, không xài lạm dụng `any`.
- Tránh logic nghiệp vụ trong React UI component. Đẩy logic về `CatalogProvider` hoặc custom hooks.

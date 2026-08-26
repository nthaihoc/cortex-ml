---
title: Quy trình phát triển
description: Workflow đóng góp code (PR, CI).
---

# :material-source-branch: Quy trình phát triển

Dự án áp dụng mô hình Pull Request (PR) chuẩn trên GitHub.

## 1. Mở Issue (Nếu là Feature/Bug lớn)

Vui lòng thảo luận trước khi viết code cho một tính năng lớn bằng cách mở Issue. Các thay đổi liên quan đến cấu trúc `NormalizedDescriptor` hoặc API thay đổi phải có Issue thảo luận.

## 2. Rẽ nhánh (Branching)

- Checkout branch mới từ nhánh `main`.
- Đặt tên branch: `feat/<tên-ngắn>` hoặc `fix/<tên-ngắn>` hoặc `docs/<tên-ngắn>`.

## 3. Commit

- Cố gắng giữ cho commit nhỏ và ý nghĩa (atomic commit).
- Message viết bằng Tiếng Anh, khuyến khích theo chuẩn [Conventional Commits](https://www.conventionalcommits.org/).

## 4. Pull Request

Tạo PR vào nhánh `main`. CI sẽ tự động chạy:
- Python `pytest`
- Typescript `npm run test`
- Code formatter `ruff`, `black`

Yêu cầu ít nhất 1 thành viên core (techlead) Review và Approve.

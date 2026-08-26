---
title: Yêu cầu hệ thống
description: Phiên bản phần mềm cần cài đặt trước khi chạy IDP Platform.
---

# :material-check-circle-outline: Yêu cầu hệ thống

## :material-language-python: Backend

| Phần mềm | Phiên bản tối thiểu | Ghi chú |
|---|---|---|
| Python | 3.12+ | Dùng cho `CatalogWorkspace`, `CatalogValidationEngine`, và toàn bộ backend |
| pip | 23+ | Quản lý dependency |

## :material-nodejs: Frontend

| Phần mềm | Phiên bản tối thiểu | Ghi chú |
|---|---|---|
| Node.js | 20 LTS+ | Chạy Vite dev server |
| npm | 10+ | Quản lý dependency |

## :material-microsoft-visual-studio-code: VS Code Extension

| Phần mềm | Phiên bản tối thiểu | Ghi chú |
|---|---|---|
| VS Code | 1.91+ | Host cho extension |
| Node.js | 20 LTS+ | Build extension |

## :material-cloud-outline: Tích hợp Supabase (tuỳ chọn)

Cần thiết khi muốn sử dụng external catalog:

| Phần mềm | Mô tả |
|---|---|
| Supabase Project | URL và Anon Key cấu hình qua `.env` |

!!! note "Hệ điều hành"
    IDP Platform hỗ trợ macOS, Linux, và Windows (WSL2). File discovery sử dụng `watchfiles` và `pathlib`, tương thích đa nền tảng.

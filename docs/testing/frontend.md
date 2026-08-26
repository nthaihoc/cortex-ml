---
title: Frontend Tests
description: Kiểm thử các React Component.
---

# :material-react: Frontend Tests

Frontend sử dụng `Vitest` làm test runner và `React Testing Library` để kiểm tra behavior của component.

## Cách chạy

```bash
cd frontend
npm run test
```

## Phạm vi (Scope)

Các test tập trung vào:

1. **`HttpCatalogClient`**: Mock API (fetch) để đảm bảo client gửi request đúng, URL encode đúng.
2. **`TopologyViewer`**: Đảm bảo component mount đúng, render đúng các `TopologyNode` màu đỏ/xanh/vàng tương ứng với các trạng thái mock từ HTTP.
3. **`catalogSearch.ts`**: Kiểm tra tính năng debounce.

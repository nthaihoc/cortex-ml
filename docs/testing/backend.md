---
title: Backend Tests
description: Cấu trúc test và lệnh chạy cho Python backend.
---

# :material-language-python: Backend Tests

## Cấu trúc thư mục

```
backend/tests/
├── unit/
│   ├── test_workspace.py
│   ├── test_validation_engine.py
│   └── test_parser.py
├── integration/
│   ├── test_http_api.py
│   └── test_language_server.py
└── fixtures/
    └── catalog_samples/
```

## Cách chạy test

Chạy toàn bộ bằng pytest:

```bash
cd backend
pytest
```

Chạy với coverage:

```bash
pytest --cov=app --cov-report=html
```

## Contract Testing

Thư mục `contracts/examples/` ở thư mục gốc chứa các file JSON chuẩn (`CatalogSnapshot`, `FocusedTopology`) để frontend và backend có thể test chung một định dạng mà không phụ thuộc lẫn nhau.

Backend tự động test chống lại các JSON fixtures này trong `test_contracts.py`.

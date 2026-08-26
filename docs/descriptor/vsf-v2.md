---
title: VSF IDP v2
description: Định dạng descriptor VSF IDP v2 — cấu trúc, trường bắt buộc, và ví dụ.
---

# :material-new-box: VSF IDP v2

Định dạng chính được sử dụng trong IDP Platform, nhận diện bằng `specVersion: vsf-idp.io/v2`.

---

## :material-file-document-outline: Cấu trúc đầy đủ

```yaml
specVersion: vsf-idp.io/v2

metadata:
  domain: "Platform Engineering"     # Bắt buộc, ≤ 128 ký tự
  system: platform                   # Bắt buộc, ^[a-z][a-z0-9-]*$
  namespace: platform                # Bắt buộc, ^[a-z][a-z0-9-]*$

spec:
  type: service                      # Bắt buộc, xem danh sách bên dưới
  id: payment-gateway                # Bắt buộc, ^[a-z][a-z0-9-]*$
  name: Payment Gateway Service      # Bắt buộc, không ký tự điều khiển

  owners:                            # Tuỳ chọn
    members:
      - user: dev@vinsmartfuture.tech
        role: techlead               # techlead | maintainer | member

  review:                            # Bắt buộc cho service/gateway
    branch: main

  topology:                          # Tuỳ chọn
    - ref: "component:platform/auth-service"
      protocol: gRPC
      reason: Token validation
```

---

## :material-format-list-checks: Trường bắt buộc

| Trường | Quy tắc | Mô tả |
|---|---|---|
| `specVersion` | Chính xác `"vsf-idp.io/v2"` | Nhận diện format |
| `metadata.domain` | ≤ 128 ký tự in được | Tên domain nghiệp vụ |
| `metadata.system` | Khớp `^[a-z][a-z0-9-]*$`, phải tồn tại trong catalog | System thuộc về |
| `metadata.namespace` | Khớp `^[a-z][a-z0-9-]*$` | Namespace phân nhóm |
| `spec.type` | Một trong danh sách hỗ trợ | Loại component |
| `spec.id` | Khớp `^[a-z][a-z0-9-]*$` | Định danh duy nhất |
| `spec.name` | Chuỗi không rỗng, không ký tự điều khiển | Tên hiển thị |

---

## :material-shape: Danh sách `spec.type` hỗ trợ

| Type | Mô tả |
|---|---|
| `service` | Dịch vụ backend, yêu cầu `spec.review.branch` |
| `gateway` | API gateway, yêu cầu `spec.review.branch` |
| `worker` | Background worker |
| `batch` | Batch processing |
| `job` | Scheduled job |
| `library` | Thư viện dùng chung |
| `website` | Website / web app |
| `mobile-app` | Ứng dụng di động |
| `data-pipeline` | Data pipeline |
| `function` | Serverless function |
| `plugin` | Plugin / extension |
| `tool` | Công cụ nội bộ |
| `documentation` | Tài liệu |
| `other` | Loại khác |

Custom type khớp `^[a-z][a-z0-9-]*$` cũng được chấp nhận.

---

## :material-account-group: Owners

```yaml
spec:
  owners:
    members:
      - user: lead@vinsmartfuture.tech
        role: techlead
      - user: dev1@vinsmartfuture.tech
        role: maintainer
      - user: dev2@vinsmartfuture.tech
        role: member
```

| Quy tắc | Chi tiết |
|---|---|
| `user` | Phải là email `*@vinsmartfuture.tech` |
| `role` | `techlead`, `maintainer`, hoặc `member` |
| Yêu cầu | Nếu `members` không rỗng, phải có ≥ 1 `techlead` |

---

## :material-swap-horizontal: Chuyển đổi nội bộ

`BackstageEntityNormalizer` chuyển đổi VSF v2 sang `NormalizedDescriptor`:

| VSF v2 | `NormalizedDescriptor` |
|---|---|
| `spec.id` | `metadata.name` |
| `spec.name` | `metadata.title` |
| `metadata.namespace` | `metadata.namespace` |
| — | `apiVersion` = `"vsf-idp.io/v2"` |
| — | `kind` = `"Component"` |
| — | `entity_ref` = `component:{namespace}/{id}` |

---

## :material-link: Đọc thêm

- [Tương thích Backstage](backstage.md)
- [Trường Topology](topology.md)
- [`CatalogValidationEngine`](../backend/validation.md)

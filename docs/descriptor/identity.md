---
title: Quy tắc định danh
description: EntityReference, canonical format, và quy tắc parse.
---

# :material-fingerprint: Quy tắc định danh

Mỗi entity trong `CatalogWorkspace` được xác định duy nhất bằng `EntityReference` — bộ ba `kind:namespace/name`.

---

## :material-format-text: Canonical Format

```
kind:namespace/name
```

| Thành phần | Quy tắc | Ví dụ |
|---|---|---|
| `kind` | Lowercase, khớp `^[a-z0-9][a-z0-9._-]{0,62}$` | `component` |
| `namespace` | Lowercase, khớp `^[a-z0-9][a-z0-9._-]{0,62}$` | `platform` |
| `name` | Lowercase, khớp `^[a-z0-9][a-z0-9._-]{0,62}$` | `payment-gateway` |

**Ví dụ đầy đủ:** `component:platform/payment-gateway`

---

## :material-swap-horizontal: Parse Rules

`EntityReference.parse(value, default_kind, default_namespace)`:

| Input | `default_kind` | `default_namespace` | Kết quả |
|---|---|---|---|
| `"component:platform/payment-gateway"` | — | — | `component:platform/payment-gateway` |
| `"platform/payment-gateway"` | `"component"` | — | `component:platform/payment-gateway` |
| `"payment-gateway"` | `"component"` | `"default"` | `component:default/payment-gateway` |
| `"Payment-Gateway"` | `"component"` | `"default"` | `component:default/payment-gateway` (lowercase) |

### Lỗi parse

- Không có `kind` và không có `default_kind` → `ValueError`
- Segment không khớp regex → `ValueError`

---

## :material-tag: Tính canonical `EntityReference` cho mỗi format

### VSF IDP v2

```
component:{metadata.namespace}/{spec.id}
```

Luôn có `kind` = `component`, `namespace` = `metadata.namespace`, `name` = `spec.id`.

### Backstage

```
{kind}:{metadata.namespace}/{metadata.name}
```

`kind` và `namespace` từ descriptor, mặc định `namespace` = `"default"`.

---

## :material-alert: Duplicate Detection

Khi hai document tạo ra cùng canonical `EntityReference`:

- `CatalogWorkspace` chuyển cả hai sang `TopologyNodeState.CONFLICT`
- Phát sinh `IdentityConflict` trong `CatalogSnapshot.conflicts`
- Không entity nào thắng — phải giải quyết thủ công

---

## :material-link: Đọc thêm

- [VSF IDP v2](vsf-v2.md)
- [Tương thích Backstage](backstage.md)
- [Quản lý trạng thái](../architecture/state.md)

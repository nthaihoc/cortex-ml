---
title: Tương thích Backstage
description: Hỗ trợ Backstage descriptor format trong IDP Platform.
---

# :material-swap-horizontal: Tương thích Backstage

IDP Platform hỗ trợ đầy đủ [Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/) descriptor format. `CatalogValidationEngine` tự nhận diện format khi **không** có trường `specVersion`.

---

## :material-file-document-outline: Cấu trúc

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: payment-gateway
  namespace: platform            # Mặc định: "default"
  title: Payment Gateway Service
  description: Xử lý thanh toán
  labels:
    tier: backend
  annotations:
    github.com/project-slug: team/payment-gateway
  tags:
    - java
    - grpc
  links:
    - url: https://dashboard.example.com
      title: Dashboard
spec:
  type: service
  lifecycle: production
  owner: team-platform
  system: platform
  dependsOn:
    - component:platform/auth-service
  providesApis:
    - api:platform/payment-api
```

---

## :material-format-list-checks: Trường bắt buộc

| Trường | Quy tắc |
|---|---|
| `apiVersion` | Bắt buộc, chuỗi không rỗng |
| `kind` | Bắt buộc, chuỗi không rỗng |
| `metadata` | Bắt buộc, phải là object |
| `metadata.name` | Bắt buộc, chuỗi không rỗng |
| `spec` | Nếu có, phải là object |

---

## :material-swap-horizontal: Chuyển đổi sang `NormalizedDescriptor`

`BackstageEntityNormalizer` xử lý trực tiếp:

| Backstage | `NormalizedDescriptor` |
|---|---|
| `apiVersion` | `api_version` |
| `kind` | `kind` (lowercase) |
| `metadata.name` | `metadata.name` (lowercase) |
| `metadata.namespace` | `metadata.namespace` (lowercase, mặc định `"default"`) |
| — | `entity_ref` = `{kind}:{namespace}/{name}` |

---

## :material-relation-many-to-many: Relation Fields

Backstage sử dụng spec fields trực tiếp (khác với VSF v2 dùng `spec.topology[]`):

| Spec Field | `RelationType` | Default Kind |
|---|---|---|
| `spec.system` | `partOf` | `system` |
| `spec.domain` | `partOf` | `domain` |
| `spec.parent` | `partOf` | `group` |
| `spec.dependsOn[]` | `dependsOn` | `component` |
| `spec.providesApis[]` | `providesApi` | `api` |
| `spec.consumesApis[]` | `consumesApi` | `api` |
| `spec.publishesTo[]` | `publishesTo` | `event` |
| `spec.consumesFrom[]` | `consumesFrom` | `event` |

---

## :material-link: Đọc thêm

- [VSF IDP v2](vsf-v2.md)
- [Quy tắc định danh](identity.md)
- [Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/)

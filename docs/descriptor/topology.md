---
title: Trường Topology
description: Khai báo quan hệ giữa các entity qua spec.topology và spec fields.
---

# :material-graph: Trường Topology

Topology xác định quan hệ (relation) giữa các entity. Có hai cách khai báo tuỳ theo format.

---

## :material-new-box: VSF IDP v2 — `spec.topology[]`

VSF v2 sử dụng array `spec.topology[]` với format `type:ref`:

```yaml
specVersion: vsf-idp.io/v2
# ...
spec:
  topology:
    - ref: "component:platform/auth-service"
      protocol: gRPC
      reason: Token validation
    - ref: "component:platform/notification-service"
      reason: Send payment notifications
    - ref: "providesApis:api/payment-api"
```

### Cấu trúc mỗi item

| Trường | Bắt buộc | Mô tả |
|---|---|---|
| `ref` | ✅ | `EntityReference` dạng `type:identity` hoặc canonical |
| `protocol` | Không | Giao thức kết nối (VD: `gRPC`, `REST`, `Kafka`) |
| `reason` | Không | Lý do quan hệ |

### Type prefix mapping

`BackstageRelationProjector` parse `type` từ prefix trước dấu `:` trong `ref`:

| Type Prefix | `RelationType` | Default Kind |
|---|---|---|
| `system` | `partOf` | `system` |
| `domain` | `partOf` | `domain` |
| `parent` | `partOf` | `group` |
| `component` | `dependsOn` | `component` |
| `resource` | `dependsOn` | `resource` |
| `providesApis` | `providesApi` | `api` |
| `consumesApis` | `consumesApi` | `api` |
| `publishesTo` | `publishesTo` | `event` |
| `consumesFrom` | `consumesFrom` | `event` |
| `module` | `contains` | `module` |
| `function` | `contains` | `function` |

!!! note "Case-insensitive"
    Type prefix trong VSF v2 là case-insensitive. `Component:...` và `component:...` đều hợp lệ.

---

## :material-swap-horizontal: Backstage — Spec Fields

Backstage sử dụng spec fields riêng lẻ:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
# ...
spec:
  system: platform
  dependsOn:
    - component:platform/auth-service
    - component:platform/notification-service
  providesApis:
    - api:platform/payment-api
  consumesApis:
    - api:platform/config-api
```

Ngoài ra, Backstage cũng hỗ trợ `spec.topology[]` với trường `type` tường minh:

```yaml
spec:
  topology:
    - type: component
      ref: platform/auth-service
      protocol: gRPC
```

---

## :material-relation-many-to-many: Bảng `RelationType` đầy đủ

| `RelationType` | Ý nghĩa | Ví dụ |
|---|---|---|
| `partOf` | Entity thuộc về entity khác | Service thuộc System |
| `dependsOn` | Entity phụ thuộc entity khác | Service gọi Service khác |
| `providesApi` | Entity cung cấp API | Service expose REST API |
| `consumesApi` | Entity tiêu thụ API | Service gọi API bên ngoài |
| `publishesTo` | Entity publish event | Service gửi message tới topic |
| `consumesFrom` | Entity consume event | Service đọc message từ topic |
| `contains` | Entity chứa entity con | Module chứa Function |

---

## :material-alert-circle: Validation cho Topology

| Mã lỗi | Mô tả | Blocking? |
|---|---|---|
| `REFERENCE_INVALID` | Reference string không parse được | ✅ |
| `TOPOLOGY_SELF_REFERENCE` | Entity tự reference chính nó | ⚠️ Warning |
| `REFERENCE_TARGET_NOT_FOUND` | Target không tồn tại trong `CatalogSnapshot` | ⚠️ Warning |

---

## :material-link: Đọc thêm

- [VSF IDP v2](vsf-v2.md)
- [Quy tắc định danh](identity.md)
- [Ingest Pipeline](../backend/ingest-pipeline.md)

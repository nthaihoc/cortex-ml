---
title: Backstage Compatibility
description: Using Backstage-format descriptors alongside VSF IDP v2 in the same workspace.
---

# :material-history: Backstage Compatibility

The IDP Platform **reads existing Backstage-format `catalog-info.yaml` files** without modification. Backstage descriptors are first-class citizens in the same workspace as VSF IDP v2 descriptors.

---

## :material-file-document-outline: Backstage Descriptor Example

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: legacy-service
  namespace: default
  title: Legacy Service
  description: An existing Backstage component being migrated.
  labels:
    team: platform
  annotations:
    backstage.io/techdocs-ref: dir:.
  tags:
    - java
    - legacy
spec:
  type: service
  lifecycle: production
  owner: group:platform-team
  system: system:payments
  dependsOn:
    - component:auth-service
  providesApis:
    - api:legacy-api
```

---

## :material-check-decagram: What Backstage Fields Are Supported

| Field | Supported | Notes |
|-------|-----------|-------|
| `apiVersion` | ✅ | Any non-blank string |
| `kind` | ✅ | Any non-blank string (Component, API, System, Group, …) |
| `metadata.name` | ✅ | Forms the entity name |
| `metadata.namespace` | ✅ | Defaults to `"default"` if absent |
| `metadata.title` | ✅ | Used as `display_name` |
| `metadata.description` | ✅ | Preserved in descriptor |
| `metadata.labels` | ✅ | Preserved as-is |
| `metadata.annotations` | ✅ | Preserved as-is |
| `metadata.tags` | ✅ | Preserved as-is |
| `spec.type` | ✅ | Preserved in descriptor |
| `spec.lifecycle` | ✅ | Preserved in descriptor |
| `spec.owner` | ✅ | Normalized to canonical reference |
| `spec.system` | ✅ | Normalized and projected as `partOf` |
| `spec.domain` | ✅ | Normalized and projected as `partOf` |
| `spec.parent` | ✅ | Normalized and projected as `partOf` |
| `spec.dependsOn[]` | ✅ | Projected as `dependsOn` relations |
| `spec.providesApis[]` | ✅ | Projected as `providesApi` relations |
| `spec.consumesApis[]` | ✅ | Projected as `consumesApi` relations |
| `spec.publishesTo[]` | ✅ | Projected as `publishesTo` relations |
| `spec.consumesFrom[]` | ✅ | Projected as `consumesFrom` relations |
| `spec.topology[]` | ✅ | VSF-style topology items |
| `Location` kind | ⚠️ | Accepted but targets are not followed (warning diagnostic) |

---

## :material-swap-horizontal: Reference Normalization

Backstage reference strings are normalized to canonical form during ingest:

| Input | Normalized |
|-------|-----------|
| `"auth-service"` | `component:default/auth-service` |
| `"group:platform-team"` | `group:default/platform-team` |
| `"system:payments"` | `system:default/payments` |
| `"component:my-ns/auth-service"` | `component:my-ns/auth-service` |

---

## :material-alert-outline: Known Limitations

!!! warning "Location kind not followed"
    The `Location` kind is recognized but its `targets` are **not** discovered or followed. A `LOCATION_KIND_NOT_SUPPORTED` warning diagnostic is generated. Add target descriptors directly to the Catalog Root instead.

!!! info "No Backstage-specific validation"
    Backstage descriptors pass minimal required field checks only (`apiVersion`, `kind`, `metadata.name`). VSF-specific rules (ownership email format, component types, review gate) apply only to `specVersion: vsf-idp.io/v2` documents.

---

## :material-link: Further Reading

- [VSF IDP v2 Reference](vsf-v2.md)
- [Backstage Software Catalog Descriptor Format](https://backstage.io/docs/features/software-catalog/descriptor-format)
- [Backstage Component Entity](https://backstage.io/docs/features/software-catalog/system-model)

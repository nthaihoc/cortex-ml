---
title: Backstage Compatibility
description: Using Backstage-format descriptors alongside VSF IDP v2.
---

# :material-swap-horizontal: Backstage Compatibility

The IDP Platform can read **Backstage-format** `catalog-info.yaml` files alongside VSF IDP v2 descriptors. This makes it easy to migrate from Backstage without rewriting all your files at once.

---

## Backstage Format Example

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: my-service
  namespace: default
  title: My Service
  description: A backend service.
spec:
  type: service
  owner: team-alpha
  system: core-platform
  dependsOn:
    - component:default/auth-service
  providesApis:
    - api:default/my-api
```

---

## How the Two Formats Differ

| Feature | VSF IDP v2 | Backstage |
|---------|-----------|-----------|
| Identifier | `specVersion: vsf-idp.io/v2` | `apiVersion: backstage.io/v1alpha1` |
| Entity kind | Always `component` | Flexible: `Component`, `System`, `API`, etc. |
| Identity | `component:{namespace}/{spec.id}` | `{kind}:{namespace}/{name}` |
| Namespace | `metadata.namespace` | `metadata.namespace` (default: `default`) |
| Name | `spec.id` (identity) + `spec.name` (display) | `metadata.name` (both identity and display) |
| Ownership | `spec.owners.members[]` with roles | `spec.owner` (single string) |
| Relations | `spec.topology[]` with `ref`, `protocol`, `reason` | `spec.dependsOn[]`, `spec.providesApis[]`, etc. |

---

## Automatic Detection

The system automatically detects which format a file uses:

- If the file contains `specVersion` → treated as **VSF IDP v2**
- Otherwise → treated as **Backstage** format

Both formats go through the same validation and normalization pipeline, just with different rules.

---

## Reference Normalization

In Backstage format, the normalizer automatically converts short references to canonical form:

| Field | What you write | What it becomes |
|-------|---------------|-----------------|
| `spec.owner` | `team-alpha` | `group:default/team-alpha` |
| `spec.system` | `core-platform` | `system:default/core-platform` |
| `spec.dependsOn[]` | `auth-service` | `component:default/auth-service` |
| `spec.providesApis[]` | `my-api` | `api:default/my-api` |

The default kind and namespace are filled in based on the field type and the entity's own namespace.

---

## Important Differences

!!! info "Entity kinds"
    VSF IDP v2 always creates `component` entities. Backstage supports many kinds: `Component`, `System`, `API`, `Resource`, `Group`, `Domain`, etc.

!!! info "Mixed workspaces"
    Both formats can coexist in the same catalog root. A Backstage `System` entity can be referenced by a VSF IDP v2 `topology` entry, and vice versa.

!!! warning "Location kind"
    Backstage `Location` entities are not followed by the local catalog workspace. They produce a `LOCATION_KIND_NOT_SUPPORTED` warning. Add the target descriptors directly under a catalog root instead.

---

## Further Reading

- [VSF IDP v2 Reference](vsf-v2.md)
- [Identity Rules](identity.md)
- [Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/)

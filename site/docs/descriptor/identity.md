---
title: Identity Rules
description: How entity identity is computed and enforced in the IDP Platform.
---

# :material-key: Identity Rules

Entity identity is the cornerstone of the catalog's conflict detection and relation resolution.

---

## :material-fingerprint: Canonical Reference Format

Every entity in the catalog is uniquely identified by a **canonical reference** of the form:

```
{kind}:{namespace}/{name}
```

All three segments are **lowercase** and must match the pattern:

```regex
^[a-z0-9][a-z0-9._-]{0,62}$
```

### Examples

| Canonical Reference | kind | namespace | name |
|---------------------|------|-----------|------|
| `component:platform/payment-gateway` | `component` | `platform` | `payment-gateway` |
| `system:default/payments` | `system` | `default` | `payments` |
| `api:platform/payment-api` | `api` | `platform` | `payment-api` |
| `group:default/platform-team` | `group` | `default` | `platform-team` |

---

## :material-star: VSF IDP v2 Identity

For VSF v2 descriptors, the canonical reference is derived from:

- **kind:** always `component`
- **namespace:** `metadata.namespace`
- **name:** `spec.id`

```yaml
metadata:
  namespace: platform   # → namespace
spec:
  id: payment-gateway   # → name
  name: Payment Gateway # display-only, does NOT affect identity
```

**Canonical:** `component:platform/payment-gateway`

!!! info "Service key vs. canonical reference"
    The "service key" used internally is `{metadata.system}.{spec.id}` (display purposes only). The catalog identity used for relations and conflict detection is always the canonical reference.

---

## :material-history: Backstage Identity

For Backstage descriptors, the canonical reference is derived from:

- **kind:** `kind` field (lowercased)
- **namespace:** `metadata.namespace` (defaults to `"default"` if absent)
- **name:** `metadata.name` (lowercased)

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component                   # → kind
metadata:
  namespace: platform             # → namespace
  name: legacy-service            # → name
  title: Legacy Service           # display-only
```

**Canonical:** `component:platform/legacy-service`

---

## :material-swap-horizontal: Changing Identity

| Change | Effect |
|--------|--------|
| VSF: rename `spec.name` | **No identity change** — display name only |
| VSF: change `spec.id` | **New identity** — old entity removed, new entity created |
| VSF: change `metadata.namespace` | **New identity** |
| Backstage: rename `metadata.title` | **No identity change** |
| Backstage: rename `metadata.name` | **New identity** |
| Backstage: change `metadata.namespace` | **New identity** |

---

## :material-content-duplicate: Duplicate Identity (Conflicts)

If two or more `catalog-info.yaml` files claim the **same canonical reference**, a **conflict** is created:

- **Neither** entity is promoted to the resolved entities map
- A `ENTITY_DUPLICATE_REF` blocking diagnostic is generated for **each** conflicting file
- The conflict appears as a special "IDENTITY CONFLICT" node in topology
- Relations pointing to the conflicting reference are marked as `provisional` and `health: error`

**Resolution:** change `metadata.namespace` or `spec.id` (VSF) / `metadata.name` (Backstage) in one of the conflicting files.

---

## :material-code-braces: EntityReference Python API

```python
from app.domain.value_objects.entity_reference import EntityReference

# Parse from a full reference string
ref = EntityReference.parse("component:platform/payment-gateway")
print(ref.kind)      # "component"
print(ref.namespace) # "platform"
print(ref.name)      # "payment-gateway"
print(ref.canonical) # "component:platform/payment-gateway"

# Parse with defaults
ref = EntityReference.parse(
    "payment-gateway",
    default_kind="component",
    default_namespace="platform",
)
# → component:platform/payment-gateway

# Construct from parts
ref = EntityReference.from_parts("component", "platform", "payment-gateway")
```

---

## :material-link: Further Reading

- [VSF IDP v2 Descriptor](vsf-v2.md)
- [Backstage Compatibility](backstage.md)
- [Diagnostics: ENTITY_DUPLICATE_REF](../diagnostics/codes.md#entity_duplicate_ref)
- [Backstage Entity Reference format](https://backstage.io/docs/features/software-catalog/references)

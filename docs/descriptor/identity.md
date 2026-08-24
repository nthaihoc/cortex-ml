---
title: Identity Rules
description: How entity identity is computed and what happens with duplicates.
---

# :material-key: Identity Rules

Every entity in the catalog has a **canonical reference** — a unique string that identifies it. This page explains how identity works and what happens when two files have the same identity.

---

## How Identity is Computed

### VSF IDP v2

For VSF IDP v2 descriptors, the canonical reference is always:

```
component:{metadata.namespace}/{spec.id}
```

**Example:**

```yaml
specVersion: vsf-idp.io/v2
metadata:
  namespace: platform     # ← part of identity
spec:
  id: payment-gateway     # ← part of identity
  name: Payment Gateway   # ← NOT part of identity (display only)
```

Canonical reference: `component:platform/payment-gateway`

### Backstage

For Backstage descriptors, the canonical reference is:

```
{kind}:{metadata.namespace}/{metadata.name}
```

**Example:**

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component              # ← part of identity
metadata:
  name: auth-service         # ← part of identity
  namespace: default         # ← part of identity (default: "default")
  title: Authentication      # ← NOT part of identity
```

Canonical reference: `component:default/auth-service`

---

## Normalization

All identity segments are **lowercased** and must match the pattern `^[a-z0-9][a-z0-9._-]{0,62}$`:

- Must start with a lowercase letter or number
- Can contain lowercase letters, numbers, dots, underscores, and hyphens
- Maximum 63 characters per segment

These are **valid** identifiers: `payment-gateway`, `auth.service`, `my_api_v2`

These are **invalid** identifiers: `Payment-Gateway` (uppercase), `-starts-with-hyphen`, `` (empty)

---

## Identity Conflicts

A conflict happens when **two or more files** produce the same canonical reference.

**Example scenario:**

```
services/a/catalog-info.yaml  →  component:platform/payment-gateway
services/b/catalog-info.yaml  →  component:platform/payment-gateway  ← CONFLICT!
```

When a conflict is detected:

1. **Neither entity is shown** in the catalog — both are removed from the snapshot
2. A **conflict node** appears in the topology graph (marked with :material-alert-circle:{ style="color: #ef4444" })
3. Both files get an `ENTITY_DUPLICATE_REF` **error diagnostic**
4. The diagnostic message tells you which other file is causing the conflict

### How to Fix a Conflict

Change `metadata.namespace` or the identity field (`spec.id` for VSF, `metadata.name` for Backstage) in one of the conflicting files so they produce different canonical references.

---

## Identity Changes

If you change the identity fields of a file, the system treats it as:

1. **Remove** the old entity (with the old reference)
2. **Add** a new entity (with the new reference)

All relations from and to the old reference become unresolved until other files update their references to match.

---

## Display Name vs. Identity

| Format | Identity Field | Display Name Field |
|--------|---------------|-------------------|
| VSF IDP v2 | `spec.id` | `spec.name` |
| Backstage | `metadata.name` | `metadata.title` (or `metadata.name` if no title) |

You can freely change the display name without affecting the entity's identity or any relations that point to it.

---

## Further Reading

- [VSF IDP v2 Reference](vsf-v2.md)
- [Backstage Compatibility](backstage.md)
- [State Management](../architecture/state.md) — How conflicts are tracked
- [Diagnostic Codes](../diagnostics/codes.md) — `ENTITY_DUPLICATE_REF` details

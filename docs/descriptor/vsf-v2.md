---
title: VSF IDP v2 Descriptor
description: Complete reference for the VSF IDP v2 catalog-info.yaml descriptor format.
---

# :material-star: VSF IDP v2 Descriptor

The **VSF IDP v2** format is the primary way to describe services in the platform. It is identified by `specVersion: vsf-idp.io/v2` at the top of the file.

---

## Full Example

```yaml
specVersion: vsf-idp.io/v2

metadata:
  namespace: platform
  system: payments
  domain: Financial Services

spec:
  id: payment-gateway
  name: Payment Gateway Service
  type: service
  description: |
    Handles all payment processing and routing for the platform.

  owners:
    members:
      - user: alice@vinsmartfuture.tech
        role: techlead
      - user: bob@vinsmartfuture.tech
        role: maintainer

  review:
    branch: main

  topology:
    - ref: "component:checkout-service"
      protocol: REST
      reason: "Receives payment requests"
    - ref: "providesApis:payment-api"
```

This file creates an entity with the identity `component:platform/payment-gateway`.

---

## Field Reference

### Root Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `specVersion` | `string` | ✅ | Must be exactly `"vsf-idp.io/v2"` |
| `metadata` | `object` | ✅ | Classification and identity fields |
| `spec` | `object` | ✅ | Service specification |

---

### `metadata` Object

| Field | Type | Required | Rules |
|-------|------|----------|-------|
| `namespace` | `string` | ✅ | Must match `^[a-z][a-z0-9-]*$` (lowercase letters, numbers, hyphens) |
| `system` | `string` | ✅ | Must match `^[a-z][a-z0-9-]*$` |
| `domain` | `string` | ✅ | Up to 128 printable characters, free text |

**Example:**

```yaml
metadata:
  namespace: platform      # Used in entity identity
  system: idp-core         # Groups related services
  domain: Platform Engineering  # Business domain (free text)
```

---

### `spec` Object

| Field | Type | Required | Rules |
|-------|------|----------|-------|
| `id` | `string` | ✅ | Must match `^[a-z][a-z0-9-]*$` — this forms the entity identity |
| `name` | `string` | ✅ | Display name (no control characters). Changing this does **not** change identity. |
| `type` | `string` | ✅ | Must be one of the [Component Types](#component-types) below |
| `description` | `string` | — | Free text description |
| `owners` | `object` | ✅ | See [Ownership](#ownership) below |
| `review` | `object` | Conditional | Required for `service` and `gateway` types |
| `topology` | `array` | — | See [Topology](topology.md) |

---

### Ownership {#ownership}

Every service must have at least one owner with the `techlead` role.

```yaml
spec:
  owners:
    members:
      - user: alice@vinsmartfuture.tech
        role: techlead       # Required: at least one techlead
      - user: bob@vinsmartfuture.tech
        role: maintainer
      - user: charlie@vinsmartfuture.tech
        role: member
```

| Field | Type | Rules |
|-------|------|-------|
| `members` | `array` | Must have at least one item |
| `members[*].user` | `string` | Must be a `@vinsmartfuture.tech` email address |
| `members[*].role` | `string` | One of: `techlead`, `maintainer`, `member` |

!!! warning "At least one techlead required"
    If no member has `role: techlead`, the validation engine produces a blocking `SCHEMA_FIELD_REQUIRED` error and the entity will not be registered.

---

### Review Gate

Required for services with `type: service` or `type: gateway`:

```yaml
spec:
  review:
    branch: main    # The Git branch used for review
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `branch` | `string` | ✅ | Git branch name for the review gate |

---

### Topology

Declares connections to other services. See the full reference at [Topology Fields](topology.md).

```yaml
spec:
  topology:
    - ref: "component:auth-service"
      protocol: gRPC
      reason: "Token validation"
    - ref: "providesApis:payment-api"
```

---

## Component Types {#component-types}

The `spec.type` field must be one of these values:

| Type | Use for |
|------|---------|
| `service` | Long-running HTTP or gRPC service |
| `gateway` | API gateway or backend-for-frontend |
| `worker` | Background worker or message consumer |
| `batch` | Batch processing job |
| `job` | Scheduled or trigger-based job |
| `library` | Shared library or SDK |
| `website` | Web frontend application |
| `mobile-app` | Mobile application |
| `data-pipeline` | Data processing pipeline |
| `function` | Serverless function |
| `plugin` | Plugin or extension |
| `tool` | Internal tooling |
| `documentation` | Documentation site |
| `other` | Anything that does not fit the above |

---

## Identity

An entity's canonical reference is computed as:

```
component:{metadata.namespace}/{spec.id}
```

**Example:** `metadata.namespace: platform` + `spec.id: payment-gateway` → `component:platform/payment-gateway`

Key rules:

- `spec.name` is **display-only** — changing it does not change the identity
- Changing `metadata.namespace` or `spec.id` changes the identity
- Two files with the same canonical reference create an **identity conflict** (see [Identity Rules](identity.md))

---

## Further Reading

- [Backstage Compatibility](backstage.md) — Using Backstage descriptors
- [Identity Rules](identity.md) — Detailed identity and conflict rules
- [Topology Fields](topology.md) — All relation types
- [Validation Engine](../backend/validation.md) — How validation works
- [Diagnostic Codes](../diagnostics/codes.md) — All error and warning codes

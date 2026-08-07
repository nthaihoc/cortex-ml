---
title: VSF IDP v2 Descriptor
description: Complete reference for the VSF IDP v2 catalog-info.yaml descriptor format.
---

# :material-star: VSF IDP v2 Descriptor

The **VSF IDP v2** format (`specVersion: vsf-idp.io/v2`) is the primary authoring contract for all new services in the platform.

---

## :material-file-document-outline: Minimal Valid Example

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
      reason: "Receives payment initiation requests"
    - ref: "providesApis:payment-api"
```

---

## :material-format-list-bulleted: Field Reference

### Root Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `specVersion` | `string` | ✅ | Must be exactly `"vsf-idp.io/v2"` |
| `metadata` | `object` | ✅ | Entity identity and classification |
| `spec` | `object` | ✅ | Component specification |

---

### `metadata` Object

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `namespace` | `string` | ✅ | Matches `^[a-z][a-z0-9-]*$` |
| `system` | `string` | ✅ | Matches `^[a-z][a-z0-9-]*$` |
| `domain` | `string` | ✅ | ≤ 128 printable characters |

---

### `spec` Object

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `id` | `string` | ✅ | Matches `^[a-z][a-z0-9-]*$` — forms the entity identity |
| `name` | `string` | ✅ | Display name; no control characters |
| `type` | `string` | ✅ | See [Component Types](#component-types) |
| `description` | `string` | — | Free-form description |
| `owners` | `object` | ✅ | Ownership declaration |
| `review` | `object` | ✅ for `service`, `gateway` | Review gate configuration |
| `topology` | `array` | — | Declared relations to other entities |

---

### `spec.owners` Object

```yaml
spec:
  owners:
    members:
      - user: alice@vinsmartfuture.tech
        role: techlead
      - user: bob@vinsmartfuture.tech
        role: maintainer
      - user: charlie@vinsmartfuture.tech
        role: member
```

| Field | Type | Validation |
|-------|------|------------|
| `members` | `array` | At least one member required |
| `members[*].user` | `string` | Must match `[^@\s]+@vinsmartfuture.tech` |
| `members[*].role` | `string` | One of: `techlead`, `maintainer`, `member` |

!!! warning "At least one `techlead` required"
    Every `spec.owners.members` array must contain at least one member with `role: techlead`. Missing this causes a `SCHEMA_FIELD_REQUIRED` blocking diagnostic.

---

### `spec.review` Object

Required for components with `type: service` or `type: gateway`.

```yaml
spec:
  review:
    branch: main
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `branch` | `string` | ✅ | Git branch used for the review gate |

---

### :material-graph: `spec.topology` Array

Declares typed relations to other catalog entities. Each item requires a `ref` and may include `protocol` and `reason`.

```yaml
spec:
  topology:
    - ref: "component:auth-service"
      protocol: gRPC
      reason: "Token validation"
    - ref: "providesApis:payment-api"
    - ref: "consumesFrom:transaction-events"
      protocol: Kafka
```

#### `ref` Format

The `ref` value uses a `{kind}:{identifier}` prefix format:

| Prefix | Target Kind | Relation |
|--------|------------|---------|
| `system:{id}` | `system` | `partOf` |
| `component:{id}` | `component` | `dependsOn` |
| `resource:{id}` | `resource` | `dependsOn` |
| `providesApis:{id}` | `api` | `providesApi` |
| `consumesApis:{id}` | `api` | `consumesApi` |
| `publishesTo:{id}` | `event` | `publishesTo` |
| `consumesFrom:{id}` | `event` | `consumesFrom` |
| `module:{id}` | `module` | `contains` |
| `function:{id}` | `function` | `contains` |

---

## :material-shape-outline: Component Types {#component-types}

The `spec.type` field accepts these values:

| Type | Description |
|------|-------------|
| `service` | Long-running HTTP/gRPC service |
| `gateway` | API gateway or BFF |
| `worker` | Background worker or consumer |
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
| `other` | Does not fit the above categories |

---

## :material-key: Identity Rules

An entity's canonical reference is computed as:

```
component:{metadata.namespace}/{spec.id}
```

**Example:** A descriptor with `metadata.namespace: platform` and `spec.id: payment-gateway` has the canonical reference `component:platform/payment-gateway`.

- `spec.name` is **display-only** and can change without affecting identity
- Changing `metadata.namespace` or `spec.id` changes the entity's identity
- Two files with the same canonical reference create an **identity conflict**

---

## :material-link: Further Reading

- [Backstage Compatibility](backstage.md)
- [Identity Rules](identity.md)
- [Topology Fields](topology.md)
- [Validation Engine](../backend/validation.md)
- [Diagnostic Codes](../diagnostics/codes.md)

---
title: Topology Fields
description: Complete reference for topology relation declarations in catalog-info.yaml descriptors.
---

# :material-graph: Topology Fields

Topology declarations express **intentional relationships** between catalog entities. These are declared in the descriptor, never inferred from runtime traffic.

---

## :material-relation-many-to-many: Supported Relation Types

| Relation | Direction | Description |
|----------|-----------|-------------|
| `partOf` | entity → parent | Entity belongs to a system, domain, or group |
| `dependsOn` | entity → dependency | Entity depends on another component or resource |
| `providesApi` | entity → API | Entity exposes this API |
| `consumesApi` | entity → API | Entity consumes this API |
| `publishesTo` | entity → event | Entity publishes to this event/topic |
| `consumesFrom` | entity → event | Entity consumes from this event/topic |
| `contains` | entity → module/function | Entity contains this module or function |

---

## :material-star: VSF IDP v2 Topology

In VSF v2, topology is declared as a list in `spec.topology`. Each item uses a `{kind}:{id}` prefix format.

```yaml
spec:
  topology:
    # Depends on another component
    - ref: "component:auth-service"
      protocol: gRPC
      reason: "Token validation"

    # Provides an API
    - ref: "providesApis:payment-api"

    # Consumes from a Kafka topic
    - ref: "consumesFrom:transaction-events"
      protocol: Kafka
      reason: "Async event processing"

    # Part of a system
    - ref: "system:payments"
```

### VSF Topology Item Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ref` | `string` | ✅ | `{kind-prefix}:{identifier}`, optionally `{kind}:{namespace}/{name}` |
| `protocol` | `string` | — | Transport protocol (e.g., `REST`, `gRPC`, `Kafka`, `AMQP`) |
| `reason` | `string` | — | Human-readable reason for this relation |

### VSF Ref Prefix Mapping

| Prefix | Resolved kind | Relation |
|--------|--------------|---------|
| `system` | `system` | `partOf` |
| `component` | `component` | `dependsOn` |
| `resource` | `resource` | `dependsOn` |
| `providesApis` | `api` | `providesApi` |
| `consumesApis` | `api` | `consumesApi` |
| `publishesTo` | `event` | `publishesTo` |
| `consumesFrom` | `event` | `consumesFrom` |
| `module` | `module` | `contains` |
| `function` | `function` | `contains` |

---

## :material-history: Backstage Topology

In Backstage format, relations are declared as top-level `spec` fields:

```yaml
spec:
  system: system:payments               # partOf
  domain: domain:financial-services     # partOf
  owner: group:platform-team            # ownership (not a topology relation)
  dependsOn:
    - component:auth-service
    - component:billing-service
  providesApis:
    - api:payment-api
  consumesApis:
    - api:auth-api
  publishesTo:
    - event:payment-completed
  consumesFrom:
    - event:order-created
```

### Backstage Field Mapping

| Spec Field | Default Kind | Relation |
|-----------|-------------|---------|
| `system` | `system` | `partOf` |
| `domain` | `domain` | `partOf` |
| `parent` | `group` | `partOf` |
| `dependsOn[]` | `component` | `dependsOn` |
| `providesApis[]` | `api` | `providesApi` |
| `consumesApis[]` | `api` | `consumesApi` |
| `publishesTo[]` | `event` | `publishesTo` |
| `consumesFrom[]` | `event` | `consumesFrom` |

---

## :material-eye: Topology Visualization

### Health States for Relations

| State | Color | Meaning |
|-------|-------|---------|
| `healthy` | Green solid | Both source and target are resolved |
| `warning` | Amber dashed | Target entity is not yet resolved |
| `error` | Red dotted | Provisional relation (invalid source or duplicate target) |

### Traversal Rules

- **Root:** Always included in the focused view
- **Direction:** `both` (default), `incoming`, or `outgoing`
- **Depth:** Fixed at **1 hop** — click a related node to continue navigation
- **Missing targets:** Visible as `UNRESOLVED` warning nodes; do not block the source entity

---

## :material-alert-outline: Common Validation Issues

| Issue | Cause | Action |
|-------|-------|--------|
| `REFERENCE_INVALID` | `ref` is not a valid entity reference string | Check the prefix and identifier format |
| `REFERENCE_TARGET_NOT_FOUND` | Target entity not in the catalog | Add the target's `catalog-info.yaml` |
| `TOPOLOGY_SELF_REFERENCE` | Entity declares a relation to itself | Remove the self-referencing topology item |

---

## :material-link: Further Reading

- [VSF IDP v2 Reference](vsf-v2.md)
- [Focused Topology API](../api/endpoints.md#get-apiv1catalogtopology)
- [Topology Viewer](../frontend/topology-viewer.md)
- [Backstage System Model](https://backstage.io/docs/features/software-catalog/system-model)

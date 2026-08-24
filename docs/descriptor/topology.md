---
title: Topology Fields
description: How to declare connections between services in catalog-info.yaml.
---

# :material-graph: Topology Fields

Topology fields declare how your service connects to other services in the catalog. These connections are shown as edges in the topology graph.

---

## VSF IDP v2 Topology

In VSF IDP v2, all relations are declared in the `spec.topology` array:

```yaml
spec:
  topology:
    - ref: "component:platform/auth-service"
      protocol: gRPC
      reason: "Token validation on every request"
    - ref: "providesApis:platform/payment-api"
    - ref: "consumesFrom:platform/order-events"
      protocol: Kafka
```

### Topology Item Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ref` | `string` | ✅ | Reference to the target entity (see format below) |
| `protocol` | `string` | — | Communication protocol (e.g., `REST`, `gRPC`, `Kafka`) |
| `reason` | `string` | — | Why this connection exists |

### `ref` Format

The `ref` value uses a `{kind}:{namespace}/{name}` or `{kind}:{name}` format. The kind prefix determines the relation type:

| Prefix | Target Kind | Relation Type | Meaning |
|--------|------------|---------------|---------|
| `system:` | `system` | `partOf` | This service belongs to that system |
| `component:` | `component` | `dependsOn` | This service depends on that service |
| `resource:` | `resource` | `dependsOn` | This service depends on that resource |
| `providesApis:` | `api` | `providesApi` | This service provides that API |
| `consumesApis:` | `api` | `consumesApi` | This service consumes that API |
| `publishesTo:` | `event` | `publishesTo` | This service publishes to that event channel |
| `consumesFrom:` | `event` | `consumesFrom` | This service consumes from that event channel |
| `module:` | `module` | `contains` | This service contains that module |
| `function:` | `function` | `contains` | This service contains that function |

!!! tip "Short form"
    If you omit the namespace, it defaults to the entity's own `metadata.namespace`:
    ```yaml
    # These two are the same (when metadata.namespace is "platform"):
    - ref: "component:platform/auth-service"
    - ref: "component:auth-service"
    ```

---

## Backstage Topology

In Backstage format, relations are declared using separate spec fields:

```yaml
spec:
  system: core-platform
  dependsOn:
    - component:default/auth-service
    - resource:default/main-database
  providesApis:
    - api:default/payment-api
  consumesApis:
    - api:default/user-api
```

### Backstage Relation Fields

| Field | Default Kind | Multiple | Relation Type |
|-------|-------------|----------|---------------|
| `spec.system` | `system` | No (single value) | `partOf` |
| `spec.domain` | `domain` | No | `partOf` |
| `spec.parent` | `group` | No | `partOf` |
| `spec.dependsOn[]` | `component` | Yes (array) | `dependsOn` |
| `spec.providesApis[]` | `api` | Yes | `providesApi` |
| `spec.consumesApis[]` | `api` | Yes | `consumesApi` |
| `spec.publishesTo[]` | `event` | Yes | `publishesTo` |
| `spec.consumesFrom[]` | `event` | Yes | `consumesFrom` |

---

## Relation Types

The platform supports 7 relation types:

| Relation Type | Meaning | Example |
|--------------|---------|---------|
| `partOf` | Entity belongs to a larger group | Service → System |
| `dependsOn` | Entity depends on another entity | Service → Service |
| `providesApi` | Entity provides an API | Service → API |
| `consumesApi` | Entity uses an API | Service → API |
| `publishesTo` | Entity publishes events | Service → Event Channel |
| `consumesFrom` | Entity consumes events | Service → Event Channel |
| `contains` | Entity contains a sub-component | Service → Module |

---

## Validation Rules

The system checks topology entries for several problems:

| Problem | Error Code | Blocking |
|---------|-----------|----------|
| `ref` is not a valid entity reference | `REFERENCE_INVALID` | ✅ Yes |
| Unknown relation kind prefix | `REFERENCE_INVALID` | ✅ Yes |
| Target entity does not exist in the catalog | `REFERENCE_TARGET_NOT_FOUND` | ❌ No (warning) |
| Entity references itself | `TOPOLOGY_SELF_REFERENCE` | ✅ Yes |

---

## Further Reading

- [VSF IDP v2 Reference](vsf-v2.md)
- [Backstage Compatibility](backstage.md)
- [Diagnostic Codes](../diagnostics/codes.md)

---
title: Descriptor Format
description: How to write catalog-info.yaml files for the IDP Platform.
---

# :material-file-code-outline: Descriptor Format

The IDP Platform reads `catalog-info.yaml` files to build the catalog. These files describe your services, APIs, and how they connect to each other.

The platform supports **two formats**:

| Format | Identifier | Status |
|--------|-----------|--------|
| **VSF IDP v2** | `specVersion: vsf-idp.io/v2` | ✅ Primary — use this for new services |
| **Backstage** | `apiVersion: backstage.io/v1alpha1` | ✅ Supported — for migration from Backstage |

Both formats can be used in the same workspace. The validation engine handles each format with its own rules.

---

<div class="grid cards" markdown>

-   :material-star:{ .lg .middle } **VSF IDP v2**

    The primary format for all new services. Includes ownership, review gates, and typed topology.

    [:octicons-arrow-right-24: VSF IDP v2 Reference](vsf-v2.md)

-   :material-swap-horizontal:{ .lg .middle } **Backstage Compatibility**

    How Backstage-format descriptors work alongside VSF IDP v2.

    [:octicons-arrow-right-24: Backstage Guide](backstage.md)

-   :material-key:{ .lg .middle } **Identity Rules**

    How entity identity is computed and what happens with conflicts.

    [:octicons-arrow-right-24: Identity Rules](identity.md)

-   :material-graph:{ .lg .middle } **Topology Fields**

    How to declare connections between services.

    [:octicons-arrow-right-24: Topology Fields](topology.md)

</div>

---

## Quick Example

Here is a minimal valid VSF IDP v2 descriptor:

```yaml
specVersion: vsf-idp.io/v2

metadata:
  namespace: platform
  system: idp-core
  domain: Platform Engineering

spec:
  id: my-service
  name: My Service
  type: service
  owners:
    members:
      - user: alice@vinsmartfuture.tech
        role: techlead
  review:
    branch: main
```

This creates an entity with the canonical reference `component:platform/my-service`.

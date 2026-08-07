---
title: Descriptor Format
description: Guide to authoring catalog-info.yaml descriptor files for the IDP Platform.
---

# :material-file-code-outline: Descriptor Format

All catalog entities are described using `catalog-info.yaml` files placed anywhere within the Catalog Root directory.

---

## :material-layers: Two Supported Formats

The IDP Platform supports two descriptor formats:

<div class="grid cards" markdown>

-   :material-star:{ .lg .middle } **VSF IDP v2** *(Primary)*

    ---

    `specVersion: vsf-idp.io/v2` — the primary authoring contract for all new services.

    Includes ownership, review gates, and structured topology declarations.

    [:octicons-arrow-right-24: VSF IDP v2 Reference](vsf-v2.md)

-   :material-history:{ .lg .middle } **Backstage** *(Legacy / Migration)*

    ---

    Standard Backstage `apiVersion` + `kind` format for components migrating from a Backstage catalog.

    Readable alongside VSF v2 in the same workspace.

    [:octicons-arrow-right-24: Backstage Compatibility](backstage.md)

</div>

---

## :material-folder-search: Discovery Rules

The platform discovers descriptors by:

1. Recursively scanning the `CATALOG_ROOT` directory
2. Including only files named **exactly** `catalog-info.yaml`
3. Excluding hidden directories (names starting with `.`)
4. Excluding common generated directories: `node_modules`, `__pycache__`, `.venv`
5. Never following symlinks or junctions

!!! info "One entity per file"
    Each `catalog-info.yaml` file must contain exactly **one** YAML document with exactly **one** entity descriptor. Multi-document YAML (separated by `---`) is rejected.

---

## :material-format-list-bulleted: YAML Constraints

The parser enforces a **strict YAML 1.2 JSON-compatible subset**:

| ✅ Allowed | ❌ Not Allowed |
|-----------|--------------|
| String scalars | YAML anchors/aliases |
| Boolean (`true`/`false`) | Implicit type coercions (e.g., `yes` → `true`) |
| Integer and float numbers | NaN and Infinity |
| `null` | YAML timestamps as bare values |
| Mappings (objects) | Non-string mapping keys |
| Sequences (arrays) | Duplicate mapping keys |
| Nested structures | Multi-document files |

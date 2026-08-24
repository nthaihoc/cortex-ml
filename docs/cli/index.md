---
title: CLI
description: Command Line Interface for the IDP Platform (Planned).
---

# :material-console: CLI

!!! warning "Planned Feature"
    The CLI is currently in development and not yet available for general use. The documentation below describes the planned design.

The IDP Platform CLI will provide a way to interact with the catalog directly from your terminal, without needing the browser or VS Code. It will be especially useful for CI/CD pipelines to validate catalog files before merging.

---

## Planned Goals

- **CI/CD Validation:** Run `idp validate` in your GitHub Actions or GitLab CI to ensure no broken catalog files are merged.
- **Fast Queries:** Query entities and relations directly from the terminal.
- **Generation:** Scaffold new `catalog-info.yaml` files quickly.

---

<div class="grid cards" markdown>

-   :material-format-list-bulleted-type:{ .lg .middle } **Commands**

    The planned command list and arguments.

    [:octicons-arrow-right-24: Commands](commands.md)

</div>

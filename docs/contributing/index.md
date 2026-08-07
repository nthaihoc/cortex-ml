---
title: Contributing
description: How to contribute to the IDP Platform project.
---

# :material-handshake: Contributing

Thank you for your interest in contributing to **IDP Platform — Local Catalog Topology**!

<div class="grid cards" markdown>

-   :material-source-branch:{ .lg .middle } **Development Workflow**

    Branching strategy, pull request process, and commit conventions.

    [:octicons-arrow-right-24: Workflow](workflow.md)

-   :material-code-braces:{ .lg .middle } **Code Conventions**

    Python, TypeScript, and documentation style guidelines.

    [:octicons-arrow-right-24: Conventions](conventions.md)

</div>

---

## :material-quick-alert-outline: Before You Start

1. Read the [Architecture Overview](../architecture/index.md) to understand the module boundaries
2. Run the full test suite to verify your environment: `python -m pytest` + `npm test`
3. Check existing issues and discussions before opening a new one

---

## :material-bug: Reporting Issues

When reporting a bug, include:

- Operating system and version
- Python and Node.js versions
- The `catalog-info.yaml` content that triggers the issue (if applicable)
- The full diagnostic output or error message
- Steps to reproduce

---

## :material-lightbulb-on-outline: Proposing Features

Open a discussion issue describing:

- The use case or problem it solves
- How it fits within the existing architecture
- Whether it requires changes to the `CatalogWorkspace` core (approach carefully — all catalog semantics live there)

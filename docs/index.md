---
title: IDP Platform — Local Catalog Topology
description: Developer documentation for the VSF IDP v2 Local Catalog Topology platform.
hide:
  - navigation
  - toc
---

# :material-graph-outline: IDP Platform — Local Catalog Topology

<div class="grid cards" markdown>

-   :material-rocket-launch-outline:{ .lg .middle } **Quick Start**

    ---

    Get up and running in minutes with a fresh clone. No database, no containers, no remote services required.

    [:octicons-arrow-right-24: Getting Started](getting-started/index.md)

-   :material-sitemap:{ .lg .middle } **Architecture**

    ---

    Understand the layered design: `CatalogWorkspace` at the core, FastAPI and LSP as adapters, React and VS Code as viewers.

    [:octicons-arrow-right-24: Architecture](architecture/index.md)

-   :material-file-code-outline:{ .lg .middle } **Descriptor Format**

    ---

    Author `catalog-info.yaml` files using VSF IDP v2 with full backward compatibility for Backstage descriptors.

    [:octicons-arrow-right-24: Descriptor Guide](descriptor/index.md)

-   :material-api:{ .lg .middle } **HTTP API**

    ---

    Loopback-only REST API with catalog snapshots, focused topology, diagnostics, and real-time SSE events.

    [:octicons-arrow-right-24: API Reference](api/index.md)

-   :material-microsoft-visual-studio-code:{ .lg .middle } **VS Code Extension**

    ---

    Live validation diagnostics and one-hop topology preview directly inside your editor, powered by a Python LSP server.

    [:octicons-arrow-right-24: Extension Guide](vscode/index.md)

-   :material-gauge:{ .lg .middle } **Performance**

    ---

    Measured benchmarks: 1,000 entities under 2 s startup, 5,000 entities at p95 87 ms focus time.

    [:octicons-arrow-right-24: Performance](performance/index.md)

</div>

---

## :material-information-outline: What is IDP Platform?

**IDP Platform** is a **development-environment vertical slice** for browsing declared VSF IDP v2 catalog topology from local `catalog-info.yaml` files.

It lets engineers **see the declared service graph of their workspace in real time** — in a browser viewer or inside VS Code — with zero external services, zero database, zero authentication, and zero network connection required after initial dependency installation.

```text
catalog-info.yaml files
        │
        ▼
┌─────────────────────────────────────────────────────┐
│                 CatalogWorkspace                     │
│  (YAML parsing → normalization → validation →        │
│   relation projection → conflict detection →         │
│   last-valid state → focused topology)               │
└──────────┬──────────────────────┬───────────────────┘
           │                      │
    ┌──────▼──────┐      ┌────────▼──────────┐
    │  FastAPI    │      │  Python LSP        │
    │  HTTP API   │      │  (stdio)           │
    └──────┬──────┘      └────────┬──────────┘
           │                      │
    ┌──────▼──────┐      ┌────────▼──────────┐
    │  React      │      │  VS Code Extension │
    │  Browser    │      │  + Webview         │
    └─────────────┘      └───────────────────┘
```

!!! info "Design Philosophy"
    **Python owns all catalog semantics.** The HTTP layer and LSP server are thin adapters that translate data shapes. TypeScript and React are pure presentation. This means the same validation engine runs for filesystem scanning, HTTP requests, and editor diagnostics.

---

## :material-feature-search-outline: Key Features

| Feature | Description |
|---|---|
| :material-file-search: **File Discovery** | Recursively discovers all `catalog-info.yaml` files beneath a Catalog Root |
| :material-check-all: **Dual Schema Support** | VSF IDP v2 (`specVersion: vsf-idp.io/v2`) and Backstage descriptors |
| :material-graph: **Topology Graph** | One-hop focused traversal, interactive node navigation |
| :material-stethoscope: **Live Diagnostics** | Structured diagnostics with stable codes, severity, and field-level provenance |
| :material-history: **Last-Valid State** | Previously valid documents remain visible as stale/error during invalid edits |
| :material-alert: **Conflict Detection** | Duplicate canonical entity references surface as conflict nodes |
| :material-eye: **Real-Time Updates** | Filesystem watcher + SSE stream keeps browser state current automatically |
| :material-microsoft-visual-studio-code: **Editor Integration** | LSP diagnostics + topology webview with 300 ms debounce on unsaved changes |
| :material-speedometer: **Performance** | 1,000 entities: < 2 s startup; 5,000 entities: < 90 ms p95 focus time |

---

## :material-map: Project Map

```
idp-platform/
├── backend/            # Python FastAPI + catalog engine
│   └── app/
│       ├── catalog_workspace/   # ← Core: CatalogWorkspace
│       ├── ingest/              # YAML parsing, normalization, relation projection
│       ├── validators/          # Schema + topology validation engine
│       ├── domain/              # Entity, EntityReference, RelationType
│       ├── local_catalog/       # HTTP runtime, file watcher, filesystem adapter
│       └── catalog_language_server/  # stdio LSP + unsaved editor overlay
├── frontend/           # React + ReactFlow browser topology viewer
├── vscode-extension/   # VS Code extension (LSP client + webview host)
├── cli/                # Typer-based catalog CLI
├── openapi/            # OpenAPI 3.1 contract (openapi.yaml)
├── contracts/          # Contract-tested JSON examples
└── docs/               # Existing prose documentation
```

---

## :material-link: References & Further Reading

- [Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/)
- [OpenAPI Specification 3.1](https://spec.openapis.org/oas/v3.1.0)
- [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)
- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [ReactFlow Documentation](https://reactflow.dev/)

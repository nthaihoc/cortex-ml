---
title: Architecture
description: How the IDP Platform is designed and how its components work together.
---

# :material-sitemap: Architecture

The IDP Platform follows a simple rule: **Python owns all catalog logic, TypeScript owns all display.**

This section explains how the system is organized and how data flows through it.

```mermaid
flowchart TD
    subgraph SOURCE["📁 Local Files"]
        FILES["catalog-info.yaml"]
    end

    subgraph CORE["🐍 Python Core"]
        direction TB
        FS["Filesystem Adapter\nDiscovers files, watches for changes"]
        CW["CatalogWorkspace\nParsing → Normalization → Validation\nRelation Projection → Identity Management"]
        FS --> CW
    end

    subgraph ADAPTERS["🔌 Adapters"]
        direction LR
        API["FastAPI HTTP Server\n127.0.0.1:8000"]
        LSP["Language Server\nstdio protocol"]
    end

    subgraph VIEWERS["👁️ Viewers"]
        direction LR
        UI["React Browser Viewer\nVite · port 5173"]
        EXT["VS Code Extension\nWebview + Diagnostics"]
    end

    FILES --> FS
    CW --> API
    CW --> LSP
    API --> UI
    LSP --> EXT

```

---

<div class="grid cards" markdown>

-   :material-view-dashboard-outline:{ .lg .middle } **System Overview**

    All components, their roles, and the repository structure.

    [:octicons-arrow-right-24: System Overview](overview.md)

-   :material-wall:{ .lg .middle } **Module Boundaries**

    Rules about what each component is allowed to do.

    [:octicons-arrow-right-24: Module Boundaries](boundaries.md)

-   :material-pipe:{ .lg .middle } **Data Flow**

    How a `catalog-info.yaml` file goes from disk to the screen.

    [:octicons-arrow-right-24: Data Flow](data-flow.md)

-   :material-state-machine:{ .lg .middle } **State Management**

    How the system manages entities, drafts, conflicts, and stale data.

    [:octicons-arrow-right-24: State Management](state.md)

</div>

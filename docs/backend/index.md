---
title: Backend
description: Python backend components — the core of the IDP Platform.
---

# :material-language-python: Backend

The backend is written in Python and contains all catalog logic. It has five main modules:

```mermaid
flowchart TD
    subgraph BACKEND["Python Backend"]
        CW["CatalogWorkspace\n(Core engine)"]
        IP["Ingest Pipeline\n(Parse, normalize, project)"]
        VE["Validation Engine\n(Schema + topology checks)"]
        LC["Local Catalog Runtime\n(HTTP + file watcher)"]
        LS["Language Server\n(LSP for VS Code)"]

        LC --> CW
        LS --> CW
        CW --> IP
        CW --> VE
    end

```

---

<div class="grid cards" markdown>

-   :material-brain:{ .lg .middle } **CatalogWorkspace**

    The core module. All catalog state lives here.

    [:octicons-arrow-right-24: CatalogWorkspace](catalog-workspace.md)

-   :material-pipe:{ .lg .middle } **Ingest Pipeline**

    YAML parsing, entity normalization, and relation projection.

    [:octicons-arrow-right-24: Ingest Pipeline](ingest-pipeline.md)

-   :material-shield-check:{ .lg .middle } **Validation Engine**

    Schema validation for both VSF IDP v2 and Backstage formats.

    [:octicons-arrow-right-24: Validation Engine](validation.md)

-   :material-server:{ .lg .middle } **Local Catalog Runtime**

    HTTP server (FastAPI) and filesystem discovery.

    [:octicons-arrow-right-24: Local HTTP Runtime](local-catalog.md)

-   :material-file-eye:{ .lg .middle } **File Watcher**

    Detects changes to catalog files and updates the workspace.

    [:octicons-arrow-right-24: File Watcher](file-watcher.md)

</div>

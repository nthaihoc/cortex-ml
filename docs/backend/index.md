---
title: Backend
description: Overview of the Python backend components for the IDP Platform.
---

# :material-language-python: Backend

The backend is a Python application that contains all catalog semantics. It is organized into self-contained modules with clear responsibilities.

<div class="grid cards" markdown>

-   :material-brain:{ .lg .middle } **CatalogWorkspace**

    The deep module. All catalog parsing, validation, relation projection, conflict detection, and topology traversal.

    [:octicons-arrow-right-24: CatalogWorkspace](catalog-workspace.md)

-   :material-pipe:{ .lg .middle } **Ingest Pipeline**

    Three-stage pipeline: YAML parsing → normalization → relation projection.

    [:octicons-arrow-right-24: Ingest Pipeline](ingest-pipeline.md)

-   :material-check-circle-outline:{ .lg .middle } **Validation Engine**

    Schema and topology validation for both VSF IDP v2 and Backstage descriptors.

    [:octicons-arrow-right-24: Validation Engine](validation.md)

-   :material-server:{ .lg .middle } **Local HTTP Runtime**

    FastAPI application, loopback server, and filesystem discovery.

    [:octicons-arrow-right-24: Local Catalog](local-catalog.md)

-   :material-file-eye-outline:{ .lg .middle } **File Watcher**

    Watchfiles-based filesystem watcher with debounce and atomic event batching.

    [:octicons-arrow-right-24: File Watcher](file-watcher.md)

</div>

---

## :material-console: Running the Backend

```bash
cd backend
python -m app.local_catalog
```

This starts the FastAPI server at `http://127.0.0.1:8000` and begins watching `CATALOG_ROOT` for changes.

## :material-test-tube: Running Tests

```bash
cd backend
python -m pytest
```

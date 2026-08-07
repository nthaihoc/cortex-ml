---
title: System Overview
description: Detailed system overview of the IDP Platform components and their interactions.
---

# :material-view-dashboard-outline: System Overview

## :material-package-variant: Component Map

| Component | Location | Language | Role |
|-----------|----------|----------|------|
| **CatalogWorkspace** | `backend/app/catalog_workspace/` | Python | Core domain: all catalog semantics |
| **Ingest Pipeline** | `backend/app/ingest/` | Python | YAML parsing, normalization, relation projection |
| **Validation Engine** | `backend/app/validators/` | Python | Schema + topology validation |
| **Domain Models** | `backend/app/domain/` | Python | Entity, EntityReference, RelationType |
| **Local Catalog Runtime** | `backend/app/local_catalog/` | Python | HTTP adapter + filesystem watcher |
| **Language Server** | `backend/app/catalog_language_server/` | Python | LSP adapter over stdio |
| **Frontend** | `frontend/src/` | TypeScript + React | Browser topology viewer |
| **VS Code Extension** | `vscode-extension/src/` | TypeScript | Editor host + LSP client + webview |
| **CLI** | `cli/` | Python (Typer) | Command-line catalog utilities |
| **OpenAPI Contract** | `openapi/openapi.yaml` | YAML | Canonical HTTP wire contract |

---

## :material-file-tree: Repository Structure

```
idp-platform/
├── .env.example                    # Environment variable template
├── README.md                       # Developer quick-start
├── mkdocs.yml                      # Documentation configuration
│
├── backend/
│   ├── requirements.txt            # Production dependencies
│   ├── requirements-dev.txt        # Development + test dependencies
│   ├── pyproject.toml
│   └── app/
│       ├── catalog_workspace/      # ★ Core domain module
│       │   ├── models.py           # CatalogEntity, Snapshot, Topology, Diagnostics
│       │   ├── workspace.py        # CatalogWorkspace implementation
│       │   └── source_positions.py # Field-path to line/column mapping
│       ├── ingest/
│       │   ├── parser.py           # HardenedYamlParser (YAML 1.2 JSON-subset)
│       │   ├── normalizer.py       # BackstageEntityNormalizer
│       │   └── relation_projector.py  # BackstageRelationProjector
│       ├── validators/
│       │   ├── engine.py           # CatalogValidationEngine (Backstage + VSF v2)
│       │   ├── registry.py         # Issue factories
│       │   └── schemas.py          # ValidationIssue, ValidationReport
│       ├── domain/
│       │   ├── entity.py           # Entity (Pydantic model)
│       │   ├── enums/relation_type.py
│       │   └── value_objects/
│       │       ├── entity_reference.py  # EntityReference (canonical triplet)
│       │       └── relation.py          # Relation value object
│       ├── local_catalog/
│       │   ├── __main__.py         # Entry point: python -m app.local_catalog
│       │   ├── api.py              # FastAPI application factory
│       │   ├── runtime.py          # LocalCatalogRuntime
│       │   ├── filesystem.py       # catalog-info.yaml discovery
│       │   ├── watcher.py          # CatalogFileWatcher + WatchfilesCatalogEventSource
│       │   └── events.py           # CatalogChangeFeed (SSE pub/sub)
│       └── catalog_language_server/
│           ├── __main__.py         # Entry point: python -m app.catalog_language_server
│           ├── server.py           # pygls LSP server setup
│           └── service.py          # CatalogLanguageService
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   └── src/
│       ├── main.tsx                # React root
│       ├── app/App.tsx             # Application shell
│       ├── topology/               # ReactFlow topology viewer
│       │   ├── TopologyViewer.tsx  # Main component
│       │   ├── localContract.ts    # HTTP API client + type mapping
│       │   ├── catalogSearch.ts    # Full-catalog search
│       │   └── types.ts            # Shared TypeScript types
│       └── styles.css
│
├── vscode-extension/
│   ├── package.json                # Extension manifest
│   └── src/
│       ├── extension.ts            # activate/deactivate entry
│       ├── host/controller.ts      # Extension orchestrator
│       └── vscode/
│           ├── vscodeHost.ts       # VS Code API wrapper
│           ├── vscodeLanguageClient.ts  # LSP client
│           ├── webviewHtml.ts      # Webview HTML generator
│           └── webview/            # Shared webview React app
│
├── cli/
│   ├── main.py                     # Typer CLI entry point
│   └── pyproject.toml
│
├── openapi/
│   └── openapi.yaml                # OpenAPI 3.1 canonical contract
│
├── contracts/
│   └── examples/                   # Contract-tested JSON fixtures
│
└── docs/                           # Original prose documentation
```

---

## :material-link: Further Reading

- [Architecture Boundaries](boundaries.md)
- [Data Flow](data-flow.md)
- [State Management](state.md)
- [The "Deep Module" pattern (John Ousterhout)](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign)

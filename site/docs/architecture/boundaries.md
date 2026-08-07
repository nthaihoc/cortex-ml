---
title: Module Boundaries
description: Boundary rules and constraints governing each component of the IDP Platform.
---

# :material-fence: Module Boundaries

Each component in the IDP Platform has well-defined responsibilities and explicit constraints. These boundaries are enforced by the architecture, not by runtime checks alone.

---

## :material-folder-outline: Filesystem Adapter

**Module:** `backend/app/local_catalog/filesystem.py`

| Constraint | Detail |
|------------|--------|
| **Target files** | Only files named exactly `catalog-info.yaml` |
| **Depth** | Unlimited recursive traversal beneath `CATALOG_ROOT` |
| **Excluded directories** | Hidden dirs (`.`-prefixed), `node_modules`, `__pycache__`, `.venv` |
| **Excluded paths** | Symlinks and junctions are never followed |
| **File size limit** | Files > 1 MB are skipped with `CATALOG_DESCRIPTOR_TOO_LARGE` diagnostic |

---

## :material-http: HTTP Adapter

**Module:** `backend/app/local_catalog/api.py`

| Constraint | Detail |
|------------|--------|
| **Bind address** | `127.0.0.1` only — loopback, never 0.0.0.0 |
| **CORS** | Only the configured Vite origin (`http://localhost:5173`) |
| **Methods** | `GET` (read-only) and `PUT` (source update only) |
| **Authentication** | None — loopback-only by design |
| **Source writes** | Limited to discovered `catalog-info.yaml` files |
| **Directory traversal** | Prevented by strict path resolution and `relative_to()` check |
| **Concurrency guard** | SHA-256 `expected_version` for optimistic locking on PUT |
| **Size limit** | PUT requests > 1 MB return `413` |

---

## :material-language-python: Language Server

**Module:** `backend/app/catalog_language_server/`

| Constraint | Detail |
|------------|--------|
| **Transport** | `stdio` only — no network port |
| **Scope** | One `CatalogScope` per language server instance |
| **Document types** | Only files named `catalog-info.yaml` within workspace folders |
| **Unsaved overlays** | Applied after 300 ms debounce; superseded versions are discarded |
| **Depth** | Fixed at `depth=1` for topology requests |
| **Folder management** | Responds to `workspace/didChangeWorkspaceFolders` dynamically |

---

## :material-microsoft-visual-studio-code: VS Code Extension

**Module:** `vscode-extension/src/`

| Constraint | Detail |
|------------|--------|
| **Catalog rules** | Extension does **not** implement any catalog validation rules |
| **Active editor follow** | Updates focus when active editor changes, unless "pinned" |
| **Pin state** | User-controlled; prevents automatic focus changes |
| **Request cancellation** | Superseded in-flight topology requests are cancelled |
| **Message validation** | Webview messages are validated before processing |
| **Trusted workspaces** | Extension does **not** support untrusted workspace mode |

---

## :material-react: React Frontend

**Module:** `frontend/src/`

| Constraint | Detail |
|------------|--------|
| **Catalog rules** | Frontend does **not** implement catalog validation rules |
| **Graph scope** | Only mounts nodes returned by the focused topology response |
| **Search** | Can use the full catalog snapshot index |
| **Navigation** | Click a related node to make it the new focused root |
| **Real-time** | SSE-driven refetch; no semantic delta application |

---

## :material-brain: CatalogWorkspace

**Module:** `backend/app/catalog_workspace/`

| Constraint | Detail |
|------------|--------|
| **Storage** | Purely in-memory; no persistence |
| **Concurrency** | Single-threaded; callers are responsible for serialization |
| **Traversal depth** | Fixed at 1 hop (enforced in `focused_topology()`) |
| **Authority** | If two documents claim the same canonical reference → conflict; neither wins |
| **Invariants** | A document with no valid snapshot is a "draft"; a valid-then-invalid document remains as "stale/last-valid" |

---

## :material-transfer: Naming Conventions Across Boundaries

| Boundary | Convention | Example |
|----------|-----------|---------|
| Python internal | `snake_case` | `entity_ref`, `source_uri` |
| HTTP API (`openapi.yaml`) | `snake_case` | `entity_count`, `relative_path` |
| LSP custom methods | `camelCase` | `catalogRevision`, `changedDocumentUri` |
| Webview protocol | `camelCase` | `displayName`, `relationType` |

!!! info "Explicit mappers"
    `service.py` in the language server explicitly maps Python `snake_case` fields to `camelCase` for the LSP/extension boundary. Contract fixtures in `contracts/examples/` test these translations.

---

## :material-link: Further Reading

- [Architecture Overview](index.md)
- [OpenAPI Specification](../api/endpoints.md)
- [Language Server Protocol](../lsp/protocol.md)
- [Security in FastAPI](https://fastapi.tiangolo.com/tutorial/security/)

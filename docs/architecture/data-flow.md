---
title: Data Flow
description: How a catalog-info.yaml file goes from disk to the screen, step by step.
---

# :material-pipe: Data Flow

This page shows exactly how data moves through the system — from a `catalog-info.yaml` file on your disk to the topology graph in your browser or editor.

---

## Browser Data Flow

When you use the browser viewer, data flows through the **HTTP stack**:

```mermaid
sequenceDiagram
    participant Disk as 📄 Disk
    participant FS as Filesystem Adapter
    participant CW as CatalogWorkspace
    participant API as FastAPI Server
    participant Browser as ⚛️ React Viewer

    Note over Disk, Browser: Startup
    FS->>Disk: Discover catalog-info.yaml files
    Disk-->>FS: File list + content
    FS->>CW: upsert_document() for each file
    CW->>CW: Parse → Normalize → Validate → Store

    Note over Disk, Browser: Browser opens
    Browser->>API: GET /api/v1/catalog/topology?root=...
    API->>CW: focused_topology()
    CW-->>API: FocusedTopology (nodes + relations)
    API-->>Browser: JSON response
    Browser->>Browser: Render graph with ReactFlow

    Note over Disk, Browser: File saved on disk
    FS->>Disk: Detect change (watchfiles)
    FS->>CW: upsert_document() with new content
    CW->>CW: Re-validate, update state
    API-->>Browser: SSE event: revision changed
    Browser->>API: Re-fetch topology
    API-->>Browser: Updated JSON
```

---

## VS Code Data Flow

When you use the VS Code extension, data flows through the **LSP stack**:

```mermaid
sequenceDiagram
    participant Disk as 📄 Disk
    participant Service as CatalogLanguageService
    participant CW as CatalogWorkspace
    participant LSP as LSP Server (pygls)
    participant VSCode as 💻 VS Code

    Note over Disk, VSCode: Extension starts
    VSCode->>LSP: initialize (workspace folders)
    LSP->>Service: initialize()
    Service->>Disk: Discover catalog-info.yaml files
    Service->>CW: upsert_document() for each file

    Note over Disk, VSCode: User opens a file
    VSCode->>LSP: textDocument/didOpen
    LSP->>Service: did_open()
    Service->>CW: upsert_document()
    CW->>CW: Parse → Normalize → Validate
    Service-->>LSP: Diagnostics
    LSP-->>VSCode: publishDiagnostics

    Note over Disk, VSCode: User types (unsaved changes)
    VSCode->>LSP: textDocument/didChange
    LSP->>Service: did_change()
    Service->>Service: Wait 300ms (debounce)
    Service->>CW: upsert_document() with buffer content
    CW->>CW: Re-validate
    Service-->>LSP: Updated diagnostics
    LSP-->>VSCode: publishDiagnostics + revisionChanged

    Note over Disk, VSCode: User requests topology
    VSCode->>LSP: catalog/topologyForDocument
    LSP->>Service: topology_for_document()
    Service->>CW: focused_topology_for_document()
    CW-->>Service: FocusedTopology
    Service-->>LSP: Topology + diagnostics
    LSP-->>VSCode: JSON response
    VSCode->>VSCode: Render in webview
```

---

## Document Processing Pipeline

Every time a document enters the system (from disk or editor), it goes through the same pipeline:

```mermaid
flowchart TD
    INPUT["Raw bytes from file or editor"] --> PARSE["1. Parse YAML\n(HardenedYamlParser)"]
    PARSE -->|Parse error| FAIL["Record failure\n→ Draft or Stale"]
    PARSE -->|OK| VALIDATE["2. Validate Schema\n(CatalogValidationEngine)"]
    VALIDATE -->|Blocking errors| FAIL
    VALIDATE -->|OK| NORMALIZE["3. Normalize Entity\n(BackstageEntityNormalizer)"]
    NORMALIZE -->|Error| FAIL
    NORMALIZE -->|OK| PROJECT["4. Project Relations\n(BackstageRelationProjector)"]
    PROJECT --> RESOLVE["5. Resolve Identity\n(Authority + Conflict detection)"]
    RESOLVE --> STORE["6. Store in Snapshot\n(Increment revision)"]

```

### What happens at each step:

| Step | Module | Input | Output |
|------|--------|-------|--------|
| 1. Parse | `HardenedYamlParser` | Raw bytes | Python dict (or parse error) |
| 2. Validate | `CatalogValidationEngine` | Python dict | `ValidationOutcome` with issues |
| 3. Normalize | `BackstageEntityNormalizer` | Python dict | Typed `Entity` with canonical ref |
| 4. Project | `BackstageRelationProjector` | `Entity` | List of `Relation` objects |
| 5. Resolve | `CatalogWorkspace` | `Entity` + ref | Update candidate map, detect conflicts |
| 6. Store | `CatalogWorkspace` | Everything | Increment revision counter |

---

## What Happens When a File Changes

When the file watcher detects a change to a `catalog-info.yaml` file:

1. **Debounce** — Wait 300 ms in case more changes are coming
2. **Read** — Read the file content from disk
3. **Process** — Run the full pipeline above (parse → validate → normalize → project → resolve)
4. **Notify** — Publish a `CatalogChangeNotification` with the new revision and affected URIs
5. **SSE** — The HTTP API sends the notification to any connected browser via Server-Sent Events
6. **LSP** — The Language Server sends a `catalog/revisionChanged` notification to VS Code

---

## Further Reading

- [CatalogWorkspace](../backend/catalog-workspace.md) — How the core module processes documents
- [Ingest Pipeline](../backend/ingest-pipeline.md) — Details of parsing, normalization, and projection
- [State Management](state.md) — How entities, drafts, and conflicts are tracked

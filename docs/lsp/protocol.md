---
title: LSP Protocol
description: Standard LSP lifecycle events handled by the catalog language server.
---

# :material-protocol: LSP Protocol

The catalog language server implements standard LSP lifecycle events to maintain the workspace state and provide catalog diagnostics.

---

## :material-power: Initialization — `initialize`

When the VS Code extension initializes the language server:

```json
{
  "method": "initialize",
  "params": {
    "workspaceFolders": [
      { "uri": "file:///path/to/workspace", "name": "workspace" }
    ]
  }
}
```

**Service behavior:**
- Creates one `CatalogWorkspace` covering all workspace folders as a single `CatalogScope`
- Discovers and loads all `catalog-info.yaml` files in every workspace folder
- Publishes initial diagnostics for all loaded documents

---

## :material-folder-multiple: Workspace Folder Changes — `workspace/didChangeWorkspaceFolders`

When folders are added or removed:

- **Added folders:** Discovered and loaded; workspace scope updated
- **Removed folders:** Their documents are removed from the workspace
- The `catalog/revisionChanged` notification is sent after the scope update

---

## :material-file-plus: Document Opened — `textDocument/didOpen`

```json
{
  "method": "textDocument/didOpen",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/catalog-info.yaml",
      "version": 1,
      "text": "specVersion: vsf-idp.io/v2\n..."
    }
  }
}
```

- Registers the document in the open-documents map
- Schedules debounced analysis of the in-memory content
- Only `catalog-info.yaml` files within workspace roots are processed

---

## :material-file-edit: Document Changed — `textDocument/didChange`

- Updates the in-memory buffer with the latest text
- Schedules debounced analysis
- Older (lower version) changes are silently ignored

---

## :material-content-save: Document Saved — `textDocument/didSave`

- Updates the in-memory buffer with saved content
- Re-schedules analysis to ensure the on-disk version is processed
- Adds the document URI to the root's known sources set

---

## :material-file-remove: Document Closed — `textDocument/didClose`

- Removes the in-memory overlay
- Reloads the on-disk file and re-upserts it into the workspace
- If the file no longer exists, removes the document from the workspace
- Publishes diagnostics clearing the unsaved version

---

## :material-stethoscope: Diagnostics — `textDocument/publishDiagnostics`

After any document change, the service publishes diagnostics for **all affected documents**:

```json
{
  "method": "textDocument/publishDiagnostics",
  "params": {
    "uri": "file:///path/to/catalog-info.yaml",
    "version": 5,
    "diagnostics": [
      {
        "range": {
          "start": { "line": 10, "character": 2 },
          "end": { "line": 10, "character": 2 }
        },
        "severity": 1,
        "code": "SCHEMA_FIELD_REQUIRED",
        "source": "local-catalog",
        "message": "spec.owners.members requires at least one techlead",
        "data": { ... }
      }
    ]
  }
}
```

**Severity mapping:**

| Code | LSP Severity | Description |
|------|-------------|-------------|
| 1 | Error | Blocking diagnostic |
| 2 | Warning | Non-blocking diagnostic |

---

## :material-link: Further Reading

- [Custom Methods](custom-methods.md)
- [LSP Specification — Lifecycle](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#lifeCycleMessages)
- [LSP Specification — textDocument/publishDiagnostics](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_publishDiagnostics)
- [pygls Documentation](https://pygls.readthedocs.io/)

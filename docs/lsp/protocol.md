---
title: LSP Protocol
description: Standard LSP lifecycle events handled by the catalog language server.
---

# :material-swap-horizontal: LSP Protocol Events

The Catalog Language Server handles standard LSP lifecycle events to track file changes and publish diagnostics.

**Location:** `backend/app/catalog_language_server/server.py`

---

## Initialization (`initialize`)

When the VS Code extension starts the server, it sends an `initialize` request containing the workspace folders.

**What the server does:**

1. Reads the workspace folder URIs
2. Uses the `filesystem` module to discover all `catalog-info.yaml` files in those folders
3. Loads all discovered files into the `CatalogWorkspace`
4. Responds that it is ready

---

## Document Opened (`textDocument/didOpen`)

When you open a `catalog-info.yaml` file in VS Code.

**What the server does:**

1. Reads the file content from the message (VS Code sends the content)
2. Calls `workspace.upsert_document()`
3. Formats any issues as LSP `Diagnostic` objects
4. Sends a `textDocument/publishDiagnostics` notification back to VS Code

---

## Document Changed (`textDocument/didChange`)

When you type in a `catalog-info.yaml` file (before saving).

**What the server does:**

1. **Debounce:** Waits ~300 ms after your last keystroke to avoid validating every single letter
2. Calls `workspace.upsert_document()` with the new unsaved content
3. Sends updated diagnostics via `textDocument/publishDiagnostics`
4. Sends a custom `catalog/revisionChanged` notification (see [Custom Methods](custom-methods.md))

!!! success "Live Validation"
    Because the server uses the exact same `CatalogWorkspace` as the HTTP API, you get the same validation errors while typing that you would get after saving.

---

## Document Closed (`textDocument/didClose`)

When you close a file in VS Code without saving.

**What the server does:**

1. Drops the unsaved buffer content
2. Reloads the actual file content from disk
3. Calls `workspace.upsert_document()` with the disk content
4. Publishes updated diagnostics

---

## Diagnostics Format

When the server sends diagnostics to VS Code, it maps our `CatalogDiagnostic` to the LSP `Diagnostic` format:

| Catalog Field | LSP Field | How it maps |
|---------------|-----------|-------------|
| `severity` | `severity` | `error` → `Error` (1), `warning` → `Warning` (2) |
| `message` | `message` | The human-readable message |
| `code` | `code` | Our string code (e.g., `SCHEMA_FIELD_REQUIRED`) |
| `provenance` | `range` | We map the JSON path (e.g., `spec.owners`) to a line and column range in the text |

If a diagnostic has no specific `field_path` (like a general YAML syntax error), it is highlighted on line 1.

---

## Further Reading

- [Custom Methods](custom-methods.md)
- [Validation Engine](../backend/validation.md)

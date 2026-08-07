---
title: Language Server
description: Python Language Server Protocol (LSP) implementation for catalog descriptor validation.
---

# :material-language-python: Language Server

The Python Language Server (`backend/app/catalog_language_server/`) provides live catalog validation diagnostics and topology preview directly inside VS Code via the Language Server Protocol (LSP).

<div class="grid cards" markdown>

-   :material-protocol:{ .lg .middle } **Protocol**

    Standard LSP lifecycle events and how the language service responds.

    [:octicons-arrow-right-24: Protocol](protocol.md)

-   :material-code-braces-box:{ .lg .middle } **Custom Methods**

    The `catalog/topologyForDocument` request and `catalog/revisionChanged` notification.

    [:octicons-arrow-right-24: Custom Methods](custom-methods.md)

</div>

---

## :material-console: Starting the Language Server

The language server is started by the VS Code extension automatically:

```bash
python -m app.catalog_language_server
```

It communicates over **stdio** (stdin/stdout). No network ports are used.

---

## :material-key-chain: Key Design Points

1. **Same validation engine** — uses `CatalogWorkspace` + `CatalogValidationEngine`, the same as the HTTP runtime
2. **Unsaved editor overlays** — in-memory document buffers shadow on-disk files
3. **300 ms debounce** — avoids excessive re-validation during typing
4. **Cross-folder catalog scope** — all VS Code workspace folders contribute to one `CatalogWorkspace`
5. **Diagnostics push** — diagnostics are published via `textDocument/publishDiagnostics` notifications

---

## :material-link: Further Reading

- [Language Server Protocol Specification](https://microsoft.github.io/language-server-protocol/)
- [pygls Documentation](https://pygls.readthedocs.io/)
- [VS Code Extension](../vscode/index.md)

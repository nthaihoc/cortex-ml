---
title: VS Code Extension
description: Local Catalog Topology extension for VS Code.
---

# :material-microsoft-visual-studio-code: VS Code Extension

The IDP Platform includes a VS Code extension that brings the catalog directly into your editor. It provides **live diagnostics** (squiggly lines for errors) and a **topology webview** that updates as you type.

**Location:** `vscode-extension/`

---

<div class="grid cards" markdown>

-   :material-download-circle-outline:{ .lg .middle } **Installation**

    How to build and install the extension (`.vsix`) in your editor.

    [:octicons-arrow-right-24: Installation](installation.md)

-   :material-keyboard:{ .lg .middle } **Commands**

    All available VS Code commands provided by the extension.

    [:octicons-arrow-right-24: Commands](commands.md)

-   :material-cog-outline:{ .lg .middle } **Configuration**

    Settings for Python paths and server directories.

    [:octicons-arrow-right-24: Configuration](configuration.md)

-   :material-swap-horizontal:{ .lg .middle } **Webview Protocol**

    How the extension host talks to the React webview.

    [:octicons-arrow-right-24: Webview Protocol](webview-protocol.md)

</div>

---

## How it Works

The extension acts as a client for the [Language Server](../lsp/index.md). 

1. When it activates, it starts the Python LSP server in the background.
2. It sends your unsaved typing to the server.
3. The server runs the full `CatalogValidationEngine`.
4. The extension shows the resulting diagnostics in your editor.
5. The webview uses the custom `catalog/topologyForDocument` method to render the ReactFlow graph.

Because it uses the same Python core as the HTTP API, **validation is identical everywhere**.

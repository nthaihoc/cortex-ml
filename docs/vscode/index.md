---
title: VS Code Extension
description: Local Catalog Topology VS Code extension for live catalog validation and topology preview.
---

# :material-microsoft-visual-studio-code: VS Code Extension

The **Local Catalog Topology** VS Code extension provides:

- :material-check-circle: **Live diagnostics** for `catalog-info.yaml` files (via LSP)
- :material-graph: **One-hop topology webview** beside the active editor
- :material-pin: **Pin focus** to lock the topology on a specific entity

<div class="grid cards" markdown>

-   :material-download:{ .lg .middle } **Installation**

    Build and install the extension locally.

    [:octicons-arrow-right-24: Installation](installation.md)

-   :material-keyboard:{ .lg .middle } **Commands**

    Available VS Code commands and keyboard shortcuts.

    [:octicons-arrow-right-24: Commands](commands.md)

-   :material-cog:{ .lg .middle } **Configuration**

    Python path and working directory settings.

    [:octicons-arrow-right-24: Configuration](configuration.md)

-   :material-web:{ .lg .middle } **Webview Protocol**

    Message protocol between the extension host and the webview.

    [:octicons-arrow-right-24: Webview Protocol](webview-protocol.md)

</div>

---

## :material-information-outline: Extension Metadata

| Property | Value |
|----------|-------|
| Display Name | Local Catalog Topology |
| Extension ID | `local.local-catalog-topology-vscode` |
| VS Code Engine | ^1.91.0 |
| Category | Visualization |
| Activation | On YAML files or workspace containing `catalog-info.yaml` |
| Trusted Workspaces | Not supported |

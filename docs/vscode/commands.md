---
title: VS Code Commands
description: Available VS Code commands provided by the Local Catalog Topology extension.
---

# :material-keyboard: VS Code Commands

The extension registers three commands in the VS Code Command Palette. You can find them by pressing ++ctrl+shift+p++ (++cmd+shift+p++ on Mac) and typing "Catalog".

---

## `Catalog: Open Topology Beside`

**Command ID:** `catalogTopology.openBeside`

Opens the Topology Webview in a new editor column next to your current file.

- **What it does:** Shows the one-hop topology graph for the `catalog-info.yaml` file you are currently editing.
- **Live updates:** As you type in the YAML file, the graph updates automatically (after a 300 ms debounce).
- **Draft mode:** If the file has errors, the graph will show a "Draft" node instead of the full entity.

---

## `Catalog: Open Focused Source`

**Command ID:** `catalogTopology.openSource`

Opens the source YAML file for whatever node is currently selected in the webview.

- **How to use:** First, click a node in the webview graph. Then run this command (or double-click the node, if supported).
- **What it does:** It asks the backend for the `source_uri` of the selected entity and opens that file in VS Code. If the file is outside the current VS Code workspace, it may prompt you.

---

## `Catalog: Restart Language Server`

**Command ID:** `catalogTopology.restartLanguageServer`

Force-restarts the Python LSP server process in the background.

- **When to use:**
    - If the server crashes or stops responding
    - If you changed the Python path in settings
    - If you just installed new Python dependencies
- **What it does:** Kills the old Python process, starts a new one, and re-sends the `initialize` message with your workspace folders.

---

## Further Reading

- [Language Server Protocol](../lsp/protocol.md) — How the extension talks to the server
- [Configuration](configuration.md) — Settings that affect these commands

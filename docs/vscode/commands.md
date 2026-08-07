---
title: VS Code Commands
description: Available VS Code commands provided by the Local Catalog Topology extension.
---

# :material-keyboard: VS Code Commands

The extension contributes three commands to the VS Code command palette.

---

## :material-graph: `Catalog: Open Topology Beside`

**Command ID:** `catalogTopology.openBeside`

Opens the topology webview panel beside the currently focused `catalog-info.yaml` editor.

**How to use:**
1. Open a `catalog-info.yaml` file in the editor
2. Open the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
3. Run **"Catalog: Open Topology Beside"**

A topology panel appears beside the editor, showing the one-hop topology graph centered on the focused descriptor.

---

## :material-file-eye: `Catalog: Open Focused Source`

**Command ID:** `catalogTopology.openSource`

Navigates the editor to the source file of the currently focused topology node.

---

## :material-restart: `Catalog: Restart Language Server`

**Command ID:** `catalogTopology.restartLanguageServer`

Restarts the Python LSP server process. Use this if:

- The language server crashes unexpectedly
- You've updated the backend virtual environment
- Diagnostics are stale or not appearing

---

## :material-pin: Pin / Unpin Focus

The topology panel includes a **Pin Focus** toggle that prevents the active editor from automatically updating the focused topology root. When pinned:

- The topology stays on the current root
- Active editor changes do not update the graph
- Click **Unpin** to resume active-editor following

---

## :material-activation: Activation Events

The extension activates automatically when:

| Trigger | Description |
|---------|-------------|
| `workspaceContains:catalog-info.yaml` | Workspace has a catalog descriptor |
| `workspaceContains:**/catalog-info.yaml` | Any nested descriptor |
| `onLanguage:yaml` | A YAML file is opened |
| `onCommand:catalogTopology.*` | Any catalog command is run |

---

## :material-link: Further Reading

- [Extension Configuration](configuration.md)
- [VS Code Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)

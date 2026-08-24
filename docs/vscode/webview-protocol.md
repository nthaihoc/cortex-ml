---
title: Webview Protocol
description: Message protocol between the VS Code extension host and the topology webview.
---

# :material-swap-horizontal: Webview Protocol

The VS Code extension is split into two parts that cannot share memory:
1. **The Extension Host** (has access to VS Code APIs and the Language Server)
2. **The Webview** (a secure iframe running React)

They communicate by sending JSON messages back and forth using `postMessage`.

**Location:** `vscode-extension/src/webview/protocol.ts`

---

## Host to Webview Messages

The extension host sends these messages to the webview:

### `update_topology`

Sent when the topology data changes (e.g., after you type, or when the server pushes a new revision).

```typescript
{
  type: "update_topology";
  payload: {
    topology: FocusedTopology; // The graph data
    revision: number;          // The catalog revision
  };
}
```

### `update_diagnostics`

Sent when the validation engine reports errors or warnings for the focused file.

```typescript
{
  type: "update_diagnostics";
  payload: {
    diagnostics: CatalogDiagnostic[];
  };
}
```

---

## Webview to Host Messages

The webview sends these messages to the extension host:

### `ready`

Sent once when the React app has finished mounting and is ready to receive data.

```typescript
{
  type: "ready";
}
```
*When the host receives this, it immediately fetches the initial topology and sends an `update_topology` message.*

### `focus_node`

Sent when the user clicks a node in the ReactFlow graph.

```typescript
{
  type: "focus_node";
  payload: {
    reference: string; // The canonical entity reference
  };
}
```
*When the host receives this, it asks the Language Server for the topology around this new reference.*

### `open_source`

Sent when the user requests to see the source YAML file for a node (e.g., via a double-click or context menu).

```typescript
{
  type: "open_source";
  payload: {
    reference: string;
  };
}
```
*When the host receives this, it executes the `catalogTopology.openSource` command.*

---

## Further Reading

- [Custom LSP Methods](../lsp/custom-methods.md) — How the host gets this data from Python
- [Topology Viewer](../frontend/topology-viewer.md) — The React component running inside the webview

---
title: Custom LSP Methods
description: Custom catalog/topologyForDocument and catalog/revisionChanged methods.
---

# :material-call-made: Custom LSP Methods

In addition to standard LSP methods, the server implements two custom methods specifically for the topology webview in VS Code.

---

## `catalog/topologyForDocument`

**Direction:** Client (VS Code) ➔ Server (Python)

This method asks the server for the topology graph centered around a specific file, even if that file is currently invalid.

### Request Payload

```json
{
  "uri": "file:///path/to/catalog-info.yaml",
  "direction": "both"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `uri` | `string` | The document URI to focus on |
| `direction` | `string` | `"incoming"`, `"outgoing"`, or `"both"` |

### Response Payload

The response contains both the topology and the diagnostics for that file.

```json
{
  "topology": {
    "root": "component:platform/my-service",
    "direction": "both",
    "depth": 1,
    "nodes": { ... },
    "relations": [ ... ]
  },
  "diagnostics": [
    {
      "code": "SCHEMA_FIELD_REQUIRED",
      "severity": "error",
      "message": "...",
      "blocking": true
    }
  ]
}
```

If the document is a **draft** (it was never valid and has no computed entity reference yet), `topology.root` will be `null`, but the diagnostics will still be returned.

---

## `catalog/revisionChanged`

**Direction:** Server (Python) ➔ Client (VS Code)

This is a **notification** (no response expected). The server sends this whenever the catalog state changes (e.g., after the 300 ms debounce when you type).

### Notification Payload

```json
{
  "revision": 45
}
```

| Field | Type | Description |
|-------|------|-------------|
| `revision` | `integer` | The new catalog revision number |

### How VS Code Uses It

When the VS Code extension receives this notification, it tells the open webview panel to **refetch** its topology. This is what makes the topology graph update in real-time as you type, without saving the file.

---

## Further Reading

- [LSP Protocol Events](protocol.md)
- [Webview Protocol](../vscode/webview-protocol.md) — How the extension talks to the webview

---
title: Custom LSP Methods
description: Custom catalog/topologyForDocument and catalog/revisionChanged methods.
---

# :material-code-braces-box: Custom LSP Methods

Beyond standard LSP, the catalog language server defines two custom methods for topology and revision tracking.

---

## :material-arrow-right-circle: `catalog/topologyForDocument` — Request

Returns the one-hop focused topology for the currently focused editor document.

### Request Parameters

```json
{
  "uri": "file:///path/to/catalog-info.yaml",
  "focus": null,
  "direction": "both",
  "depth": 1
}
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `uri` | `string (uri)` | ✅ | — | URI of the active editor document |
| `focus` | `string \| null` | — | `null` | Override the focused entity reference |
| `direction` | `string` | — | `"both"` | `"incoming"`, `"outgoing"`, or `"both"` |
| `depth` | `integer` | — | `1` | Must be exactly `1` |

### Response

```json
{
  "focus": {
    "kind": "entity",
    "entityRef": "component:platform/payment-gateway"
  },
  "topology": {
    "root": "component:platform/payment-gateway",
    "direction": "both",
    "depth": 1,
    "nodes": [
      {
        "reference": "component:platform/payment-gateway",
        "displayName": "Payment Gateway Service",
        "state": "entity",
        "health": "healthy",
        "freshness": "current",
        "provenance": { "..." : "..." },
        "conflictSources": [],
        "componentType": "service",
        "system": "system:default/payments",
        "owners": ["alice@vinsmartfuture.tech"]
      }
    ],
    "relations": [ ... ]
  },
  "diagnostics": [ ... ],
  "diagnosticGroups": [ ... ],
  "catalogRevision": 42
}
```

!!! note "camelCase boundary"
    The custom method response uses `camelCase` field names (not `snake_case`). This is an explicit mapping applied in `service.py` to match TypeScript conventions.

### Focus Object

| `focus.kind` | Condition | Fields |
|-------------|-----------|--------|
| `"entity"` | Document resolves to a valid entity | `entityRef` |
| `"draft"` | Document is a draft (never-valid or unsaved) | `documentUri` |

---

## :material-bell-outline: `catalog/revisionChanged` — Notification

Sent by the server to the extension whenever the catalog revision changes.

```json
{
  "revision": 43,
  "changedDocumentUri": "file:///path/to/catalog-info.yaml"
}
```

Or after workspace folder changes:

```json
{
  "revision": 43,
  "workspaceFolderUris": [
    "file:///path/to/workspace1",
    "file:///path/to/workspace2"
  ]
}
```

**Extension behavior on receipt:**
- Refetch `catalog/topologyForDocument` for the currently visible topology panel
- Update the catalog revision in the webview state

---

## :material-link: Further Reading

- [Protocol](protocol.md)
- [VS Code Extension Webview Protocol](../vscode/webview-protocol.md)
- [LSP Specification — Custom Methods](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#dollarRequests)

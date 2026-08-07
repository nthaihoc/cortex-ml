---
title: Webview Protocol
description: Message protocol between the VS Code extension host and the topology webview.
---

# :material-web: Webview Protocol

The VS Code extension uses a typed message protocol to communicate between the **extension host** (TypeScript) and the **webview** (React component).

---

## :material-arrow-down-bold: Host → Webview Messages

### `topology-update`

Sent by the extension host when the topology data changes.

```typescript
{
  type: "topology-update",
  topology: {
    focus: {
      kind: "entity" | "draft",
      entityRef?: string,    // when kind === "entity"
      documentUri?: string,  // when kind === "draft"
    },
    topology: {
      root: string,
      direction: "incoming" | "outgoing" | "both",
      depth: number | null,
      nodes: TopologyNode[],
      relations: CatalogRelation[],
    },
    diagnostics: DiagnosticPayload[],
    diagnosticGroups: DiagnosticGroup[],
    catalogRevision: number,
  }
}
```

### `pin-state`

Sent when the pin state changes.

```typescript
{
  type: "pin-state",
  pinned: boolean
}
```

---

## :material-arrow-up-bold: Webview → Host Messages

### `node-click`

Sent when the user clicks a topology node to navigate to it.

```typescript
{
  type: "node-click",
  reference: string  // canonical entity reference
}
```

### `open-source`

Sent when the user requests to open a source file.

```typescript
{
  type: "open-source",
  uri: string  // file URI
}
```

### `toggle-pin`

Sent when the user toggles the pin focus button.

```typescript
{
  type: "toggle-pin"
}
```

---

## :material-shield-check: Message Validation

All messages received by the extension host are validated before processing:

- Unknown message types are silently discarded
- Required fields are checked for presence and type
- Malformed messages log a warning and are ignored

---

## :material-information-outline: camelCase Convention

The webview protocol uses `camelCase` throughout (matching TypeScript conventions). The extension host maps between LSP `camelCase` custom method responses and the webview message format, while diagnostic `snake_case` provenance fields are mapped to `camelCase` equivalents.

---

## :material-link: Further Reading

- [Custom LSP Methods](../lsp/custom-methods.md)
- [VS Code Webview API](https://code.visualstudio.com/api/extension-guides/webview)
- [Extension Architecture](../architecture/index.md)

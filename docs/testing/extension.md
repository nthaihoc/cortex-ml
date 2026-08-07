---
title: Extension Tests
description: TypeScript VS Code extension test suite.
---

# :material-microsoft-visual-studio-code: Extension Tests

The VS Code extension test suite uses **Vitest** and **Testing Library** to test the extension host logic and webview React component independently of the VS Code API.

---

## :material-run: Running Tests

```bash
cd vscode-extension

# Run tests once
npm test

# Watch mode
npm run test:watch

# TypeScript type-check
npm run check

# Build the extension bundle
npm run build
```

---

## :material-folder: Test Organization

Tests in the `vscode-extension/` cover:

| Area | What It Tests |
|------|--------------|
| **Extension activation** | Language client starts, topology opens beside the editor |
| **Message validation** | Webview messages are validated and invalid shapes rejected |
| **Active editor follow** | Topology updates when active `catalog-info.yaml` changes |
| **Pin state** | Focus holds when pinned; resumes when unpinned |
| **Draft rekey** | Graph canvas stays mounted when a draft entity gets a canonical reference |
| **LSP → webview mapping** | `lsp-topology-response.json` fixture is correctly mapped for the webview |
| **Webview → host messages** | `webview-topology-update.json` fixture is validated correctly |
| **Cross-folder scope** | Initialization builds one cross-folder catalog scope |

---

## :material-file-document: Contract Fixtures

The extension tests validate against two canonical JSON fixtures:

| Fixture | Purpose |
|---------|---------|
| `contracts/examples/lsp-topology-response.json` | Canonical LSP `catalog/topologyForDocument` response shape |
| `contracts/examples/webview-topology-update.json` | Canonical webview `topology-update` message shape |

Python integration tests **generate** the LSP fixture; extension tests **validate and map** both fixtures before they reach React.

---

## :material-link: Further Reading

- [Acceptance Coverage](acceptance.md)
- [Webview Protocol](../vscode/webview-protocol.md)
- [Custom LSP Methods](../lsp/custom-methods.md)
- [Vitest Documentation](https://vitest.dev/)

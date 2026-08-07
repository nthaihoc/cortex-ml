---
title: Extension Installation
description: Building and installing the Local Catalog Topology VS Code extension.
---

# :material-download: Extension Installation

---

## :material-wrench: Build from Source

```bash
cd vscode-extension
npm install
npm run build
```

This produces `dist/extension.js` via esbuild.

---

## :material-play: Development Mode (F5)

1. Open the **`idp-platform` root folder** in VS Code
2. Select **"Run Local Catalog Topology Extension"** in the Run & Debug panel
3. Press **`F5`**

A new **Extension Development Host** window opens with the extension loaded.

---

## :material-package-variant: Install as VSIX

A pre-built VSIX is included in the repository:

```bash
code --install-extension vscode-extension/local-catalog-topology-0.1.0.vsix
```

Or from within VS Code: **Extensions** panel → **...** → **Install from VSIX...**

---

## :material-alert-outline: Requirements

| Requirement | Version |
|-------------|---------|
| VS Code | ≥ 1.91.0 |
| Python | ≥ 3.12 |
| Backend `.venv` | Must have `requirements.txt` installed |
| Node.js | ≥ 20 (only for building from source) |

---

## :material-link: Further Reading

- [VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)
- [VSCE — VS Code Extension Manager](https://github.com/microsoft/vscode-vsce)

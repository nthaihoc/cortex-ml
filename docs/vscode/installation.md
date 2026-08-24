---
title: Extension Installation
description: Building and installing the Local Catalog Topology VS Code extension.
---

# :material-download-circle-outline: Extension Installation

This guide explains how to build and install the VS Code extension for your own use.

---

## Step 1: Build the Extension

You need Node.js installed to build the extension.

1. Open your terminal
2. Navigate to the extension folder:
   ```bash
   cd idp-platform/vscode-extension
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Build the extension package (`.vsix` file):
   ```bash
   npx vsce package
   ```

You should now see a file named something like `local-catalog-topology-vscode-0.1.0.vsix` in the directory.

---

## Step 2: Install in VS Code

### Method A: Using the Command Palette

1. Open VS Code
2. Open the Command Palette (++ctrl+shift+p++ or ++cmd+shift+p++ on Mac)
3. Type **Extensions: Install from VSIX...** and select it
4. Find the `.vsix` file you just built and select it
5. Reload VS Code if prompted

### Method B: Using the CLI

If you have the `code` CLI tool installed, you can install it directly from your terminal:

```bash
code --install-extension local-catalog-topology-vscode-0.1.0.vsix
```

---

## Step 3: Verify it Works

1. Open a folder in VS Code that contains a `catalog-info.yaml` file
2. Open the `catalog-info.yaml` file
3. Look at the bottom-right corner of VS Code — you should see the Language Server start up
4. Open the Command Palette and run **Catalog: Open Topology Beside**

If the topology webview appears and shows your entity, the installation was successful!

---

## Troubleshooting

**"Language Server failed to start"**
The extension needs to find a Python environment to run the server. See [Configuration](configuration.md) to set the correct Python path.

**"Command not found"**
Make sure you are editing a file named `catalog-info.yaml` or a file that is recognized as YAML by VS Code. The extension only activates when a YAML file is open.

---
title: Extension Testing
description: Running Mocha tests inside a headless VS Code instance.
---

# :material-microsoft-visual-studio-code: Extension Testing

The VS Code extension uses `@vscode/test-electron` to run its test suite inside a real, headless VS Code instance. This ensures that the VS Code APIs behave exactly as they do in production.

**Location:** `vscode-extension/src/test/`

---

## Running Tests

```bash
cd idp-platform/vscode-extension

# Compile the TypeScript and run the tests
npm test
```

When you run `npm test`, the test runner will:
1. Download a specific version of VS Code to a temporary `.vscode-test` folder
2. Launch VS Code in the background (headless)
3. Load our extension into that VS Code instance
4. Run the Mocha test suite
5. Print the results to your terminal

---

## What We Test

The extension tests verify the lifecycle and the LSP integration:

1. **Extension Activation:** Verifies the extension successfully activates when a YAML file is opened.
2. **Commands Registration:** Verifies all 3 commands are registered with VS Code.
3. **LSP Initialization:** Verifies the extension successfully spawns the Python LSP server.
4. **Diagnostic Publishing:** Opens a broken YAML file programmatically and asserts that VS Code receives the correct squiggly line diagnostics from the server.

---

## Troubleshooting

If `npm test` fails with a download error or timeout, it might be because VS Code failed to download the test runner binaries. You can clear the cache by deleting the `.vscode-test` folder inside the `vscode-extension` directory and trying again.

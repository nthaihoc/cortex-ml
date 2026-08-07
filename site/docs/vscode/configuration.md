---
title: VS Code Extension Configuration
description: Settings for the Local Catalog Topology VS Code extension.
---

# :material-cog: VS Code Extension Configuration

Configure the extension through VS Code Settings (`settings.json` or the Settings UI).

---

## :material-format-list-bulleted: Available Settings

### `catalogTopology.pythonPath`

| Property | Value |
|----------|-------|
| Type | `string` |
| Default | `""` (empty) |

The path to the Python executable used to start the language server.

**Resolution order when empty:**

1. Sibling `idp-platform/backend/.venv/bin/python` (or `.venv\Scripts\python.exe` on Windows) if present
2. `python` on the system `PATH`

**Example:**

```json
{
  "catalogTopology.pythonPath": "/home/user/workspace/idp/idp-platform/backend/.venv/bin/python"
}
```

---

### `catalogTopology.serverWorkingDirectory`

| Property | Value |
|----------|-------|
| Type | `string` |
| Default | `""` (empty) |

Working directory for the language server process.

**Default when empty:** Sibling `idp-platform/backend/` folder.

**Example:**

```json
{
  "catalogTopology.serverWorkingDirectory": "/home/user/workspace/idp/idp-platform/backend"
}
```

---

## :material-file-cog: Complete `settings.json` Example

```json
{
  "catalogTopology.pythonPath": "/home/user/workspace/idp/idp-platform/backend/.venv/bin/python",
  "catalogTopology.serverWorkingDirectory": "/home/user/workspace/idp/idp-platform/backend"
}
```

---

## :material-link: Further Reading

- [Commands Reference](commands.md)
- [VS Code User Settings](https://code.visualstudio.com/docs/getstarted/settings)
- [Quick Start](../getting-started/quickstart.md#vs-code-extension-flow)

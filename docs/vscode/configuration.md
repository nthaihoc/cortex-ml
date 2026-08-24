---
title: Extension Configuration
description: Settings for the Local Catalog Topology VS Code extension.
---

# :material-cog-outline: Extension Configuration

The extension has two configuration settings that you can change in VS Code's Settings JSON or the Settings UI.

Go to **File > Preferences > Settings** (or ++ctrl+comma++) and search for "Catalog Topology".

---

## `catalogTopology.pythonPath`

The path to the Python executable used to run the Language Server.

| Type | Default |
|------|---------|
| `string` | `""` (Empty) |

### How it resolves when empty

If you leave this empty (the default), the extension tries to find Python in this order:

1. Looks for a virtual environment (`.venv/bin/python` or `.\.venv\Scripts\python.exe`) inside the sibling `backend/` folder (assuming you have the full `idp-platform` repository open).
2. Falls back to the global `python3` or `python` command on your system PATH.

### When to set it manually

You should set this if:
- You are not opening the `idp-platform` repository, but just a folder of catalog files.
- Your Python environment is installed somewhere else (like `~/.pyenv/` or a Conda environment).

**Example:**
```json
{
  "catalogTopology.pythonPath": "/usr/local/bin/python3.12"
}
```

---

## `catalogTopology.serverWorkingDirectory`

The working directory for the Language Server process.

| Type | Default |
|------|---------|
| `string` | `""` (Empty) |

### How it resolves when empty

If you leave this empty, the extension sets the working directory to the sibling `backend/` folder. This is required because the server is run as `python -m app.catalog_language_server`, which needs the `app/` directory to be in the Python path.

### When to set it manually

You must set this if you are using the extension outside of the `idp-platform` repository. Point it to the absolute path of the `idp-platform/backend/` directory on your machine.

**Example:**
```json
{
  "catalogTopology.serverWorkingDirectory": "/Users/alice/projects/idp/idp-platform/backend"
}
```

---

## Further Reading

- [Installation](installation.md)
- [Language Server](../lsp/index.md)

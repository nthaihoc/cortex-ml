---
title: Configuration
description: Environment variables and settings for the IDP Platform.
---

# :material-cog-outline: Configuration

The IDP Platform is configured through environment variables and VS Code settings. No configuration files, databases, or cloud accounts are needed.

---

## Environment Variables

All environment variables are set in the `.env` file inside the `idp-platform/` directory.

| Variable | Default Value | Description |
|----------|---------------|-------------|
| `CATALOG_ROOT` | `../catalog-info` | Path to the folder containing your `catalog-info.yaml` files. Can be absolute or relative (relative paths resolve from `idp-platform/`). |
| `VITE_LOCAL_API_TARGET` | `http://127.0.0.1:8000` | The address of the backend API. The Vite dev server proxies frontend requests to this URL. |

### How to Change Settings

1. Open `idp-platform/.env` in your editor
2. Change the value you want
3. Restart the backend server for changes to take effect

??? example "Example: Using a different catalog folder"
    ```dotenv
    # Point to a catalog folder on your desktop
    CATALOG_ROOT=/Users/myname/Desktop/my-catalogs
    ```

??? example "Example: Using an environment variable directly"
    You can also set the variable directly in your terminal without editing the `.env` file:

    === "macOS / Linux"

        ```bash
        CATALOG_ROOT=/path/to/my/catalogs python -m app.local_catalog
        ```

    === "Windows (PowerShell)"

        ```powershell
        $env:CATALOG_ROOT="C:\path\to\my\catalogs"
        python -m app.local_catalog
        ```

---

## Backend Server Defaults

The backend server always binds to **`127.0.0.1:8000`** (localhost only). This means:

- ✅ Only your machine can access the API
- ✅ No authentication is needed
- ✅ No firewall changes are needed
- ❌ Other computers on your network cannot reach it

!!! info "File size limit"
    Catalog descriptor files larger than **1 MB** are skipped with a `CATALOG_DESCRIPTOR_TOO_LARGE` diagnostic. This prevents accidentally loading very large files.

---

## VS Code Extension Settings

If you use the VS Code extension, these settings are available in VS Code's Settings (++ctrl+comma++):

| Setting | Default | Description |
|---------|---------|-------------|
| `catalogTopology.pythonPath` | *(empty)* | Path to a specific Python executable. When empty, the extension looks for a `.venv` in the sibling `backend/` folder, then falls back to `python` on your PATH. |
| `catalogTopology.serverWorkingDirectory` | *(empty)* | Working directory for the backend Language Server. Defaults to the sibling `idp-platform/backend/` folder. |

??? example "Example: Using a specific Python version"
    In VS Code Settings JSON (++ctrl+shift+p++ → "Preferences: Open Settings (JSON)"):
    ```json
    {
      "catalogTopology.pythonPath": "/usr/local/bin/python3.12"
    }
    ```

---

## Catalog Root Behavior

When the backend starts, it scans the `CATALOG_ROOT` directory:

1. **Recursively walks** all subdirectories
2. **Looks for** files named exactly `catalog-info.yaml`
3. **Skips** these directories: `.git`, `.venv`, `node_modules`, `dist`, `build`, and any directory starting with `.`
4. **Skips** symbolic links and junctions (for security)
5. **Skips** files larger than 1 MB

After the initial scan, a **file watcher** monitors the catalog root for changes. When you add, edit, or delete a `catalog-info.yaml` file, the backend automatically updates within ~300 ms.

---

## Next Steps

- [Quick Start](quickstart.md) — Run the platform for the first time
- [Architecture](../architecture/index.md) — Learn how the system works inside

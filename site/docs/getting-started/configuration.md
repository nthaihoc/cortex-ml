---
title: Configuration
description: Environment variables and runtime configuration options for the IDP Platform.
---

# :material-cog-outline: Configuration

The IDP Platform is configured primarily through a `.env` file and VS Code settings. No external configuration service is required.

---

## :material-file-cog: Environment File (`.env`)

Copy `.env.example` to `.env` in the `idp-platform/` root directory:

```bash
cp .env.example .env
```

### Available Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CATALOG_ROOT` | `../catalog-info` | Path to the directory containing `catalog-info.yaml` files. Relative paths resolve from `idp-platform/`. |
| `VITE_LOCAL_API_TARGET` | `http://127.0.0.1:8000` | Vite dev proxy target for the loopback backend API. |

### Example Configurations

=== "Default (repo sample)"

    ```dotenv
    CATALOG_ROOT=../catalog-info
    VITE_LOCAL_API_TARGET=http://127.0.0.1:8000
    ```

=== "Custom catalog directory"

    ```dotenv
    CATALOG_ROOT=/home/user/my-services/catalog
    VITE_LOCAL_API_TARGET=http://127.0.0.1:8000
    ```

=== "Generated catalog"

    ```dotenv
    CATALOG_ROOT=./backend/.generated-catalog
    VITE_LOCAL_API_TARGET=http://127.0.0.1:8000
    ```

---

## :material-server-network: Backend Runtime Configuration

The backend (`app.local_catalog`) reads `CATALOG_ROOT` from the environment at startup. The discovery process:

1. Resolves `CATALOG_ROOT` as an absolute path
2. Recursively discovers all files named exactly **`catalog-info.yaml`**
3. Ignores hidden directories (starting with `.`) and generated directories (e.g., `node_modules`, `__pycache__`, `.venv`)
4. Ignores symlinks and junctions (security constraint)

!!! warning "File size limit"
    Individual descriptor files exceeding **1 MB** (1,048,576 bytes) are skipped with a `CATALOG_DESCRIPTOR_TOO_LARGE` diagnostic. This limit is hardcoded in `backend/app/local_catalog/runtime.py` as `DEFAULT_MAX_DESCRIPTOR_SIZE_BYTES`.

---

## :material-microsoft-visual-studio-code: VS Code Extension Settings

Configure the extension through VS Code settings (`settings.json` or the Settings UI):

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `catalogTopology.pythonPath` | `string` | `""` | Path to the Python executable. When empty, uses the sibling backend `.venv`, then falls back to `python` on PATH. |
| `catalogTopology.serverWorkingDirectory` | `string` | `""` | Backend working directory. Defaults to the sibling `idp-platform/backend` folder. |

### Example `settings.json`

```json
{
  "catalogTopology.pythonPath": "/home/user/workspace/idp/idp-platform/backend/.venv/bin/python",
  "catalogTopology.serverWorkingDirectory": "/home/user/workspace/idp/idp-platform/backend"
}
```

---

## :material-tune: Watcher Debounce

The filesystem watcher and LSP service both apply a **300 ms debounce** before processing changed files. This prevents excessive re-validation during rapid successive saves.

- Filesystem watcher: `CatalogFileWatcher(debounce_seconds=0.3)`
- Language server: `CatalogLanguageService(debounce_seconds=0.3)`

This is configurable in code but not currently exposed as an environment variable.

---

## :material-link: Further Reading

- [python-dotenv documentation](https://saurabh-kumar.com/python-dotenv/)
- [Vite Environment Variables](https://vite.dev/guide/env-and-mode)
- [VS Code Extension Settings](https://code.visualstudio.com/api/references/contribution-points#contributes.configuration)

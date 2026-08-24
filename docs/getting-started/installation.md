---
title: Installation
description: Step-by-step installation of the IDP Platform — backend, frontend, and VS Code extension.
---

# :material-download-circle-outline: Installation

This guide walks you through setting up each part of the IDP Platform from a fresh clone.

---

## Clone the Repository

=== "macOS / Linux"

    ```bash
    git clone https://github.com/truongabc-group1/idp.git
    cd idp
    ```

=== "Windows (PowerShell)"

    ```powershell
    git clone https://github.com/truongabc-group1/idp.git
    cd idp
    ```

After cloning, your folder structure looks like this:

```
idp/
├── catalog-info/       # Sample catalog descriptor files
├── idp-platform/       # The platform source code
│   ├── backend/        # Python backend
│   ├── frontend/       # React frontend
│   ├── vscode-extension/  # VS Code extension
│   └── ...
└── README.md
```

---

## Set Up the Environment File

Copy the example environment file:

=== "macOS / Linux"

    ```bash
    cp idp-platform/.env.example idp-platform/.env
    ```

=== "Windows (PowerShell)"

    ```powershell
    Copy-Item idp-platform\.env.example idp-platform\.env
    ```

The default settings work immediately — no changes needed:

```dotenv
# Path to your catalog files (relative to idp-platform/)
CATALOG_ROOT=../catalog-info

# Frontend dev server connects to this API address
VITE_LOCAL_API_TARGET=http://127.0.0.1:8000
```

!!! tip "Custom catalog location"
    If your `catalog-info.yaml` files are in a different folder, change `CATALOG_ROOT` to point there. Both absolute paths and relative paths (from `idp-platform/`) are supported.

---

## Install the Backend (Python)

=== "macOS / Linux (pip)"

    ```bash
    cd idp-platform/backend

    # Create a Python virtual environment
    python3.12 -m venv .venv

    # Activate the virtual environment
    source .venv/bin/activate

    # Install all dependencies
    pip install -r requirements.txt -r requirements-dev.txt
    ```

=== "macOS / Linux (uv — faster)"

    ```bash
    cd idp-platform/backend

    # uv automatically creates the virtual environment and installs everything
    uv sync

    # Activate the virtual environment
    source .venv/bin/activate
    ```

=== "Windows (pip)"

    ```powershell
    cd idp-platform\backend

    # Create a Python virtual environment
    py -3.12 -m venv .venv

    # Activate the virtual environment
    .\.venv\Scripts\Activate.ps1

    # Install all dependencies
    pip install -r requirements.txt -r requirements-dev.txt
    ```

??? info "What gets installed?"
    | Package | Version | What it does |
    |---------|---------|-------------|
    | `fastapi` | 0.141.0 | HTTP API framework |
    | `uvicorn[standard]` | 0.52.0 | ASGI web server |
    | `watchfiles` | 1.2.0 | Detects file changes on disk |
    | `pydantic` | 2.13.4 | Data validation and serialization |
    | `pyyaml` | 6.0.3 | YAML file parsing |
    | `pygls` | 2.1.1 | Python Language Server framework |
    | `python-dotenv` | 1.2.2 | Reads `.env` configuration files |
    | `pytest` | 9.1.1 | Test framework (dev only) |
    | `ruff` | 0.12.5 | Python linter (dev only) |
    | `httpx` | 0.28.1 | HTTP test client (dev only) |

---

## Install the Frontend (Node.js)

=== "macOS / Linux"

    ```bash
    cd ../frontend   # from backend/, go to frontend/
    npm install
    ```

=== "Windows (PowerShell)"

    ```powershell
    cd ..\frontend   # from backend\, go to frontend\
    npm install
    ```

??? info "What gets installed?"
    | Package | Version | What it does |
    |---------|---------|-------------|
    | `react` | 19.x | UI component library |
    | `react-dom` | 19.x | React rendering for the browser |
    | `reactflow` | 11.x | Interactive graph/diagram library |
    | `vite` | 7.x | Fast development server and build tool |
    | `typescript` | 5.x | Type-safe JavaScript |
    | `vitest` | 4.x | Test framework |

---

## Install the VS Code Extension *(optional)*

Only needed if you want to develop or test the VS Code extension:

=== "macOS / Linux"

    ```bash
    cd ../vscode-extension   # from frontend/, go to vscode-extension/
    npm install
    npm run build
    ```

=== "Windows (PowerShell)"

    ```powershell
    cd ..\vscode-extension   # from frontend\, go to vscode-extension\
    npm install
    npm run build
    ```

---

## Verify the Installation

Run the tests for each component to make sure everything is working:

=== "Backend"

    ```bash
    cd idp-platform/backend
    source .venv/bin/activate   # or .\.venv\Scripts\Activate.ps1 on Windows
    python -m pytest
    ```

    ??? example "Expected output"
        ```
        ========================= test session starts =========================
        collected XX items

        tests/... PASSED
        ...
        ========================= XX passed in X.XXs ==========================
        ```

=== "Frontend"

    ```bash
    cd idp-platform/frontend
    npm test
    npm run build
    ```

    ??? example "Expected output"
        ```
        ✓ All tests passed
        vite v7.x.x building for production...
        ✓ built in X.XXs
        ```

=== "VS Code Extension"

    ```bash
    cd idp-platform/vscode-extension
    npm test
    npm run check
    npm run build
    ```

---

## Troubleshooting

??? question "Python: `command not found: python3.12`"
    Try using `python3` instead. On Windows, use `py -3.12` or `py -3`.
    Make sure Python 3.12+ is installed — see [Prerequisites](prerequisites.md).

??? question "pip: `error: externally-managed-environment`"
    This happens on some Linux distributions. Use a virtual environment (which the instructions above already do), or install `uv` and use `uv sync` instead.

??? question "npm: `EACCES permission denied`"
    On macOS/Linux, do **not** use `sudo npm install`. Instead, fix npm permissions:
    ```bash
    mkdir ~/.npm-global
    npm config set prefix '~/.npm-global'
    export PATH=~/.npm-global/bin:$PATH
    ```

??? question "Windows: `cannot be loaded because running scripts is disabled`"
    Run this in an Administrator PowerShell:
    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

---

## Next Step

Everything installed? Continue to the [Quick Start](quickstart.md) to run the platform.

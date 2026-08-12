---
title: Installation
description: Step-by-step installation of the IDP Platform components — backend, frontend, and VS Code extension.
---

# :material-download-circle-outline: Installation

This guide walks through setting up each component of the IDP Platform from a fresh clone.

---

## :material-git: Step 1 — Clone the Repository

```bash
git clone https://github.com/truongabc-group1/idp.git
cd idp/idp-platform
```

---

## :material-cog: Step 2 — Configure Environment

Copy the example environment file to `.env`:

```bash
cp .env.example .env
```

The defaults work out of the box for local development:

```dotenv
# Local catalog backend. Relative paths resolve from the idp-platform directory.
CATALOG_ROOT=../catalog-info

# Optional Vite development proxy target for the loopback local catalog API.
VITE_LOCAL_API_TARGET=http://127.0.0.1:8000
```

!!! tip "Using a custom catalog root"
    Point `CATALOG_ROOT` to any directory containing `catalog-info.yaml` files. Both absolute and relative paths are supported. Relative paths resolve from the `idp-platform/` directory.

---

## :material-language-python: Step 3 — Backend Setup

=== "pip (standard)"

    ```bash
    cd backend

    # Create a virtual environment
    python3.12 -m venv .venv

    # Activate it
    source .venv/bin/activate          # macOS / Linux
    # .\.venv\Scripts\Activate.ps1    # Windows PowerShell

    # Install dependencies
    pip install -r requirements.txt -r requirements-dev.txt
    ```

=== "uv (fast)"

    ```bash
    cd backend
    uv sync
    source .venv/bin/activate
    ```

The backend installs these core packages:

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | 0.141.0 | HTTP API framework |
| `uvicorn[standard]` | 0.52.0 | ASGI server |
| `watchfiles` | 1.2.0 | Filesystem change detection |
| `pydantic` | 2.13.4 | Data validation / normalization |
| `pyyaml` | 6.0.3 | YAML parsing |
| `pygls` | 2.1.1 | Python LSP framework |
| `python-dotenv` | 1.2.2 | Environment configuration |

---

## :material-react: Step 4 — Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install
```

The frontend uses React 19, ReactFlow 11, Vite 7, and TypeScript 5.

---

## :material-microsoft-visual-studio-code: Step 5 — VS Code Extension Setup *(optional)*

Only required for the VS Code extension development flow:

```bash
cd ../vscode-extension

# Install dependencies
npm install

# Build the extension
npm run build
```

---

## :material-check-decagram: Verifying the Installation

Run the full test suite to confirm everything is correctly installed:

=== "Backend"

    ```bash
    cd backend
    python -m pytest
    ```

=== "Frontend"

    ```bash
    cd frontend
    npm test
    npm run build
    ```

=== "VS Code Extension"

    ```bash
    cd vscode-extension
    npm test
    npm run check
    npm run build
    ```

---

## :material-link: Further Reading

- [Python virtual environments (venv)](https://docs.python.org/3/library/venv.html)
- [uv documentation](https://docs.astral.sh/uv/)
- [npm documentation](https://docs.npmjs.com/)
- [FastAPI Getting Started](https://fastapi.tiangolo.com/tutorial/)

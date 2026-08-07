---
title: Prerequisites
description: Software requirements for running the IDP Platform Local Catalog Topology.
---

# :material-clipboard-check-outline: Prerequisites

Before cloning the repository and running the platform, ensure the following tools are installed on your machine.

---

## :material-language-python: Python

**Required version: 3.12 or newer**

The backend and language server are written in Python. Python 3.12 is the minimum because the codebase uses:

- `StrEnum` (PEP 663)
- `slots=True` on `dataclass` (PEP 557 update, available from 3.10, stable from 3.12)
- Modern type union syntax (`X | Y`) across all modules

=== "macOS / Linux"

    ```bash
    # Check your version
    python3 --version

    # Install via pyenv (recommended)
    pyenv install 3.12
    pyenv global 3.12
    ```

=== "Windows"

    ```powershell
    # Check your version
    py --version

    # Download from python.org
    # https://www.python.org/downloads/
    py -3.12 --version
    ```

!!! note "Alternative: `uv`"
    The repository ships `uv.lock` files in both `backend/` and `cli/`. You can use [uv](https://docs.astral.sh/uv/) instead of `pip` for faster dependency resolution:
    ```bash
    uv sync  # inside backend/ or cli/
    ```

---

## :material-nodejs: Node.js

**Required version: 20 or newer**

The frontend (React + Vite) and VS Code extension require Node.js. Node.js 20 LTS is recommended for stability.

=== "macOS / Linux"

    ```bash
    # Check version
    node --version

    # Install via nvm (recommended)
    nvm install 20
    nvm use 20
    ```

=== "Windows"

    ```powershell
    node --version
    # Download from https://nodejs.org/
    ```

---

## :material-microsoft-visual-studio-code: VS Code *(for the extension)*

**Required version: 1.91 or newer** — only needed if you want the VS Code Extension development flow.

The extension uses LSP client APIs available since VS Code 1.91.

Download VS Code from [code.visualstudio.com](https://code.visualstudio.com/).

---

## :material-table-check: Summary

| Tool | Minimum Version | Required For |
|------|-----------------|--------------|
| Python | **3.12** | Backend, Language Server, CLI |
| Node.js | **20** | Frontend, VS Code Extension |
| VS Code | **1.91** | Extension flow only |

---

## :material-link: Further Reading

- [Python Official Downloads](https://www.python.org/downloads/)
- [Node.js Official Downloads](https://nodejs.org/en/download/)
- [pyenv — Python version manager](https://github.com/pyenv/pyenv)
- [nvm — Node version manager](https://github.com/nvm-sh/nvm)
- [uv — Fast Python package manager](https://docs.astral.sh/uv/)

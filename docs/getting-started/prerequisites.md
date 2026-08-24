---
title: Prerequisites
description: Software you need before installing the IDP Platform.
---

# :material-clipboard-check-outline: Prerequisites

Before you begin, make sure you have the following software installed on your computer.

---

## Required Software

| Software | Minimum Version | What it is used for |
|----------|----------------|---------------------|
| :material-language-python: **Python** | 3.12 or newer | Runs the backend server, validation engine, and LSP |
| :material-nodejs: **Node.js** | 20 or newer | Runs the frontend dev server and builds the VS Code extension |
| :material-git: **Git** | Any recent version | Clones the repository |

!!! note "No database or Docker needed"
    The IDP Platform runs entirely on your machine without any database, container runtime, or cloud service. After installing the dependencies above, **no internet connection is needed**.

---

## How to Check Your Versions

Open a terminal and run these commands to check if you have the right versions:

=== "macOS / Linux"

    ```bash
    # Check Python version (must be 3.12 or newer)
    python3 --version

    # Check Node.js version (must be 20 or newer)
    node --version

    # Check npm version (comes with Node.js)
    npm --version

    # Check Git version
    git --version
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Check Python version (must be 3.12 or newer)
    py -3 --version

    # Check Node.js version (must be 20 or newer)
    node --version

    # Check npm version (comes with Node.js)
    npm --version

    # Check Git version
    git --version
    ```

??? example "Example output"
    ```
    $ python3 --version
    Python 3.12.4

    $ node --version
    v20.18.0

    $ npm --version
    10.8.2

    $ git --version
    git version 2.45.2
    ```

---

## How to Install Missing Software

### Python 3.12+

=== "macOS"

    Download from [python.org](https://www.python.org/downloads/) or use Homebrew:

    ```bash
    brew install python@3.12
    ```

=== "Linux (Ubuntu/Debian)"

    ```bash
    sudo apt update
    sudo apt install python3.12 python3.12-venv python3-pip
    ```

=== "Windows"

    Download the installer from [python.org](https://www.python.org/downloads/).

    !!! warning "Check 'Add to PATH'"
        During installation, make sure to check the **"Add Python to PATH"** checkbox. This lets you run Python from any terminal.

### Node.js 20+

=== "macOS"

    Download from [nodejs.org](https://nodejs.org/) or use Homebrew:

    ```bash
    brew install node@20
    ```

=== "Linux (Ubuntu/Debian)"

    ```bash
    # Using NodeSource
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt install -y nodejs
    ```

=== "Windows"

    Download the installer from [nodejs.org](https://nodejs.org/).

### Git

=== "macOS"

    Git comes with Xcode Command Line Tools:

    ```bash
    xcode-select --install
    ```

=== "Linux (Ubuntu/Debian)"

    ```bash
    sudo apt install git
    ```

=== "Windows"

    Download from [git-scm.com](https://git-scm.com/download/win).

---

## Optional: VS Code

If you want to use the VS Code extension for in-editor diagnostics and topology preview:

| Software | Version | Download |
|----------|---------|----------|
| **VS Code** | 1.91 or newer | [code.visualstudio.com](https://code.visualstudio.com/) |

---

## Next Step

Once you have Python, Node.js, and Git installed, continue to [Installation](installation.md).

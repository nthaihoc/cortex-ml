---
title: Quick Start
description: Go from fresh clone to a running topology viewer in under 5 minutes.
---

# :material-play-circle-outline: Quick Start

This guide gets you from a fresh clone to a **live browser topology viewer** in under 5 minutes.

---

## :material-monitor-dashboard: Browser Development Flow

### 1. Start the Backend

=== "macOS / Linux"

    ```bash
    cd idp-platform/backend
    python3.12 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt -r requirements-dev.txt
    python -m app.local_catalog
    ```

=== "Windows (PowerShell)"

    ```powershell
    cd idp-platform\backend
    py -3.12 -m venv .venv
    .\.venv\Scripts\python.exe -m pip install -r requirements.txt -r requirements-dev.txt
    .\.venv\Scripts\python.exe -m app.local_catalog
    ```

You should see output like:

```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### 2. Start the Frontend

Open a **second terminal**:

=== "macOS / Linux"

    ```bash
    cd idp-platform/frontend
    npm install
    npm run dev
    ```

=== "Windows (PowerShell)"

    ```powershell
    cd idp-platform\frontend
    npm install
    npm run dev
    ```

Vite will start a dev server and print:

```
  VITE v7.x  ready in 300 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

### 3. Open the Browser

Navigate to **[http://127.0.0.1:5173](http://127.0.0.1:5173)**.

!!! info "How it works"
    Vite automatically proxies `/health` and `/api` requests to the backend at `127.0.0.1:8000`. Saved descriptor file changes instantly update the running catalog via the filesystem watcher and Server-Sent Events.

---

## :material-test-tube: Generate a Sample Catalog

If you don't have `catalog-info.yaml` files yet, generate a synthetic catalog:

=== "macOS / Linux"

    ```bash
    cd backend
    python -m scripts.generate_catalog --count 20 --output ./.generated-catalog
    CATALOG_ROOT=$(pwd)/.generated-catalog python -m app.local_catalog
    ```

=== "Windows (PowerShell)"

    ```powershell
    cd idp-platform\backend
    .\.venv\Scripts\python.exe -m scripts.generate_catalog --count 20 --output .\.generated-catalog
    $env:CATALOG_ROOT=(Resolve-Path .\.generated-catalog)
    .\.venv\Scripts\python.exe -m app.local_catalog
    ```

This creates 20 synthetic catalog entities with a chain topology perfect for exploring the viewer.

---

## :material-microsoft-visual-studio-code: VS Code Extension Flow

### 1. Build the Extension

```bash
cd idp-platform/vscode-extension
npm install
npm run build
```

### 2. Launch the Extension Development Host

1. Open the **`idp-platform` root folder** in VS Code
2. Select the **"Run Local Catalog Topology Extension"** launch configuration
3. Press **`F5`**

A new VS Code Extension Development Host window opens.

### 3. Use the Extension

1. Open a folder containing `catalog-info.yaml` files in the Extension Development Host
2. Focus a `catalog-info.yaml` file in the editor
3. Run the command palette (`Ctrl+Shift+P`) → **"Catalog: Open Topology Beside"**

!!! tip "Python Path"
    If your backend virtual environment is not the default Python on your `PATH`, set `catalogTopology.pythonPath` in VS Code settings to point to the `.venv/bin/python` executable.

---

## :material-check: What to Expect

After a successful start:

- **`/health`** returns `{"status": "ok", "revision": N, "entity_count": N, "diagnostic_count": N}`
- **Browser** shows an interactive ReactFlow graph of entity topology
- **VS Code** shows inline diagnostics and a side-by-side topology webview
- **Saving** a `catalog-info.yaml` file automatically refreshes the graph within ~300 ms

---

## :material-link: Further Reading

- [Vite Dev Server](https://vite.dev/guide/)
- [FastAPI Uvicorn](https://fastapi.tiangolo.com/deployment/manually/)
- [VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)

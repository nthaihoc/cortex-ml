---
title: Quick Start
description: Start the platform and see the topology viewer in under 5 minutes.
---

# :material-rocket-launch-outline: Quick Start

This guide gets you from a fresh installation to a running topology viewer in a few minutes.

!!! note "Before you start"
    Make sure you have completed the [Installation](installation.md) steps first.

---

## Start the Backend Server

The backend reads your `catalog-info.yaml` files, validates them, and serves the API.

=== "macOS / Linux"

    ```bash
    cd idp-platform/backend
    source .venv/bin/activate
    python -m app.local_catalog
    ```

=== "Windows (PowerShell)"

    ```powershell
    cd idp-platform\backend
    .\.venv\Scripts\Activate.ps1
    python -m app.local_catalog
    ```

??? example "Expected output"
    ```
    INFO:     Loaded local catalog root=/.../catalog-info descriptors=12 entities=10
              diagnostics=2 elapsed_ms=45.3
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to stop)
    ```

!!! success "Check it works"
    Open [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) in your browser. You should see:
    ```json
    {"status": "ok", "revision": 12, "entity_count": 10, "diagnostic_count": 2}
    ```

---

## Start the Frontend Dev Server

Open a **second terminal** (keep the backend running) and start the frontend:

=== "macOS / Linux"

    ```bash
    cd idp-platform/frontend
    npm run dev
    ```

=== "Windows (PowerShell)"

    ```powershell
    cd idp-platform\frontend
    npm run dev
    ```

??? example "Expected output"
    ```
    VITE v7.x.x  ready in XXX ms

    ➜  Local:   http://localhost:5173/
    ➜  Network: use --host to expose
    ```

---

## Open the Topology Viewer

Open **[http://localhost:5173](http://localhost:5173)** in your browser.

You should see the topology viewer showing all discovered catalog entities as a graph. Click any node to focus on it and see its connections.

!!! info "How it works"
    The Vite dev server automatically proxies `/health` and `/api` requests to the backend at `http://127.0.0.1:8000`. You do not need to configure CORS or any other settings.

---

## Try Making a Change

1. Open any `catalog-info.yaml` file in your editor (for example, `catalog-info/idp-developer-portal/catalog-info.yaml`)
2. Make a small change (like editing the `description` field)
3. Save the file
4. Watch the browser — it updates automatically!

The file watcher detects your change, re-validates the descriptor, and pushes an update through the SSE event stream.

---

## Generate Sample Data

Want to test with more entities? Generate a synthetic catalog:

=== "macOS / Linux"

    ```bash
    cd idp-platform/backend
    source .venv/bin/activate

    # Generate 20 sample entities
    python -m scripts.generate_catalog --count 20 --output .generated-catalog

    # Start the backend with the generated catalog
    CATALOG_ROOT=.generated-catalog python -m app.local_catalog
    ```

=== "Windows (PowerShell)"

    ```powershell
    cd idp-platform\backend
    .\.venv\Scripts\Activate.ps1

    # Generate 20 sample entities
    python -m scripts.generate_catalog --count 20 --output .generated-catalog

    # Start the backend with the generated catalog
    $env:CATALOG_ROOT=".generated-catalog"
    python -m app.local_catalog
    ```

---

## Optional: Try the VS Code Extension

If you installed the VS Code extension:

1. Open the `idp` repository root folder in VS Code
2. Press **F5** → select **Run Local Catalog Topology Extension**
3. In the new Extension Development Host window, open a folder that contains `catalog-info.yaml` files
4. Open a `catalog-info.yaml` file and run the command **Catalog: Open Topology Beside** (from the Command Palette: ++ctrl+shift+p++)

You will see:

- **Inline diagnostics** — validation errors and warnings appear as squiggly underlines
- **Topology webview** — a graph panel shows the focused topology beside your editor
- **Live updates** — unsaved changes are analyzed after ~300 ms and the topology updates in real time

---

## Next Steps

- [Configuration](configuration.md) — Change catalog root, API port, and other settings
- [Architecture](../architecture/index.md) — Understand how the system works
- [Descriptor Format](../descriptor/index.md) — Learn how to write catalog descriptors

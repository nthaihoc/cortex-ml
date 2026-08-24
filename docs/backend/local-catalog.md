---
title: Local HTTP Runtime
description: FastAPI server, filesystem discovery, and the local catalog entry point.
---

# :material-server: Local HTTP Runtime

The local catalog runtime ties together the HTTP API, filesystem discovery, and file watcher into a single process that serves the catalog from your local disk.

**Location:** `backend/app/local_catalog/`

---

## Entry Point

Start the local catalog with:

```bash
python -m app.local_catalog
```

This runs the `LocalCatalogRuntime`, which:

1. Reads `CATALOG_ROOT` from the environment (defaults to `../catalog-info`)
2. Discovers all `catalog-info.yaml` files under that root
3. Loads each file into the `CatalogWorkspace`
4. Starts the file watcher for live updates
5. Starts the FastAPI HTTP server on `127.0.0.1:8000`

---

## Filesystem Discovery

**File:** `backend/app/local_catalog/filesystem.py`

The discovery process:

1. **Recursively walks** all directories under `CATALOG_ROOT`
2. **Looks for** files named exactly `catalog-info.yaml`
3. **Skips** these directories: `.git`, `.venv`, `node_modules`, `dist`, `build`, `__pycache__`, and directories starting with `.`
4. **Skips** symbolic links and junctions
5. **Skips** files larger than 1 MB
6. **Returns** a list of `(source_uri, relative_path, content)` tuples

---

## FastAPI Application

**File:** `backend/app/local_catalog/api.py`

The HTTP server provides 7 endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Server status and catalog stats |
| `/api/v1/catalog/snapshot` | GET | Full catalog snapshot |
| `/api/v1/catalog/topology` | GET | One-hop focused topology |
| `/api/v1/catalog/diagnostics` | GET | All active diagnostics |
| `/api/v1/catalog/events` | GET | SSE change notification stream |
| `/api/v1/catalog/source` | GET | Read a descriptor file |
| `/api/v1/catalog/source` | PUT | Update a descriptor file |

All endpoints return JSON. The server binds to `127.0.0.1:8000` (loopback only — not accessible from the network).

See the full API reference at [API Endpoints](../api/endpoints.md).

---

## Security Model

The local catalog runtime is designed to run **only on your machine**:

- Binds to `127.0.0.1` (localhost only)
- No authentication or authorization
- The PUT `/api/v1/catalog/source` endpoint uses **optimistic concurrency** (SHA-256 content hashing) to prevent write conflicts
- Source files must be within the catalog root — path traversal is blocked
- Symbolic links are not followed

---

## Further Reading

- [API Endpoints](../api/endpoints.md) — Detailed endpoint documentation
- [File Watcher](file-watcher.md) — How changes are detected
- [Configuration](../getting-started/configuration.md) — Environment variables

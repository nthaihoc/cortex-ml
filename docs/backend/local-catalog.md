---
title: Local HTTP Runtime
description: LocalCatalogRuntime, FastAPI application, and filesystem discovery.
---

# :material-server: Local HTTP Runtime

The local HTTP runtime (`backend/app/local_catalog/`) wraps `CatalogWorkspace` in a FastAPI application for the browser viewer.

---

## :material-diagram: Component Diagram

```
CATALOG_ROOT/
    └── catalog-info.yaml files
              │
              ▼
    discover_catalog_descriptors()     ← filesystem.py
              │
              ▼
    LocalCatalogRuntime                ← runtime.py
    ├── CatalogWorkspace
    ├── CatalogChangeFeed (SSE pub/sub)
    └── adapter_diagnostics (oversized files)
              │
              ▼
    create_local_catalog_app()         ← api.py
    ├── FastAPI application
    ├── CORSMiddleware (Vite origin only)
    └── CatalogFileWatcher task        ← watcher.py
```

---

## :material-file-find: Filesystem Discovery — `filesystem.py`

```python
from app.local_catalog.filesystem import discover_catalog_descriptors

descriptors = discover_catalog_descriptors(Path("/path/to/catalog/root"))
# Returns a sorted list of Path objects for all catalog-info.yaml files
```

**Rules:**
- Only files named exactly `catalog-info.yaml`
- Unlimited depth beneath `CATALOG_ROOT`
- Skips hidden directories (`.`-prefixed)
- Skips `node_modules`, `__pycache__`, `.venv`, etc.
- Never follows symlinks or junctions

---

## :material-server-network: `LocalCatalogRuntime` — `runtime.py`

```python
@dataclass(frozen=True, slots=True)
class LocalCatalogRuntime:
    catalog_root: Path
    workspace: CatalogWorkspace
    adapter_diagnostics: tuple[CatalogDiagnostic, ...]
    changes: CatalogChangeFeed
```

**Key methods:**

| Method | Description |
|--------|-------------|
| `snapshot()` | Full catalog snapshot (workspace diagnostics + adapter diagnostics) |
| `diagnostics()` | Sorted combined diagnostics |
| `focused_topology(root, ...)` | Delegates to `workspace.focused_topology()` |

**Loading:**

```python
from app.local_catalog.runtime import load_catalog_root

runtime = load_catalog_root(Path("./catalog"))
# Discovers, reads, and upserts all descriptors
# Returns a fully initialized LocalCatalogRuntime
```

**File size limit:**

Files > `DEFAULT_MAX_DESCRIPTOR_SIZE_BYTES` (1 MB) are skipped and generate a `CATALOG_DESCRIPTOR_TOO_LARGE` error diagnostic instead of being loaded.

---

## :material-api: FastAPI Application — `api.py`

The application is created by `create_local_catalog_app()`:

```python
from app.local_catalog.api import create_local_catalog_app

app = create_local_catalog_app(
    catalog_root=Path("./catalog"),
    vite_origin="http://localhost:5173",
)
```

### CORS Configuration

Only the configured `vite_origin` is allowed:

```python
CORSMiddleware(
    allow_origins=[vite_origin],
    allow_credentials=False,
    allow_methods=["GET", "PUT"],
    allow_headers=["*"],
)
```

### Application Lifespan

On startup:
1. `CatalogFileWatcher.run()` task starts watching `CATALOG_ROOT`

On shutdown:
1. The watcher task is cancelled and awaited

---

## :material-link: Further Reading

- [File Watcher](file-watcher.md)
- [API Endpoints](../api/endpoints.md)
- [FastAPI Lifespan](https://fastapi.tiangolo.com/advanced/events/)
- [Watchfiles](https://watchfiles.helpmanual.io/)

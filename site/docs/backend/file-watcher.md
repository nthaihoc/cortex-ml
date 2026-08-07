---
title: File Watcher
description: How the CatalogFileWatcher detects and processes filesystem changes.
---

# :material-file-eye-outline: File Watcher

**File:** `backend/app/local_catalog/watcher.py`

The `CatalogFileWatcher` monitors the `CATALOG_ROOT` directory for changes to `catalog-info.yaml` files and updates the `CatalogWorkspace` accordingly.

---

## :material-pipeline: Architecture

```
watchfiles.awatch()                      ← raw OS filesystem events
        │
        ▼
WatchfilesCatalogEventSource.__aiter__() ← filters + normalizes events
        │ yields tuple[CatalogFileEvent, ...]
        ▼
CatalogFileWatcher.run()                 ← main event loop
        │
        ▼
CatalogFileWatcher._schedule(event)      ← debounce per-file key
        │
        ▼ (after 300ms debounce)
CatalogFileWatcher._apply(event)         ← reads + upserts/removes
        │
        ▼
LocalCatalogRuntime.workspace.upsert_document() / remove_document()
        │
        ▼
LocalCatalogRuntime.changes.publish(notification) ← SSE
```

---

## :material-file-multiple: Event Types

```python
class CatalogFileChange(StrEnum):
    ADDED = "added"
    MODIFIED = "modified"
    MOVED = "moved"
    DELETED = "deleted"
```

**MOVED** events are decomposed into a `DELETED` for the source path and an `ADDED` for the destination path.

---

## :material-clock-fast: Debounce Mechanism

Each file path has a per-key debounce:

1. When an event arrives, a new async task is created for the file key
2. The previous pending task for that key is **cancelled**
3. The new task waits `debounce_seconds` (default: `0.3s`)
4. If a newer event arrives before the debounce expires, the cycle repeats
5. Only the last (most recent) event applies

This ensures **burst saves** (e.g., auto-format on save) apply only the final state.

---

## :material-shield: Safety Filtering

`_safe_event_path()` filters events before processing:

| Check | Action if failed |
|-------|-----------------|
| File name is exactly `catalog-info.yaml` | Skip |
| Path is within `catalog_root` | Skip |
| No path segment starts with `.` | Skip |
| No path segment is in ignored directory list | Skip |
| No parent directory is a symlink or junction | Skip |

---

## :material-file-move: Batch Normalization

A single watchfiles batch may contain multiple events. The normalizer:

1. Groups events by type: added, modified, deleted
2. Sorts each group by path
3. Pairs `deleted[i]` with `added[i]` as `MOVED` events (up to `min(len(added), len(deleted))`)
4. Remaining unpaired adds → `ADDED` events
5. Remaining unpaired deletes → `DELETED` events
6. All `modified` events → `MODIFIED` events

---

## :material-code-braces: Custom Event Sources (Testing)

For testing and injection, the `event_source` parameter accepts any `AsyncIterable[tuple[CatalogFileEvent, ...]]`:

```python
from app.local_catalog.api import create_local_catalog_app
from app.local_catalog.watcher import CatalogFileEvent, CatalogFileChange

async def fake_events():
    yield (CatalogFileEvent(CatalogFileChange.MODIFIED, Path("catalog-info.yaml")),)

app = create_local_catalog_app(
    catalog_root=Path("./catalog"),
    event_source=fake_events(),
    watcher_wait=lambda _: None,  # instant debounce
)
```

---

## :material-link: Further Reading

- [Local HTTP Runtime](local-catalog.md)
- [SSE Events](../api/events.md)
- [watchfiles Documentation](https://watchfiles.helpmanual.io/)
- [asyncio Tasks](https://docs.python.org/3/library/asyncio-task.html)

---
title: Backend Tests
description: Python backend test suite for the IDP Platform catalog engine.
---

# :material-language-python: Backend Tests

The backend test suite uses **pytest** and covers the entire catalog pipeline from YAML parsing through topology traversal.

---

## :material-run: Running Tests

```bash
cd backend
python -m pytest

# With coverage
python -m pytest --cov=app --cov-report=term-missing

# Specific test file
python -m pytest tests/test_workspace.py -v
```

---

## :material-folder: Test Organization

| Test File | What It Tests |
|-----------|--------------|
| `tests/test_workspace.py` | Core `CatalogWorkspace` behaviors |
| `tests/test_ingest.py` | YAML parser + normalizer + relation projector |
| `tests/test_validation.py` | `CatalogValidationEngine` schema rules |
| `tests/test_local_catalog.py` | HTTP API, runtime, file watcher |
| `tests/test_language_server.py` | LSP lifecycle and custom methods |

---

## :material-check-all: Coverage Categories

### Core Workspace

- Upsert and remove documents
- Duplicate identity (conflict detection)
- Last-valid state on invalid update
- Draft state on never-valid document
- Focused topology traversal (one-hop, all directions)
- Incremental indexing (no re-parse of unchanged files)
- Save burst deduplication

### YAML Parsing

- All security constraint violations
- Multi-document rejection
- Alias/anchor rejection
- Duplicate key rejection
- Timestamp bare value rejection

### Validation Engine

- VSF IDP v2: all required field checks
- VSF IDP v2: owner email + role validation
- VSF IDP v2: review gate for service/gateway
- Backstage: minimal field checks
- Blocking vs. non-blocking issue classification

### File Watcher

- ADDED, MODIFIED, DELETED, MOVED events
- Debounce (burst save coalescing)
- Safety filtering (symlinks, hidden dirs)
- Batch normalization

### HTTP API

- All endpoint happy paths
- Error cases (422, 404, 409, 413)
- SSE event delivery
- Source update with version guard

---

## :material-link: Further Reading

- [Acceptance Coverage](acceptance.md)
- [pytest Documentation](https://docs.pytest.org/)
- [CatalogWorkspace](../backend/catalog-workspace.md)

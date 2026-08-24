---
title: Backend Testing
description: Running and writing tests for the Python backend.
---

# :material-language-python: Backend Testing

The backend uses `pytest` for unit and integration testing.

**Location:** `backend/tests/`

---

## Running Tests

Activate your virtual environment, then run:

```bash
cd idp-platform/backend
source .venv/bin/activate

# Run all tests
python -m pytest

# Run with coverage report
python -m pytest --cov=app

# Run only validation tests
python -m pytest tests/test_validators/
```

---

## Test Structure

- `tests/test_ingest/` — Tests the hardened parser and normalizer (verifies bad YAML is caught)
- `tests/test_validators/` — Tests the validation engine (checks all 22 diagnostic codes)
- `tests/test_workspace/` — Tests the `CatalogWorkspace` state machine (conflict resolution, topology extraction)
- `tests/test_api/` — Uses `TestClient` to test the FastAPI endpoints
- `tests/test_lsp/` — Uses a mocked language client to test LSP standard methods

---

## The "Bad YAML" Philosophy

A significant portion of the ingest tests verify that the system gracefully handles malicious or malformed YAML. We explicitly test:
- Billion-laughs attacks (anchors/aliases)
- Non-string keys
- Deeply nested structures
- Invalid UTF-8 bytes

When writing new features, always include a test case for malformed input.

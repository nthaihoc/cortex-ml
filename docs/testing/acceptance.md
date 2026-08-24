---
title: Contract Tests
description: Verifying the JSON API payloads stay in sync across components.
---

# :material-handshake-outline: Contract Tests

Because the IDP Platform is split between Python (backend) and TypeScript (frontend/extension), we need to ensure they agree on the JSON data formats.

We use **JSON Contracts** to enforce this.

**Location:** `contracts/examples/`

---

## How it Works

Instead of the backend generating JSON and hoping the frontend can parse it, we store explicit JSON examples in the repo.

Both the backend and the frontend test suites run against these examples:

1. **Backend Tests:** The backend uses `pytest` to generate a snapshot and asserts that the resulting JSON exactly matches the example files.
2. **Frontend Tests:** The frontend uses `vitest` to parse the example files and asserts that they successfully deserialize into the expected TypeScript types.

---

## Contract Files

The contract files live in `contracts/examples/`:

- `snapshot_v1.json`: Example of a full `/api/v1/catalog/snapshot` response.
- `topology_v1.json`: Example of a `/api/v1/catalog/topology` response.
- `diagnostics_v1.json`: Example of a `/api/v1/catalog/diagnostics` response.
- `event_v1.json`: Example of a single SSE event payload.

---

## Modifying the API

If you need to change a field in the API (e.g., adding a new `provisional` flag to relations):

1. **Update Python:** Update the Pydantic models in `backend/app/api/schemas.py`.
2. **Update TypeScript:** Update the interfaces in `frontend/src/localCatalog/types.ts`.
3. **Update Contracts:** Manually edit the JSON files in `contracts/examples/` to include your new field.
4. **Run Tests:** Run both test suites to ensure both sides agree with the new contract.

If you skip step 3, the backend tests will fail because its output no longer matches the contract.

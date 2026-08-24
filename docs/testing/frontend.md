---
title: Frontend Testing
description: Running and writing tests for the React frontend.
---

# :material-react: Frontend Testing

The frontend uses `vitest` for fast, headless unit testing of React components and logic.

**Location:** `frontend/src/**/*.test.ts` and `*.test.tsx`

---

## Running Tests

```bash
cd idp-platform/frontend

# Run all tests
npm test

# Run tests in watch mode (reruns on file save)
npm run test:watch

# Run with coverage report
npm run coverage
```

---

## What We Test

Because the frontend is pure presentation (no validation logic), the tests focus on:

1. **API Client (`HttpLocalCatalogClient.test.ts`)**
   - Verifying URL construction
   - Verifying error handling (404, 500)
2. **Search Logic (`catalogSearch.test.ts` & `catalogSearch.bench.ts`)**
   - Verifying the ranking algorithm (exact match > display name > description)
   - Benchmarking search performance
3. **Layout Logic (`topologyLayout.local.test.ts`)**
   - Verifying nodes are placed in the correct concentric circles based on relation type

---

## No E2E Tests (Yet)

We currently do not run heavy End-to-End (E2E) browser tests like Playwright. We rely on the contract tests to ensure the JSON payloads are correct, and unit tests to verify the UI logic.

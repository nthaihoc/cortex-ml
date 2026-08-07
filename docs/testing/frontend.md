---
title: Frontend Tests
description: TypeScript frontend test suite for the IDP Platform topology viewer.
---

# :material-react: Frontend Tests

The frontend test suite uses **Vitest** and **Testing Library** to test the React topology viewer and catalog utilities.

---

## :material-run: Running Tests

```bash
cd frontend

# Run tests once
npm test

# Watch mode
npm run test:watch

# Performance benchmarks
npm run benchmark

# Build (type-check + bundle)
npm run build
```

---

## :material-folder: Test Organization

| Test File | What It Tests |
|-----------|--------------|
| `src/topology/TopologyViewer.test.tsx` | Main topology viewer React component |
| `src/topology/localContract.test.ts` | HTTP API contract mapping |
| `src/topology/catalogSearch.test.ts` | Catalog search logic |
| `src/topology/topologyLayout.local.test.ts` | Graph layout calculations |
| `src/topology/catalogSearch.bench.ts` | Search performance benchmarks |

---

## :material-check-all: Coverage Categories

### Topology Viewer (`TopologyViewer.test.tsx`)

- Initial render with empty catalog
- Node rendering for all entity states (entity, draft, unresolved, conflict)
- Edge rendering for all relation health states
- Click-to-navigate (root change)
- Pin/unpin focus behavior
- SSE event triggers re-fetch
- Active editor follow behavior (webview mode)
- Draft rekey — keeps graph canvas mounted when a draft becomes an entity
- Message validation for host → webview messages

### Contract Mapping (`localContract.test.ts`)

- HTTP snapshot response → TypeScript types
- HTTP topology response → TypeScript types
- camelCase ↔ snake_case field mapping
- Null handling for optional fields
- Health and freshness enum mapping

### Search (`catalogSearch.test.ts`)

- Empty catalog returns empty results
- Canonical reference exact match
- Display name substring match
- Case-insensitive search

### Benchmarks (`catalogSearch.bench.ts`)

- Linear canonical reference search over 5,000 entities
- Linear display text search over 5,000 entities

---

## :material-link: Further Reading

- [Acceptance Coverage](acceptance.md)
- [Vitest Documentation](https://vitest.dev/)
- [Testing Library Documentation](https://testing-library.com/)

---
title: Development Workflow
description: Branching, pull request, and development workflow for IDP Platform contributors.
---

# :material-source-branch: Development Workflow

---

## :material-git: Branching Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable release branch |
| `feature/<name>` | New features |
| `fix/<name>` | Bug fixes |
| `docs/<name>` | Documentation updates |

---

## :material-hammer-wrench: Local Development Loop

### 1. Create a feature branch

```bash
git checkout -b feature/my-feature main
```

### 2. Make your changes

Follow the [Code Conventions](conventions.md) and ensure all existing tests pass.

### 3. Add tests

- **Backend:** Add pytest tests in `backend/tests/`
- **Frontend:** Add Vitest tests in `frontend/src/`
- **Extension:** Add Vitest tests in `vscode-extension/src/`

### 4. Run the full test suite

```bash
# Backend
cd backend && python -m pytest

# Frontend
cd frontend && npm test && npm run build

# Extension
cd vscode-extension && npm test && npm run check && npm run build
```

### 5. Open a pull request

- Target `main`
- Describe the change and reference any relevant issues
- Ensure all CI checks pass

---

## :material-checklist: Pre-merge Checklist

- [ ] All existing tests pass
- [ ] New tests added for new behavior
- [ ] Documentation updated if public API changed
- [ ] Diagnostic codes (if new) added to [Diagnostic Codes](../diagnostics/codes.md)
- [ ] `openapi/openapi.yaml` updated if HTTP API changed
- [ ] Contract examples in `contracts/examples/` regenerated if shapes changed

---

## :material-link: Further Reading

- [Code Conventions](conventions.md)
- [Testing Overview](../testing/index.md)
- [Architecture Boundaries](../architecture/boundaries.md)

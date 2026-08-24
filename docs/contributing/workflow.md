---
title: Development Workflow
description: Branching strategy and pull request process.
---

# :material-git: Development Workflow

The IDP Platform follows a standard GitHub pull request workflow.

---

## Branching Strategy

- **`main`**: The default branch. It is always deployable and stable.
- **`dev`**: The active development branch. Feature branches are merged here first for integration testing.

When you start a new feature or bugfix, create your branch from `dev`:

```bash
git checkout dev
git pull
git checkout -b feature/my-new-thing
```

Branch naming conventions:
- `feature/*` for new features
- `fix/*` for bug fixes
- `docs/*` for documentation changes
- `chore/*` for refactoring or dependency updates

---

## Creating a Pull Request

When your code is ready:

1. Push your branch to GitHub.
2. Open a Pull Request targeting the **`dev`** branch (not `main`).
3. Fill out the PR template.
4. Ensure all CI checks pass (tests, linting, formatting).

### The CI Pipeline

Every PR runs GitHub Actions that verify:
- Backend: `pytest` and `ruff`
- Frontend: `vitest`, `eslint`, and `prettier`
- VS Code: `npm test` and `eslint`
- Contract Tests: Ensuring backend and frontend agree on API schemas

Your PR must pass all CI checks before it can be merged.

---

## Code Review

All PRs require at least one approval from a repository maintainer before they can be merged.

During review, maintainers will look closely at:
- **Module Boundaries:** Did you leak Python catalog logic into TypeScript?
- **Safety:** Does the parser still reject bad YAML?
- **Performance:** Does this change the `O(1)` or `O(N)` characteristics of the topology graph?

---

## Merging and Releases

1. Features are merged into `dev` via "Squash and Merge".
2. Periodically, `dev` is merged into `main` via a Release PR.
3. Merging to `main` triggers the release pipeline (building the VS Code extension VSIX and publishing to the registry).

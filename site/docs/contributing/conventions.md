---
title: Code Conventions
description: Python, TypeScript, and documentation style guidelines for IDP Platform contributors.
---

# :material-code-braces: Code Conventions

---

## :material-language-python: Python Conventions

### Style

- **Formatter:** `ruff format` (Black-compatible)
- **Linter:** `ruff check`
- **Type checker:** `mypy`
- **Python minimum:** 3.12

### Naming

| Element | Convention | Example |
|---------|-----------|---------|
| Modules | `snake_case` | `catalog_workspace.py` |
| Classes | `PascalCase` | `CatalogWorkspace` |
| Functions | `snake_case` | `focused_topology()` |
| Constants | `UPPER_SNAKE_CASE` | `DEFAULT_MAX_DESCRIPTOR_SIZE_BYTES` |
| Private | `_leading_underscore` | `_refresh_authority()` |

### Architecture Rules

- **No catalog rules in adapters.** The HTTP layer and LSP server translate data shapes; all business logic lives in `CatalogWorkspace` and the ingest pipeline.
- **Frozen dataclasses preferred** for value objects and snapshots.
- **`slots=True`** on all `dataclass` definitions where possible.
- **Imports:** absolute, never relative for cross-module imports.

### Testing

- **Framework:** `pytest`
- **Fixtures:** prefer factory functions over class-based fixtures
- **Names:** `test_{scenario_name}` — descriptive, not abbreviated

---

## :material-language-typescript: TypeScript Conventions

### Style

- **Formatter:** Prettier (via `npm run format` if configured)
- **Type checker:** `tsc --strict`
- **Minimum target:** ES2022

### Naming

| Element | Convention | Example |
|---------|-----------|---------|
| Files | `camelCase.ts` | `catalogSearch.ts` |
| Interfaces | `PascalCase` | `TopologyNode` |
| Functions | `camelCase` | `fetchTopology()` |
| Constants | `UPPER_SNAKE_CASE` or `camelCase` | `DEFAULT_DEPTH` |

### Architecture Rules

- **No catalog rules in TypeScript.** TypeScript maps Python data shapes for presentation; it never reimplements validation or topology rules.
- **Explicit `null` checks** — never rely on falsy coercions for optional fields.
- **Contract fixtures** are the source of truth for LSP/webview message shapes.

---

## :material-naming-convention: Field Naming Across Boundaries

| Context | Convention |
|---------|-----------|
| Python internal | `snake_case` |
| HTTP API (`openapi.yaml`) | `snake_case` |
| LSP custom methods | `camelCase` |
| Webview protocol | `camelCase` |

Explicit mappers convert between conventions at each boundary. Shared contract fixtures test both sides of every translation.

---

## :material-file-document: Documentation Conventions

- **Language:** English, active voice, present tense
- **Icons:** use Material Design icons in section headers (`:material-<name>:`)
- **Tables:** prefer tables over bullet lists for structured data
- **Code blocks:** always specify language for syntax highlighting
- **Links:** use relative Markdown links to other documentation pages

---

## :material-link: Further Reading

- [Development Workflow](workflow.md)
- [Architecture Boundaries](../architecture/boundaries.md)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)

---
title: Coding Conventions
description: Linting, typing, and style guidelines for the IDP Platform.
---

# :material-code-tags-check: Coding Conventions

To keep the codebase maintainable, we enforce strict formatting and typing rules across both Python and TypeScript.

---

## Python Conventions

We use **Ruff** for all Python linting and formatting. It replaces Flake8, Black, and isort.

### Running Ruff

```bash
cd idp-platform/backend

# Check for errors
ruff check .

# Fix auto-fixable errors
ruff check --fix .

# Format code
ruff format .
```

### Python Typing (Strict)

The backend uses Python 3.12+ type hints. We enforce **strict mode** with `pyright` (or `mypy`).

- Every function signature must be fully typed (arguments and return type).
- Use `|` for unions (e.g., `str | None` instead of `Optional[str]`).
- Use built-in generics (e.g., `list[str]`, `dict[str, int]`) instead of the `typing` module.
- Never use `Any` unless absolutely necessary (and if you do, leave a comment explaining why).

---

## TypeScript Conventions

We use **ESLint** for linting and **Prettier** for formatting.

### Running Linters

```bash
cd idp-platform/frontend  # or vscode-extension

# Check for errors
npm run lint

# Format code
npm run format
```

### TypeScript Typing (Strict)

Both the frontend and VS Code extension run with `"strict": true` in `tsconfig.json`.

- Every variable and function must have a type.
- Avoid `any`. Use `unknown` if you truly don't know the type, and then narrow it with a type guard.
- Interfaces for API responses must exactly match the JSON Contracts in `contracts/examples/`.

---

## Documentation Conventions

This site uses **MkDocs Material**.

When writing markdown documentation:

1. **Use clear, B1/B2 English.** Avoid complex idioms or jargon.
2. **Keep it visual.** Use Mermaid diagrams, icons, and tables where possible.
3. **Use admonitions.** Highlight important information using `!!! info`, `!!! warning`, etc.
4. **Include examples.** Don't just describe a field; show a YAML or JSON snippet.

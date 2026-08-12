---
title: CLI
description: Command-line interface for the IDP Platform catalog.
---

# :material-console: CLI

The **IDP Platform CLI** is a Typer-based command-line tool for local catalog operations.

---

## :material-alert-outline: Status

!!! warning "Under Development"
    The CLI is currently a **stub**. Commands are declared but not yet implemented. The structure is in place for future implementation.

---

## :material-download-circle: Installation

```bash
cd cli
pip install -e .
# or
uv sync
```

After installation, the `catalog` command is available:

```bash
catalog --help
```

---

## :material-format-list-bulleted: Commands Reference

### `catalog validate`

Validate a local descriptor and optionally consult the REST catalog.

```bash
catalog validate [PATH]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `PATH` | `catalog-info.yaml` | Path to the descriptor file to validate |

**Status:** Stub — not yet implemented.

---

### `catalog dependency add`

Select a catalog target and prepare a local YAML dependency change.

```bash
catalog dependency add [PATH]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `PATH` | `catalog-info.yaml` | Path to the descriptor to add the dependency to |

**Status:** Stub — not yet implemented.

---

## :material-package: Dependencies

| Package | Purpose |
|---------|---------|
| `typer ≥ 0.12` | CLI framework |
| `httpx ≥ 0.27` | HTTP client for catalog API calls |
| `pyyaml ≥ 6.0.2` | YAML parsing |
| `mkdocs-material` | Documentation (bundled for convenience) |

---

## :material-link: Further Reading

- [Typer Documentation](https://typer.tiangolo.com/)
- [httpx Documentation](https://www.python-httpx.org/)
- [HTTP API Reference](../api/index.md)

---
title: CLI Commands
description: Detailed CLI command reference for the IDP Platform catalog tool.
---

# :material-console: CLI Commands Reference

```
catalog --help

 Usage: catalog [OPTIONS] COMMAND [ARGS]...

 Service Catalog CLI.

╭─ Options ──────────────────────────────────────────────────╮
│ --help  Show this message and exit.                         │
╰─────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────╮
│ validate   Validate a local descriptor                      │
│ dependency Manage declared YAML dependencies                │
╰─────────────────────────────────────────────────────────────╯
```

---

## `catalog validate`

```
catalog validate --help

 Usage: catalog validate [OPTIONS] [PATH]

 Validate a local descriptor and optionally consult the REST catalog.

╭─ Arguments ────────────────────────────────────────────────╮
│ path  [PATH]  [default: catalog-info.yaml]                  │
╰─────────────────────────────────────────────────────────────╯
```

---

## `catalog dependency`

```
catalog dependency --help

 Usage: catalog dependency [OPTIONS] COMMAND [ARGS]...

 Manage declared YAML dependencies.

╭─ Commands ─────────────────────────────────────────────────╮
│ add  Select a catalog target and prepare a YAML change      │
╰─────────────────────────────────────────────────────────────╯
```

### `catalog dependency add`

```
catalog dependency add --help

 Usage: catalog dependency add [OPTIONS] [PATH]

 Select a catalog target and prepare a local YAML dependency change.

╭─ Arguments ────────────────────────────────────────────────╮
│ path  [PATH]  [default: catalog-info.yaml]                  │
╰─────────────────────────────────────────────────────────────╯
```

---

## :material-link: Further Reading

- [CLI Index](index.md)
- [Typer Documentation](https://typer.tiangolo.com/)

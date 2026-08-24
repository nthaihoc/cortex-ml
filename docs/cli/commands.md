---
title: CLI Commands
description: Planned commands for the IDP Platform CLI.
---

# :material-format-list-bulleted-type: CLI Commands

!!! warning "Planned Feature"
    The CLI is not yet implemented. This page describes the planned command structure.

---

## `idp validate`

Validates all `catalog-info.yaml` files in a directory and exits with a non-zero status code if any blocking errors are found.

**Usage in CI/CD:**

```bash
# Validates the current directory
idp validate

# Validates a specific directory
idp validate ./my-services

# Outputs results as JSON for other tools
idp validate --format=json
```

**Output:**
Prints a human-readable summary of all diagnostics, similar to the `GET /api/v1/catalog/diagnostics` endpoint.

---

## `idp query`

Queries the catalog for specific entities or relations.

```bash
# Find an entity by exact reference
idp query component:platform/payment-gateway

# Search entities by name
idp query --search "Payment"
```

---

## `idp generate`

Scaffolds a new `catalog-info.yaml` file based on a template.

```bash
# Interactive prompt to create a new service
idp generate service

# Non-interactive generation
idp generate service --id=my-service --namespace=platform --owner=team-a
```

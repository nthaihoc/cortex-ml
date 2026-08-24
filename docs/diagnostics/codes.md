---
title: Diagnostic Codes
description: Complete reference for all 22 IDP Platform validation diagnostic codes.
---

# :material-format-list-numbered: Diagnostic Codes

The validation engine produces 22 distinct diagnostic codes. This page lists all of them, what they mean, and how to fix them.

---

## Parser Diagnostics

These errors happen when the file is not valid YAML or violates security constraints. **All parser diagnostics are blocking errors.**

| Code | Meaning | How to fix |
|------|---------|------------|
| `YAML_INVALID_UTF8` | File is not UTF-8 encoded | Save the file as UTF-8 |
| `YAML_SYNTAX_ERROR` | Basic YAML syntax error | Fix the YAML formatting (indentation, quotes) |
| `YAML_MULTIPLE_DOCUMENTS` | File contains `---` document separators | Remove the separators, keep only one document |
| `YAML_ROOT_NOT_MAPPING` | The top level of the file is a list or scalar | Make sure the root is a dictionary/object |
| `YAML_ALIAS_UNSUPPORTED` | File uses YAML anchors `&a` or aliases `*a` | Remove them and copy/paste values instead |
| `YAML_NON_STRING_KEY` | A dictionary key is a number or boolean | Quote the key (e.g., `"123": value`) |
| `YAML_DUPLICATE_KEY` | The same key appears twice in an object | Remove or rename one of the keys |
| `YAML_TAG_UNSUPPORTED` | File uses custom tags like `!!str` | Remove the tags |
| `YAML_TIMESTAMP_UNSUPPORTED` | Value looks like an unquoted timestamp | Put quotes around the timestamp |
| `YAML_NON_FINITE_NUMBER` | Contains `NaN` or `Infinity` | Remove or quote these values |

---

## Schema Diagnostics

These errors happen when the YAML is valid, but the content violates the expected schema. **All schema diagnostics are blocking errors.**

| Code | Meaning | How to fix |
|------|---------|------------|
| `SCHEMA_SPEC_VERSION_INVALID` | Unknown `specVersion` | Must be `vsf-idp.io/v2` |
| `SCHEMA_API_VERSION_REQUIRED` | Missing `apiVersion` (Backstage) | Add `apiVersion: backstage.io/v1alpha1` |
| `SCHEMA_KIND_REQUIRED` | Missing `kind` (Backstage) | Add `kind: Component` (or similar) |
| `SCHEMA_METADATA_REQUIRED` | Missing `metadata` object | Add a `metadata` section |
| `SCHEMA_METADATA_NAME_REQUIRED` | Missing `metadata.name` (Backstage) | Add `name` under `metadata` |
| `SCHEMA_SPEC_INVALID` | `spec` is not an object | Change `spec` to be an object/dictionary |
| `SCHEMA_FIELD_REQUIRED` | A required field is missing | Add the required field (e.g., `techlead` owner) |
| `SCHEMA_FIELD_INVALID` | Field has wrong type or format | Correct the format (e.g., check regex constraints) |

---

## Reference Diagnostics

These diagnostics relate to entity references.

| Code | Severity | Meaning | How to fix |
|------|----------|---------|------------|
| `REFERENCE_INVALID` | :material-close-circle:{ .error } Error (Blocking) | Reference syntax is malformed | Use format `kind:namespace/name` |
| `REFERENCE_TARGET_NOT_FOUND` | :material-alert:{ .warning } Warning | Target entity does not exist | Create the target entity, or check for typos |

---

## Topology Diagnostics

These diagnostics relate to graph connections.

| Code | Severity | Meaning | How to fix |
|------|----------|---------|------------|
| `TOPOLOGY_SELF_REFERENCE` | :material-close-circle:{ .error } Error (Blocking) | Entity declares a relation to itself | Remove the self-referencing topology entry |

---

## Identity Diagnostics

These diagnostics happen during identity resolution (after validation).

| Code | Severity | Meaning | How to fix |
|------|----------|---------|------------|
| `ENTITY_DUPLICATE_REF` | :material-close-circle:{ .error } Error (Blocking) | Multiple files claim the same reference | Change `metadata.namespace` or ID in one file |

---

## File Diagnostics

These diagnostics relate to filesystem limits.

| Code | Severity | Meaning | How to fix |
|------|----------|---------|------------|
| `CATALOG_DESCRIPTOR_TOO_LARGE` | :material-close-circle:{ .error } Error (Blocking) | File exceeds the 1 MB limit | Split the catalog definitions, or reduce description size |

---

<style>
.error { color: #ef4444; }
.warning { color: #f59e0b; }
</style>

---
title: Ingest Pipeline
description: How catalog descriptors are parsed, normalized, and projected into relations.
---

# :material-pipe: Ingest Pipeline

The ingest pipeline transforms raw `catalog-info.yaml` bytes into typed, normalized `Entity` objects and `Relation` tuples. It is composed of three independent stages.

---

## :material-numeric-1-circle: Stage 1: YAML Parsing — `HardenedYamlParser`

**File:** `backend/app/ingest/parser.py`

The parser enforces a **strict YAML 1.2 JSON-compatible subset** to prevent security and correctness issues.

### What it does

- Decodes bytes as UTF-8
- Parses the YAML document tree using PyYAML with a custom `JsonScalarLoader`
- Recursively converts the node tree to Python primitives
- Enforces all safety constraints

### Safety Constraints

| Constraint | Error Code |
|-----------|------------|
| Must be valid UTF-8 | `YAML_INVALID_UTF8` |
| Must be parseable YAML | `YAML_SYNTAX_ERROR` |
| Must be exactly 1 document | `YAML_MULTIPLE_DOCUMENTS` |
| Root must be a mapping | `YAML_ROOT_NOT_MAPPING` |
| No YAML aliases/anchors | `YAML_ALIAS_UNSUPPORTED` |
| All keys must be strings | `YAML_NON_STRING_KEY` |
| No duplicate mapping keys | `YAML_DUPLICATE_KEY` |
| No unsupported tags | `YAML_TAG_UNSUPPORTED` |
| No timestamps as bare values | `YAML_TIMESTAMP_UNSUPPORTED` |
| No NaN or Infinity values | `YAML_NON_FINITE_NUMBER` |

### Example

```python
from app.ingest.parser import HardenedYamlParser, DescriptorParseError

parser = HardenedYamlParser()

try:
    descriptor = parser.parse(b"specVersion: vsf-idp.io/v2\n...")
except DescriptorParseError as e:
    print(e.code)       # e.g., "YAML_SYNTAX_ERROR"
    print(e.message)    # Human-readable message
    print(e.line)       # Line number (if available)
    print(e.column)     # Column number (if available)
    print(e.field_path) # JSON path (e.g., "$.spec.owners")
```

---

## :material-numeric-2-circle: Stage 2: Normalization — `BackstageEntityNormalizer`

**File:** `backend/app/ingest/normalizer.py`

Normalizes a raw descriptor dict into a typed `Entity` Pydantic model with a canonical `entity_ref`.

### Supported Formats

=== "VSF IDP v2"

    - Detects `"specVersion" in descriptor`
    - Validates `specVersion == "vsf-idp.io/v2"`
    - Computes `reference = component:{metadata.namespace}/{spec.id}`
    - Adds synthetic `metadata.name`, `metadata.title`, `metadata.description`
    - Returns `Entity.model_validate(payload)`

=== "Backstage"

    - Uses `apiVersion`, `kind`, `metadata.name`, `metadata.namespace`
    - Computes `reference = {kind}:{namespace}/{name}` (all lowercased)
    - Normalizes all reference fields in `spec` to canonical form
    - Returns `Entity.model_validate(payload)`

### Reference Normalization

`spec` fields containing entity reference strings are automatically normalized:

| Field | Default Kind | Multiple? |
|-------|-------------|-----------|
| `spec.owner` | `group` | No |
| `spec.system` | `system` | No |
| `spec.domain` | `domain` | No |
| `spec.parent` | `group` | No |
| `spec.dependsOn[]` | `component` | Yes |
| `spec.providesApis[]` | `api` | Yes |
| `spec.consumesApis[]` | `api` | Yes |
| `spec.publishesTo[]` | `event` | Yes |
| `spec.consumesFrom[]` | `event` | Yes |

---

## :material-numeric-3-circle: Stage 3: Relation Projection — `BackstageRelationProjector`

**File:** `backend/app/ingest/relation_projector.py`

Projects declared spec fields into a list of typed `Relation` value objects.

### Output

```python
@dataclass(frozen=True, slots=True)
class ProjectionResult:
    relations: tuple[Relation, ...]
    issues: tuple[ValidationIssue, ...]
```

### Deduplication

Duplicate `(source, relation_type, target)` triplets are automatically deduplicated — only the first occurrence is kept.

### Self-Reference Detection

If `source == target`, a `TOPOLOGY_SELF_REFERENCE` issue is generated.

### Missing Target Detection

If `known_entity_refs` is provided, references not in the set generate `REFERENCE_TARGET_NOT_FOUND` issues.

---

## :material-link: Further Reading

- [CatalogWorkspace](catalog-workspace.md)
- [Validation Engine](validation.md)
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [Pydantic Documentation](https://docs.pydantic.dev/)

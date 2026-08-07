---
title: Validation Engine
description: How the CatalogValidationEngine validates VSF IDP v2 and Backstage descriptors.
---

# :material-check-circle-outline: Validation Engine

**File:** `backend/app/validators/engine.py`

The `CatalogValidationEngine` is the single authoritative validator for all catalog descriptors. It runs the same validation logic for filesystem, HTTP, and LSP adapters.

---

## :material-layers: Validation Stages

```mermaid
flowchart LR
    A[descriptor dict] --> B{specVersion\npresent?}
    B -->|Yes| C[VSF IDP v2\nschema checks]
    B -->|No| D[Backstage\nschema checks]
    C --> E{blocking\nissues?}
    D --> E
    E -->|Yes| F[return early\nno entity]
    E -->|No| G[BackstageEntityNormalizer\n.normalize()]
    G --> H[BackstageRelationProjector\n.project()]
    H --> I[ValidationOutcome\n entity + relations + report]
```

---

## :material-star: VSF IDP v2 Schema Validation

Applied when `"specVersion" in descriptor`.

| Rule | Field | Code |
|------|-------|------|
| `specVersion` must be `"vsf-idp.io/v2"` | `specVersion` | `SCHEMA_SPEC_VERSION_INVALID` |
| `metadata` must be an object | `metadata` | `SCHEMA_METADATA_REQUIRED` |
| `spec` must be an object | `spec` | `SCHEMA_SPEC_INVALID` |
| `metadata.namespace` required, matches `^[a-z][a-z0-9-]*$` | `metadata.namespace` | `SCHEMA_FIELD_REQUIRED` / `SCHEMA_FIELD_INVALID` |
| `metadata.system` required, matches pattern | `metadata.system` | `SCHEMA_FIELD_REQUIRED` / `SCHEMA_FIELD_INVALID` |
| `metadata.domain` required, ≤ 128 printable chars | `metadata.domain` | `SCHEMA_FIELD_REQUIRED` / `SCHEMA_FIELD_INVALID` |
| `spec.id` required, matches pattern | `spec.id` | `SCHEMA_FIELD_REQUIRED` / `SCHEMA_FIELD_INVALID` |
| `spec.name` required, no control chars | `spec.name` | `SCHEMA_FIELD_REQUIRED` / `SCHEMA_FIELD_INVALID` |
| `spec.type` one of 13 supported types | `spec.type` | `SCHEMA_FIELD_REQUIRED` / `SCHEMA_FIELD_INVALID` |
| `spec.owners.members` non-empty array | `spec.owners.members` | `SCHEMA_FIELD_REQUIRED` |
| Each member has valid email | `spec.owners.members[*].user` | `SCHEMA_FIELD_INVALID` |
| Each member has valid role | `spec.owners.members[*].role` | `SCHEMA_FIELD_INVALID` |
| At least one `techlead` role | `spec.owners.members` | `SCHEMA_FIELD_REQUIRED` |
| `spec.review.branch` required for `service`/`gateway` | `spec.review.branch` | `SCHEMA_FIELD_REQUIRED` |
| `spec.topology` must be array if present | `spec.topology` | `SCHEMA_FIELD_INVALID` |
| Each topology item must have `ref` only | `spec.topology[*]` | `SCHEMA_FIELD_INVALID` |

---

## :material-history: Backstage Schema Validation

Applied when `"specVersion"` is absent.

| Rule | Field | Code |
|------|-------|------|
| `apiVersion` non-blank string | `apiVersion` | `SCHEMA_API_VERSION_REQUIRED` |
| `kind` non-blank string | `kind` | `SCHEMA_KIND_REQUIRED` |
| `metadata` must be an object | `metadata` | `SCHEMA_METADATA_REQUIRED` |
| `metadata.name` non-blank string | `metadata.name` | `SCHEMA_METADATA_NAME_REQUIRED` |
| `spec` must be an object if present | `spec` | `SCHEMA_SPEC_INVALID` |

---

## :material-check-decagram: Validation Outcome

```python
@dataclass(frozen=True, slots=True)
class ValidationOutcome:
    entity: Entity | None          # None if validation failed
    relations: tuple[Relation, ...] # Empty if blocking issues exist
    report: ValidationReport        # All issues, ordered and deduplicated
```

```python
@dataclass(frozen=True, slots=True)
class ValidationReport:
    valid: bool                     # True if no blocking issues
    issues: tuple[ValidationIssue, ...]
```

---

## :material-code-braces: Using the Validation Engine

```python
from app.validators.engine import CatalogValidationEngine
from app.ingest.normalizer import BackstageEntityNormalizer
from app.ingest.relation_projector import BackstageRelationProjector

engine = CatalogValidationEngine(
    BackstageEntityNormalizer(),
    BackstageRelationProjector(),
)

outcome = engine.validate(
    descriptor,
    source_uri="file:///path/to/catalog-info.yaml",
    relative_path="my-service/catalog-info.yaml",
    document_version="optional-version",
)

if outcome.report.valid:
    print("Entity:", outcome.entity.entity_ref)
    print("Relations:", len(outcome.relations))
else:
    for issue in outcome.report.issues:
        print(f"[{issue.severity}] {issue.code}: {issue.message}")
```

---

## :material-link: Further Reading

- [Diagnostic Codes](../diagnostics/codes.md)
- [Ingest Pipeline](ingest-pipeline.md)
- [CatalogWorkspace](catalog-workspace.md)

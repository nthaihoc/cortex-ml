---
title: CatalogValidationEngine
description: Schema và topology validation cho VSF IDP v2 và Backstage descriptors.
---

# :material-check-decagram: `CatalogValidationEngine`

**File:** `backend/app/validators/engine.py`

`CatalogValidationEngine` chạy validation trên parsed descriptor, tạo ra `ValidationReport` chứa danh sách `ValidationIssue`. Đây là engine duy nhất cho cả filesystem scanning, HTTP entity writes, và LSP diagnostics.

---

## :material-cog: Khởi tạo

```python
engine = CatalogValidationEngine(
    normalizer=BackstageEntityNormalizer(),
    projector=BackstageRelationProjector(),
    get_system_values=lambda: frozenset(known_systems),  # Tuỳ chọn
)
```

Tham số `get_system_values` cho phép validate `metadata.system` tồn tại trong catalog (cho VSF v2).

---

## :material-play: Luồng `validate()`

```python
outcome: ValidationOutcome = engine.validate(
    descriptor,
    source_uri="file:///...",
    relative_path="my-service/catalog-info.yaml",
    document_version="sha256-hash",
    known_entity_refs={"component:platform/auth-service"},
)
```

`ValidationOutcome` chứa:

| Field | Type | Mô tả |
|---|---|---|
| `entity` | `NormalizedDescriptor \| None` | `None` nếu có blocking issue |
| `relations` | `tuple[Relation, ...]` | Quan hệ đã chiếu |
| `report` | `ValidationReport` | Tất cả `ValidationIssue` |

---

## :material-format-list-checks: Schema Rules

### VSF IDP v2 (`specVersion: vsf-idp.io/v2`)

| Trường | Quy tắc | Blocking? |
|---|---|---|
| `specVersion` | Phải chính xác `"vsf-idp.io/v2"` | ✅ |
| `metadata` | Bắt buộc, phải là object | ✅ |
| `metadata.domain` | Bắt buộc, ≤ 128 ký tự in được | ✅ |
| `metadata.system` | Bắt buộc, khớp `^[a-z][a-z0-9-]*$`, phải tồn tại trong catalog | ✅ |
| `metadata.namespace` | Bắt buộc, khớp `^[a-z][a-z0-9-]*$` | ✅ |
| `spec` | Bắt buộc, phải là object | ✅ |
| `spec.type` | Một trong: `service`, `gateway`, `worker`, `batch`, `job`, `library`, `website`, `mobile-app`, `data-pipeline`, `function`, `plugin`, `tool`, `documentation`, `other`; hoặc custom khớp `^[a-z][a-z0-9-]*$` | ✅ |
| `spec.id` | Bắt buộc, khớp `^[a-z][a-z0-9-]*$` | ✅ |
| `spec.name` | Bắt buộc, không chứa ký tự điều khiển | ✅ |
| `spec.owners.members` | Nếu không rỗng, phải có ≥ 1 `techlead` | ✅ |
| `spec.owners.members[*].user` | Phải khớp `*@vinsmartfuture.tech` | ✅ |
| `spec.owners.members[*].role` | Phải là `techlead`, `maintainer`, hoặc `member` | ✅ |
| `spec.review.branch` | Bắt buộc khi `spec.type` = `service` hoặc `gateway` | ✅ |
| `spec.topology[*]` | Mỗi item phải có `ref`; chỉ `protocol` và `reason` là tuỳ chọn | ✅ |

### Backstage

| Trường | Quy tắc | Blocking? |
|---|---|---|
| `apiVersion` | Bắt buộc, chuỗi không rỗng | ✅ |
| `kind` | Bắt buộc, chuỗi không rỗng | ✅ |
| `metadata` | Bắt buộc, phải là object | ✅ |
| `metadata.name` | Bắt buộc, chuỗi không rỗng | ✅ |
| `spec` | Nếu có, phải là object | ✅ |

---

## :material-alert-circle: `ValidationIssue`

```python
@dataclass(frozen=True, slots=True)
class ValidationIssue:
    code: str           # Mã ổn định, VD: "SCHEMA_FIELD_REQUIRED"
    severity: str       # "error" | "warning"
    blocking: bool      # True = ngăn tạo NormalizedDescriptor
    message: str        # Mô tả lỗi
    provenance: DocumentProvenance
    entity_ref: str | None
    target_ref: str | None
    suggested_action: str | None
    details: dict | None
```

---

## :material-link: Đọc thêm

- [Ingest Pipeline](ingest-pipeline.md)
- [Bảng mã Diagnostic](../diagnostics/codes.md)
- [Luồng dữ liệu](../architecture/data-flow.md)

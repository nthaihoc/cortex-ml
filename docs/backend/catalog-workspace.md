---
title: CatalogWorkspace
description: Deep-dive into the CatalogWorkspace core module — the heart of the IDP Platform.
---

# :material-brain: CatalogWorkspace

`CatalogWorkspace` (`backend/app/catalog_workspace/workspace.py`) is the **deep module** at the center of the IDP Platform. All catalog semantics — parsing, normalization, validation, relation projection, conflict detection, focused traversal, and diagnostics — flow through this single class.

---

## :material-api: Public Interface

### Construction

```python
workspace = CatalogWorkspace.open(CatalogScope(roots=("file:///path/to/catalog",)))
```

### Document Lifecycle

```python
# Add or update a document
workspace.upsert_document(
    source_uri="file:///path/to/catalog-info.yaml",
    relative_path="my-service/catalog-info.yaml",
    content=b"specVersion: vsf-idp.io/v2\n...",
    version="optional-version-string",
)

# Remove a document
workspace.remove_document("file:///path/to/catalog-info.yaml")
```

### Reading State

```python
# Full in-memory snapshot
snapshot: CatalogSnapshot = workspace.snapshot()

# All current diagnostics
diagnostics: tuple[CatalogDiagnostic, ...] = workspace.diagnostics()

# One-hop focused topology
topology: FocusedTopology = workspace.focused_topology(
    "component:platform/payment-gateway",
    direction="both",  # "incoming" | "outgoing" | "both"
    depth=1,           # Fixed at 1
)

# Topology by document URI (before entity is resolved)
topology = workspace.focused_topology_for_document(
    "file:///path/to/catalog-info.yaml",
    direction="both",
)
```

---

## :material-state-machine: Document Processing

When `upsert_document()` is called:

1. **Parse** — `HardenedYamlParser.parse()` converts bytes to `dict`
2. **Validate** — `CatalogValidationEngine.validate()` runs schema + topology checks
3. **If invalid** → record failure:
   - If document was previously valid: mark as **stale** (retain last-valid entity)
   - If document was never valid: record as **draft**
4. **If valid** → normalize entity, extract canonical reference
5. **Authority resolution** — update candidate map, promote or create conflict
6. **Increment revision**

---

## :material-graph: Focused Topology Algorithm

`focused_topology(root, direction, depth=1)`:

1. Build outgoing and incoming adjacency maps from all resolved relations
2. Start with `frontier = {root_ref}`
3. For each hop (depth=1):
   - If `direction` includes `"outgoing"`: follow all outgoing edges from frontier
   - If `direction` includes `"incoming"`: follow all incoming edges from frontier
   - Add newly discovered nodes to `included`
4. Collect all relations involving any included node pair
5. Build `TopologyNode` for each included reference (entity/draft/conflict/unresolved)

---

## :material-alert: Conflict Detection

When two documents claim the same canonical reference (`kind:namespace/name`):

- Both are added to `_candidates_by_ref[reference]`
- `_refresh_authority()` detects `len(candidates) > 1` → removes from `_entities`
- The conflict is surfaced via `_conflicts()` returning an `IdentityConflict`
- Diagnostics include `ENTITY_DUPLICATE_REF` for each conflicting document

---

## :material-data-matrix: Data Models

### `CatalogScope`

```python
@dataclass(frozen=True, slots=True)
class CatalogScope:
    roots: tuple[str, ...]  # Catalog root URIs
```

### `CatalogSnapshot`

```python
@dataclass(frozen=True, slots=True)
class CatalogSnapshot:
    revision: int
    entities: Mapping[str, CatalogEntity]
    relations: tuple[CatalogRelation, ...]
    conflicts: Mapping[str, IdentityConflict]
    drafts: Mapping[str, DraftEntity]
    diagnostics: tuple[CatalogDiagnostic, ...]
```

### `FocusedTopology`

```python
@dataclass(frozen=True, slots=True)
class FocusedTopology:
    root: str                    # Root entity reference
    direction: TopologyDirection  # "incoming" | "outgoing" | "both"
    depth: int | None            # Fixed at 1
    nodes: Mapping[str, TopologyNode]
    relations: tuple[CatalogRelation, ...]
```

---

## :material-link: Further Reading

- [Ingest Pipeline](ingest-pipeline.md)
- [Validation Engine](validation.md)
- [State Management](../architecture/state.md)
- [API Schemas](../api/schemas.md)

---
title: Acceptance Coverage
description: Milestone 1 acceptance scenarios and their automated test evidence.
---

# :material-check-decagram: Acceptance Coverage

All **Milestone 1** specification scenarios have automated test evidence. Scenario 20 additionally has a manual release gate.

---

## :material-list-status: Acceptance Scenarios

| # | Scenario | Automated Evidence |
|---|----------|-------------------|
| 1 | **Nested discovery** | `test_catalog_descriptor_is_discovered_beyond_legacy_depth_limit` |
| 2 | **Healthy relation** | `test_one_valid_document_produces_one_canonical_entity` + `test_standard_fields_and_spec_topology_share_one_relation_model` |
| 3 | **Missing target warning** | `test_missing_relation_target_is_warning_placeholder_without_harming_source` |
| 4 | **Blocking source isolation** | `test_loading_mixed_descriptors_keeps_valid_snapshot_and_invalid_diagnostic` |
| 5 | **Current-session last valid** | `test_invalid_update_keeps_last_valid_entity_as_error_and_stale` |
| 6 | **Invalid startup draft** | `test_invalid_save_keeps_process_state_but_restart_has_no_snapshot` |
| 7 | **Case-only duplicate** | `test_case_only_duplicate_refs_create_conflict_without_authoritative_entity` |
| 8 | **Title keeps identity** | `test_title_change_preserves_identity_and_name_change_replaces_it` |
| 9 | **Name changes identity** | Same test as #8 above |
| 10 | **Move preserves identity/provenance** | `test_move_preserves_entity_identity_and_updates_provenance` |
| 11 | **Delete restores unresolved target** | `test_removing_source_removes_entity_and_leaves_incoming_relation_unresolved` |
| 12 | **Incremental save** | `test_save_burst_applies_latest_source_once_without_reparsing_unchanged_files` |
| 13 | **Saved editor focus** | Extension: `activates one language client and opens the default focused topology beside the editor` |
| 14 | **Valid unsaved debounce** | `test_superseded_and_stale_document_versions_cannot_replace_latest_result` |
| 15 | **Invalid unsaved last valid and diagnostics** | `test_unsaved_edits_publish_current_diagnostics_and_keep_last_valid_topology` |
| 16 | **Draft rekey** | `test_new_invalid_document_rekeys_from_uri_draft_to_canonical_identity` + webview `keeps the graph canvas mounted when a draft rekeys` |
| 17 | **Editor follow and pin** | Extension: `follows active descriptors, validates messages, and holds focus while pinned` |
| 18 | **Cross-folder scope** | `test_initialization_builds_one_cross_folder_catalog_scope` |
| 19 | **Loopback/no login** | `test_development_entrypoint_loads_catalog_root_and_binds_loopback` + local API tests |
| 20 | **Service-free suites** | Run backend `pytest`, frontend test/build, and extension test/check/build from `README.md` |

---

## :material-clipboard-text: Scenario 20 — Manual Release Gate

Scenario 20 requires a **fresh clone** verification:

1. Clone the repository to a new directory
2. Follow the instructions in [`README.md`](https://github.com/truongabc-group1/idp/blob/main/idp-platform/README.md) exactly
3. Confirm:
   - Backend starts and serves the catalog with no extra services
   - Browser viewer loads and shows topology
   - VS Code extension (`F5`) shows diagnostics and topology in the editor
   - No external service, database, container, or network access is required

---

## :material-scale-balance: Scale Evidence

Scale scenarios are covered by:

| Test | Evidence |
|------|---------|
| Focused view bounded at scale | `test_generated_catalog_keeps_focused_view_bounded` |
| 5,000-entity search | `catalogSearch.bench.ts` (< 20 ms) |
| Fixed one-hop viewer | `TopologyViewer.test.tsx` — mount count assertions |
| Performance measurements | [Performance Benchmarks](../performance/benchmarks.md) |

---

## :material-link: Further Reading

- [Backend Tests](backend.md)
- [Frontend Tests](frontend.md)
- [Extension Tests](extension.md)
- [Performance Benchmarks](../performance/benchmarks.md)

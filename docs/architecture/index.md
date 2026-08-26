---
title: Kiến trúc
description: Tổng quan kiến trúc hệ thống IDP Platform.
---

# :material-sitemap: Kiến trúc

<div class="grid cards" markdown>

-   :material-view-dashboard-outline: **Tổng quan hệ thống**

    Bản đồ thành phần và cấu trúc repository.

    [:octicons-arrow-right-24: Tổng quan](overview.md)

-   :material-fence: **Ranh giới Module**

    Quy tắc ràng buộc của từng thành phần.

    [:octicons-arrow-right-24: Ranh giới](boundaries.md)

-   :material-transit-connection-variant: **Luồng dữ liệu**

    Pipeline xử lý từ YAML bytes tới `CatalogSnapshot`.

    [:octicons-arrow-right-24: Luồng dữ liệu](data-flow.md)

-   :material-state-machine: **Quản lý trạng thái**

    `TopologyNodeState`, last-valid state, và `IdentityConflict`.

    [:octicons-arrow-right-24: Trạng thái](state.md)

</div>

!!! info "Nguyên tắc cốt lõi"
    **Python sở hữu toàn bộ catalog semantics.** `CatalogWorkspace` là "deep module" — callers chỉ cần gọi `upsert_document()` / `remove_document()` và đọc `CatalogSnapshot`. Toàn bộ logic parsing, validation, relation projection, conflict detection, và focused traversal được ẩn bên trong.

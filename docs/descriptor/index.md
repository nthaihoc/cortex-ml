---
title: Định dạng Descriptor
description: Hướng dẫn viết file catalog-info.yaml cho VSF IDP v2 và Backstage.
---

# :material-file-code-outline: Định dạng Descriptor

File `catalog-info.yaml` là đơn vị dữ liệu cơ bản của IDP Platform. Mỗi file mô tả một entity (service, component, system, ...) và quan hệ (topology) của nó.

<div class="grid cards" markdown>

-   :material-new-box: **VSF IDP v2**

    Định dạng chính, sử dụng `specVersion: vsf-idp.io/v2`.

    [:octicons-arrow-right-24: VSF IDP v2](vsf-v2.md)

-   :material-swap-horizontal: **Tương thích Backstage**

    Hỗ trợ đầy đủ descriptor format của Backstage.

    [:octicons-arrow-right-24: Backstage](backstage.md)

-   :material-fingerprint: **Quy tắc định danh**

    Canonical `EntityReference` — `kind:namespace/name`.

    [:octicons-arrow-right-24: Định danh](identity.md)

-   :material-graph: **Trường Topology**

    Khai báo quan hệ giữa các entity qua `spec.topology`.

    [:octicons-arrow-right-24: Topology](topology.md)

</div>

!!! info "Dual Schema"
    `CatalogValidationEngine` tự phát hiện format dựa trên sự hiện diện của `specVersion`. Nếu `specVersion` tồn tại → VSF IDP v2; nếu không → Backstage.

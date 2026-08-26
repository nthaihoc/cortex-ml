---
title: Frontend
description: Tổng quan React frontend — TopologyViewer, HttpCatalogClient, và catalog search.
---

# :material-react: Frontend

Frontend sử dụng React 19 + ReactFlow 11 + Vite, cung cấp `TopologyViewer` trên browser.

<div class="grid cards" markdown>

-   :material-graph: **`TopologyViewer`**

    Component chính hiển thị focused topology graph.

    [:octicons-arrow-right-24: Chi tiết](topology-viewer.md)

-   :material-magnify: **Tìm kiếm Catalog**

    Full-text search qua `CatalogSearchIndex`.

    [:octicons-arrow-right-24: Chi tiết](catalog-search.md)

-   :material-palette: **Trạng thái hiển thị**

    Màu sắc và icon theo `Health`, `Freshness`, `TopologyNodeState`.

    [:octicons-arrow-right-24: Chi tiết](visual-states.md)

</div>

---

## :material-cog: Stack

| Thành phần | Phiên bản | Vai trò |
|---|---|---|
| React | 19 | UI framework |
| ReactFlow | 11 | Graph rendering |
| Vite | 7 | Dev server + bundler |
| TypeScript | 5.6+ | Type safety |

## :material-layers-outline: Cấu trúc

```
frontend/src/
├── main.tsx                    # React root
├── app/App.tsx                 # Application shell
├── catalog/
│   ├── HttpCatalogClient.ts    # HTTP API client
│   ├── CatalogProvider.tsx     # React context
│   ├── client.ts               # Client interface
│   └── types.ts                # TypeScript types
└── topology/
    ├── TopologyViewer.tsx       # Main component
    ├── topologyLayout.ts        # Graph layout algorithm
    ├── localContract.ts         # API type mapping
    ├── catalogSearch.ts         # Search logic
    └── types.ts                 # Shared types
```

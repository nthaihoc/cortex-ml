---
title: Frontend
description: React browser viewer for the IDP Platform catalog topology.
---

# :material-react: Frontend

The frontend is a **React 19** application that displays the catalog topology in your browser. It uses **ReactFlow** to render the interactive graph and **Vite** for the development server.

**Location:** `frontend/src/`

---

<div class="grid cards" markdown>

-   :material-graph:{ .lg .middle } **Topology Viewer**

    The main ReactFlow component that renders nodes and edges.

    [:octicons-arrow-right-24: Topology Viewer](topology-viewer.md)

-   :material-text-search:{ .lg .middle } **Catalog Search**

    The full-text search implementation for finding entities.

    [:octicons-arrow-right-24: Catalog Search](catalog-search.md)

-   :material-palette-outline:{ .lg .middle } **Visual States**

    How health, freshness, and node types are styled.

    [:octicons-arrow-right-24: Visual States](visual-states.md)

</div>

---

## Design Principles

Following the [Module Boundaries](../architecture/boundaries.md) rules, the frontend is **pure presentation**.

- **No Validation:** It never parses YAML or checks schema rules.
- **No Identity Resolution:** It uses the `reference` strings exactly as provided by the API.
- **State Driven:** It just reacts to the `/api/v1/catalog/topology` data.

---

## API Client

The `HttpLocalCatalogClient` (`frontend/src/localCatalog/HttpLocalCatalogClient.ts`) handles all communication with the backend.

It provides typed methods for:
- Fetching the health status
- Fetching the focused topology
- Connecting to the SSE stream (`/api/v1/catalog/events`)

When the SSE stream emits a `revisionChanged` event, the client triggers a callback that tells React to re-fetch the current view.

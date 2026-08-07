---
title: Frontend
description: React + ReactFlow browser topology viewer for the IDP Platform.
---

# :material-react: Frontend

The frontend is a **React 19 + ReactFlow 11 + Vite 7** browser application that provides an interactive topology viewer for the local catalog.

<div class="grid cards" markdown>

-   :material-graph:{ .lg .middle } **Topology Viewer**

    Interactive node graph with health badges and one-hop navigation.

    [:octicons-arrow-right-24: Topology Viewer](topology-viewer.md)

-   :material-magnify:{ .lg .middle } **Catalog Search**

    Full-text search over the complete catalog snapshot.

    [:octicons-arrow-right-24: Catalog Search](catalog-search.md)

-   :material-palette-outline:{ .lg .middle } **Visual States**

    Health, freshness, and state badges used across the UI.

    [:octicons-arrow-right-24: Visual States](visual-states.md)

</div>

---

## :material-console: Running the Frontend

```bash
cd frontend
npm install
npm run dev
```

The development server starts at `http://localhost:5173`. API calls are proxied to `http://127.0.0.1:8000` via the Vite dev proxy.

---

## :material-package: Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `react` | ^19.0.0 | UI framework |
| `react-dom` | ^19.0.0 | DOM rendering |
| `reactflow` | ^11.4.0 | Graph/topology visualization |
| `vite` | ^7.3.6 | Build tool + dev server |
| `typescript` | ^5.6.3 | Type safety |
| `vitest` | ^4.1.10 | Testing |

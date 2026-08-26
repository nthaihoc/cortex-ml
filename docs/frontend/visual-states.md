---
title: Trạng thái hiển thị
description: Quy tắc màu sắc và icon cho Health, Freshness, TopologyNodeState.
---

# :material-palette: Trạng thái hiển thị

`TopologyViewer` sử dụng màu sắc và icon nhất quán để thể hiện trạng thái entity.

---

## :material-heart-pulse: `Health`

| Giá trị | Màu | Ý nghĩa |
|---|---|---|
| `healthy` | 🟢 Xanh lá | Entity hợp lệ, không có lỗi |
| `warning` | 🟡 Vàng | Có cảnh báo (VD: `REFERENCE_TARGET_NOT_FOUND`) |
| `error` | 🔴 Đỏ | Có lỗi blocking hoặc đang ở last-valid state |

## :material-clock-outline: `Freshness`

| Giá trị | Hiệu ứng | Ý nghĩa |
|---|---|---|
| `current` | Viền đặc | Dữ liệu phản ánh file hiện tại |
| `stale` | Viền nét đứt | Giữ last-valid state, file hiện tại bị lỗi |

## :material-state-machine: `TopologyNodeState`

| Trạng thái | Icon | Màu nền | Mô tả |
|---|---|---|---|
| `entity` | ■ | Theo `Health` | `CatalogEntity` đã resolve |
| `draft` | ◇ | Xám | `DraftEntity` — chưa bao giờ valid |
| `conflict` | ⚠ | Đỏ nhạt | `IdentityConflict` — duplicate reference |
| `unresolved` | ? | Xám nhạt | Relation target không tìm thấy |

---

## :material-relation-many-to-many: `RelationType` Edge Styles

| `RelationType` | Style | Label |
|---|---|---|
| `partOf` | Nét liền | "part of" |
| `dependsOn` | Nét liền, mũi tên | "depends on" |
| `providesApi` | Nét đứt | "provides" |
| `consumesApi` | Nét đứt, mũi tên | "consumes" |
| `publishesTo` | Nét chấm | "publishes to" |
| `consumesFrom` | Nét chấm, mũi tên | "consumes from" |
| `contains` | Nét liền mảnh | "contains" |

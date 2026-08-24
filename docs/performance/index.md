---
title: Performance
description: Performance characteristics and limits of the IDP Platform.
---

# :material-gauge: Performance

The IDP Platform is designed as a **local-first** developer tool. Because there is no network database and all data fits in memory, it is extremely fast.

---

<div class="grid cards" markdown>

-   :material-timer-outline:{ .lg .middle } **Benchmarks**

    Measured performance for loading, querying, and searching large catalogs.

    [:octicons-arrow-right-24: Benchmarks](benchmarks.md)

-   :material-chart-line-variant:{ .lg .middle } **Scalability Limits**

    How the system degrades at extreme scale and current limits.

    [:octicons-arrow-right-24: Scalability Limits](scalability.md)

</div>

---

## Why it's fast

1. **In-Memory Core:** The entire `CatalogWorkspace` state is kept in RAM. Retrieving the snapshot or a focused topology requires zero disk I/O.
2. **C Extensions:** The `watchfiles` library uses Rust, and `pyyaml` uses the libyaml C extension (when available) for maximum speed.
3. **Optimized Algorithms:** The topology graph computation uses a simple adjacency list BFS that runs in microseconds.
4. **Debouncing:** When you type in your editor, validation is debounced by 300 ms so we don't parse partial words.

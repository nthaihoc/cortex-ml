---
title: Diagnostics
description: How the IDP Platform reports errors and warnings.
---

# :material-stethoscope: Diagnostics

When the system encounters a problem in a `catalog-info.yaml` file, it produces a **Diagnostic**. Diagnostics are exactly like the squiggly line errors you see in your code editor.

Diagnostics are available via:
1. The **VS Code Extension** (shown directly in the editor)
2. The **HTTP API** (`/api/v1/catalog/diagnostics`)
3. The **Frontend Viewer** (shown as colored borders on nodes)

---

<div class="grid cards" markdown>

-   :material-format-list-numbered:{ .lg .middle } **Diagnostic Codes**

    The complete list of all 22 diagnostic codes and how to fix them.

    [:octicons-arrow-right-24: Codes Reference](codes.md)

-   :material-shield-alert:{ .lg .middle } **Severity Guide**

    The difference between an error and a warning, and what makes an error "blocking".

    [:octicons-arrow-right-24: Severity Guide](severity.md)

</div>

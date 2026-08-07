---
title: Testing
description: Testing strategy and test suites for the IDP Platform.
---

# :material-test-tube: Testing

The IDP Platform has comprehensive automated test coverage across all three components: Python backend, TypeScript frontend, and VS Code extension.

<div class="grid cards" markdown>

-   :material-language-python:{ .lg .middle } **Backend Tests**

    pytest-based tests for the core catalog engine.

    [:octicons-arrow-right-24: Backend Tests](backend.md)

-   :material-react:{ .lg .middle } **Frontend Tests**

    Vitest + Testing Library tests for the React viewer.

    [:octicons-arrow-right-24: Frontend Tests](frontend.md)

-   :material-microsoft-visual-studio-code:{ .lg .middle } **Extension Tests**

    Vitest tests for the VS Code extension and webview.

    [:octicons-arrow-right-24: Extension Tests](extension.md)

-   :material-check-decagram:{ .lg .middle } **Acceptance Coverage**

    Milestone 1 acceptance scenarios and their automated evidence.

    [:octicons-arrow-right-24: Acceptance Coverage](acceptance.md)

</div>

---

## :material-run: Running All Tests

=== "Backend"

    ```bash
    cd backend
    python -m pytest
    ```

=== "Frontend"

    ```bash
    cd frontend
    npm test
    npm run benchmark
    npm run build
    ```

=== "VS Code Extension"

    ```bash
    cd vscode-extension
    npm test
    npm run check
    npm run build
    ```

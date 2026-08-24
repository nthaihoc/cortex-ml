---
title: Scalability Limits
description: Known limits and edge cases at extreme scale.
---

# :material-chart-line-variant: Scalability Limits

The platform is optimized for local developer workspaces. While it can handle thousands of files effortlessly, there are hard limits designed to protect your machine's memory and CPU.

---

## Hard Limits

| Limit | Value | What happens if exceeded? |
|-------|-------|---------------------------|
| **Maximum File Size** | 1 MB | File is skipped. Generates a `CATALOG_DESCRIPTOR_TOO_LARGE` diagnostic. |
| **YAML Nesting Depth** | (Python recursion limit) | Fails with `YAML_SYNTAX_ERROR`. Normal descriptors are shallow, so this requires a malicious file. |
| **Topology Depth** | 1 | Hardcoded. The API only supports 1-hop focused topology. Requests for `depth=2` fail with HTTP 422. |

---

## Memory Consumption

The entire catalog is kept in RAM in Python.

- **Rule of thumb:** ~5 MB of RAM per 1,000 entities.
- A 10,000 entity catalog uses roughly 50-70 MB of RAM (negligible on modern hardware).
- However, the `GET /api/v1/catalog/snapshot` JSON payload can become quite large (~25 MB for 10,000 entities), which causes a temporary CPU/Memory spike during JSON serialization.

---

## Filesystem Watcher Limits

The `watchfiles` library relies on operating system events (fsevents on macOS, inotify on Linux).

**Linux `inotify` limit:**
If you have millions of files in your `CATALOG_ROOT` (for example, if you accidentally point it at your entire home directory or a massive `node_modules` folder), Linux may run out of inotify watchers.

**Symptoms:**
- The backend crashes on startup with an OS error about file watchers.
- Changes stop triggering updates.

**Fix:**
Point `CATALOG_ROOT` to a more specific directory, or increase the system limit:
```bash
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```
*(The backend tries to skip `node_modules` automatically, but highly nested custom folders can still hit this limit).*

---

## Team Size / Concurrent Users

The local catalog runtime binds to `127.0.0.1:8000` and uses the standard Uvicorn ASGI server. It is designed for **single-user local access only**.

It is **not** designed to be deployed to the cloud or shared across a team. If you want a shared portal for your whole company, use the main Backstage instance. This tool is strictly for your local VS Code environment.

---
title: Server-Sent Events
description: Real-time catalog change notification stream via SSE.
---

# :material-broadcast: Server-Sent Events

The `/api/v1/catalog/events` endpoint provides a **Server-Sent Events (SSE)** stream that pushes catalog revision change metadata to connected clients in real time.

---

## :material-connection: Connecting to the Stream

```javascript
const events = new EventSource('http://127.0.0.1:8000/api/v1/catalog/events');

events.onmessage = (event) => {
  const notification = JSON.parse(event.data);
  console.log('Catalog revision:', notification.revision);
  console.log('Changed:', notification.changed_source_uris);
  console.log('Removed:', notification.removed_source_uris);
};
```

---

## :material-code-json: `CatalogChangeEvent` Schema

Each SSE `data` frame contains a JSON object:

```json
{
  "revision": 43,
  "changed_source_uris": [
    "file:///path/to/my-service/catalog-info.yaml"
  ],
  "removed_source_uris": []
}
```

| Field | Type | Description |
|-------|------|-------------|
| `revision` | `integer` | The new catalog revision after this change |
| `changed_source_uris` | `array[uri]` | File URIs that were added or updated |
| `removed_source_uris` | `array[uri]` | File URIs that were deleted |

---

## :material-refresh: Recommended Client Pattern

On receiving any SSE event, clients should **refetch** the current catalog state. The event payload is **change metadata only** — not a semantic delta that can be applied to a previous snapshot.

```javascript
events.onmessage = async (event) => {
  const { revision } = JSON.parse(event.data);

  // Refetch the current focused topology or full snapshot
  const topology = await fetch(
    `/api/v1/catalog/topology?root=${currentRoot}`
  ).then(r => r.json());

  renderTopology(topology);
};
```

---

## :material-server-network: How the Stream Works

1. The `CatalogFileWatcher` detects a filesystem change
2. After 300 ms debounce, it calls `workspace.upsert_document()` or `remove_document()`
3. If the catalog revision changes, it calls `runtime.changes.publish(notification)`
4. `CatalogChangeFeed` delivers the notification to all active SSE subscribers
5. Each subscriber serializes the notification as a JSON `data` frame

The `CatalogChangeFeed` is a simple pub/sub backed by `asyncio.Queue` per subscriber, created and cleaned up per SSE connection.

---

## :material-alert-outline: Notes

!!! info "Cache-Control"
    The SSE response includes `Cache-Control: no-cache` to prevent intermediate caches from buffering the stream.

!!! warning "Connection lifecycle"
    When the browser tab is closed or the SSE connection drops, the server-side stream generator terminates automatically. Reconnect by creating a new `EventSource` instance.

---

## :material-link: Further Reading

- [MDN: Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- [WHATWG SSE Specification](https://html.spec.whatwg.org/multipage/server-sent-events.html)
- [FastAPI StreamingResponse](https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse)

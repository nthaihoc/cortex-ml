---
title: Server-Sent Events
description: Real-time catalog change notification stream via SSE.
---

# :material-broadcast: Server-Sent Events (SSE)

The IDP Platform provides a real-time event stream that notifies you when catalog files change on disk. This is how the browser viewer updates automatically when you save a file.

---

## Connecting to the Stream

Connect to the `/api/v1/catalog/events` endpoint. The server will keep the connection open and stream events using the `text/event-stream` format.

**Example Request:**

```
GET /api/v1/catalog/events HTTP/1.1
Accept: text/event-stream
```

---

## Event Format

Every time a file is added, modified, or deleted, the server sends a JSON payload in the `data` field of an event.

```
data: {"revision":43,"changed_source_uris":["file:///path/to/catalog-info.yaml"],"removed_source_uris":[]}

data: {"revision":44,"changed_source_uris":[],"removed_source_uris":["file:///old/catalog-info.yaml"]}
```

| Field | Type | Description |
|-------|------|-------------|
| `revision` | `integer` | The new catalog revision number (increases monotonically) |
| `changed_source_uris` | `array` of strings | `file://` URIs of files that were added or updated |
| `removed_source_uris` | `array` of strings | `file://` URIs of files that were deleted |

---

## How to Use the Stream

The event payload **only contains metadata**, not the actual entity data. This is an intentional design choice to keep the stream lightweight.

When your client receives an event, it should **refetch** the data it needs using the new `revision` number to ensure it has the latest state.

### Example Workflow

1. Client connects to `/api/v1/catalog/events`
2. Client fetches the initial state: `GET /api/v1/catalog/topology?root=...`
3. User saves a `catalog-info.yaml` file
4. Server sends SSE event: `{"revision": 45, ...}`
5. Client receives the event
6. Client fetches the updated state: `GET /api/v1/catalog/topology?root=...`

---

## Browser Example (JavaScript)

```javascript
const eventSource = new EventSource("http://127.0.0.1:8000/api/v1/catalog/events");

eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log(`Catalog updated to revision ${data.revision}`);
    
    // The data changed, so fetch the new topology
    fetchTopology();
};

eventSource.onerror = (error) => {
    console.error("Lost connection to SSE stream. Reconnecting...", error);
    // EventSource automatically tries to reconnect
};
```

---

## Further Reading

- [API Endpoints Reference](endpoints.md)
- [File Watcher](../backend/file-watcher.md) — How the backend detects file changes

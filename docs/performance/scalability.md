---
title: Khả năng mở rộng
description: Scalability của in-memory catalog.
---

# :material-arrow-expand-all: Khả năng mở rộng (Scalability)

`CatalogWorkspace` được thiết kế dưới dạng In-memory Object Graph. Nó loại bỏ độ trễ database để bù lại bằng việc tiêu thụ RAM. 

## Tính toán bộ nhớ

Mỗi `CatalogEntity` cùng với descriptor object và relations chiếm khoảng **25 KB - 30 KB** RAM trong CPython (tùy thuộc vào số lượng field).

Với các tổ chức lớn (Enterprise level):
- **10,000 dịch vụ/tài nguyên** -> Tiêu tốn khoảng **250 - 300 MB** RAM. 
- Mức RAM này là cực kỳ nhẹ cho bất kỳ máy tính dev (developer laptop) nào hiện nay.

## Điểm giới hạn (Bottleneck)

Thiết kế hiện tại có một số giới hạn (by design):

1. **Khóa GIL (Global Interpreter Lock):** Python giới hạn xử lý CPU trên một thread duy nhất. Khi initial scan (lúc bật máy), toàn bộ tiến trình quét 10,000 file bị serialize.
2. **JSON Serialization:** Backend trả về topology JSON graph cho frontend. Nếu một node có quá nhiều cạnh (ví dụ: Core API Gateway có 500 downstream connections), JSON payload sẽ phình to. 
3. **Frontend ReactFlow:** Browser vẽ > 500 node trên ReactFlow sẽ bắt đầu giật lag (frame drop). Đó là lý do API luôn enforce `depth=1` để graph tập trung và nhỏ.

## Chiến lược tương lai

Nếu hệ thống vượt qua 50,000 entities, `catalog_http` có thể thay đổi chiến lược sang:
- Cache `FocusedTopology` payload (memcached).
- Pagination cho các relation vượt quá 100 edges.
- Chuyển `HardenedYamlParser` sang một extension Rust/C.

# Hướng dẫn vẽ biểu đồ Mermaid cơ bản

Dưới đây là một khối Mermaid kết hợp giữa việc tạo **Node nhiều màu sắc** và nhóm chúng lại bằng **Subgraph** (Thư mục/Nhóm logic):

```mermaid
graph TD
    %% Tùy chỉnh Subgraph: Nhóm các thành phần liên quan
    subgraph Frontend [Khối Giao diện]
        Node1[Bắt đầu]
        Node2(Xử lý giao diện)
    end
    
    subgraph Backend [Khối Xử lý Lõi]
        Node3{Kiểm tra dữ liệu}
        Node4[(Lưu trữ Database)]
    end

    %% Liên kết giữa các node (kể cả xuyên qua subgraph)
    Node1 --> Node2
    Node2 -->|Gửi yêu cầu| Node3
    Node3 -->|Hợp lệ| Node4
    Node3 -->|Không hợp lệ| Node1

    %% Tùy chỉnh màu sắc (style) cho từng node
    %% fill: Màu nền, stroke: Màu viền, color: Màu chữ
    style Node1 fill:#ff9999,stroke:#333,stroke-width:2px,color:#000
    style Node2 fill:#99ccff,stroke:#0055cc,stroke-width:2px,color:#000
    style Node3 fill:#99ff99,stroke:#339933,stroke-width:4px,color:#000
    style Node4 fill:#ffd966,stroke:#b45f06,stroke-width:2px,color:#000

    %% Tùy chỉnh màu cho Subgraph (tùy chọn)
    style Frontend fill:#f3f3f3,stroke:#666,stroke-width:2px,stroke-dasharray: 5 5
    style Backend fill:#eef2f5,stroke:#333,stroke-width:2px
```

### Giải thích cú pháp Subgraph:
1. `subgraph Tên_ID [Tiêu đề hiển thị]`: Khởi tạo một cụm chức năng (khối).
2. Viết các Node bên trong `subgraph` ... `end` để gộp chúng lại với nhau trong một hộp chứa (box).
3. Bạn có thể kéo mũi tên từ một Node trong Subgraph này sang một Node ở Subgraph khác hoàn toàn bình thường (như `Node2 --> Node3`).
4. Bạn cũng có thể dùng `style Tên_ID_Subgraph` để đổi màu nền và viền cho chính cái hộp chứa đó (như tôi đã thêm nét đứt `stroke-dasharray` cho khối Frontend).

---
title: Cài đặt
description: Hướng dẫn đóng gói và cài đặt VS Code Extension.
---

# :material-download: Cài đặt

## Cài đặt từ mã nguồn (Development)

Để phát triển hoặc thử nghiệm extension trực tiếp:

1. Mở thư mục `idp-platform` trong VS Code.
2. Mở terminal, đi tới thư mục extension:
    ```bash
    cd vscode-extension
    npm install
    ```
3. Mở Run and Debug panel (`Ctrl+Shift+D` / `Cmd+Shift+D`).
4. Chọn **"Run Extension"** và nhấn F5. Một cửa sổ VS Code mới (Extension Development Host) sẽ mở ra với extension đã được nạp.

---

## Đóng gói VSIX để cài đặt thủ công

Để cài đặt extension vào bản VS Code thông thường của bạn (hoặc chia sẻ cho người khác):

1. Đi tới thư mục extension:
    ```bash
    cd idp-platform/vscode-extension
    npm install
    ```
2. Cài đặt `vsce` (công cụ đóng gói của VS Code) nếu chưa có:
    ```bash
    npm install -g @vscode/vsce
    ```
3. Đóng gói:
    ```bash
    vsce package --no-dependencies
    ```
   Lệnh này sẽ tạo ra một file `.vsix` (ví dụ: `local-catalog-topology-vscode-0.1.0.vsix`).

4. Cài đặt file VSIX:
    - Qua giao diện: Vào mục Extensions (`Ctrl+Shift+X`), click vào icon "..." góc trên phải, chọn "Install from VSIX..." và trỏ tới file vừa tạo.
    - Qua command line:
      ```bash
      code --install-extension local-catalog-topology-vscode-0.1.0.vsix
      ```

!!! note "Backend requirements"
    Extension này khởi chạy một process Python chạy `CatalogLanguageServer`. Do đó, Python 3.12+ và các dependencies trong `backend/requirements.txt` phải có sẵn trong môi trường của bạn (hoặc cấu hình qua biến môi trường của extension).

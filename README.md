🤖 Hệ thống 2 Robot Master – Slave tìm đường trong Webots
📌 Giới thiệu
Dự án mô phỏng hệ thống gồm 2 robot: Master và Slave hoạt động trên môi trường Webots.
Robot Master đứng cố định tại góc bản đồ, có nhiệm vụ:
Nhận vị trí hiện tại của Slave
Tính đường đi ngắn nhất bằng thuật toán Dijkstra
Gửi danh sách waypoint cho Slave
Robot Slave:
Xác định vị trí bằng GPS
Gửi vị trí về Master
Nhận đường đi và di chuyển theo các điểm được gửi
🗺️ Môi trường mô phỏng
Sử dụng RectangleArena
Kích thước sàn: 6.5 x 6.5 m
Kích thước ô: 0.5 x 0.5 m
Bản đồ được chia thành: 12 x 12 ô
Ngoài ra môi trường có thêm vật thể trang trí (cây, đá, động vật) không ảnh hưởng đến thuật toán (chỉ grid quyết định đường đi)
🔲 Bản đồ (Grid)
Grid kích thước: 12 x 12
Giá trị:
0 → đi được
1 → vật cản
Đích đến: (11, 11)
🔄 Cách hoạt động
Slave gửi vị trí hiện tại (grid) cho Master
Master nhận vị trí và chạy Dijkstra
Master gửi đường đi dạng danh sách waypoint
Slave nhận và di chuyển từng bước đến đích
⚙️ Thành phần hệ thống
Master
Receiver (nhận vị trí)
Emitter (gửi đường đi)
Thuật toán Dijkstra
Slave
GPS → lấy vị trí
Compass → xác định hướng
Receiver → nhận đường đi
Emitter → gửi vị trí
2 motor → điều khiển di chuyển
🚀 Kết quả
Master tính được đường đi hợp lệ tránh vật cản
Slave nhận đúng dữ liệu và di chuyển theo lộ trình
Robot đến đúng đích (11, 11)
🎯 Mục tiêu đạt được
Mô phỏng mô hình Master – Slave
Ứng dụng thuật toán tìm đường trên grid
Điều khiển robot di chuyển trong môi trường Webots
👨‍💻 Nhóm thực hiện
Phạm Ngọc Kỳ Sơn
Tạ Minh Quân
Chu Hữu Tươi
Vũ Anh Tú

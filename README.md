🤖 Hệ thống Robot Master – Slave tìm đường trong Webots

📌 Giới thiệu

Dự án mô phỏng hệ thống gồm 2 robot hoạt động theo mô hình Master – Slave trong môi trường Webots.

Robot Master đứng yên tại một vị trí trên bản đồ, có nhiệm vụ nhận dữ liệu và tính toán đường đi.

Robot Slave di chuyển trong môi trường, gửi vị trí hiện tại và thực hiện di chuyển theo lộ trình do Master cung cấp.

🗺️ Môi trường mô phỏng

Sử dụng RectangleArena trong Webots

Kích thước sàn: khoảng 6.5 x 6.5 m

Bản đồ được chia thành lưới 12 x 12 ô

Mỗi ô có kích thước 0.5 x 0.5 m

Bản đồ được biểu diễn bằng ma trận (grid), trong đó:

0: ô có thể đi qua
1: ô chứa vật cản

🔄 Nguyên lý hoạt động

Hệ thống hoạt động theo các bước:

Slave xác định vị trí bằng GPS và chuyển sang tọa độ grid

Slave gửi vị trí hiện tại cho Master

Master nhận dữ liệu, sử dụng thuật toán Dijkstra để tìm đường đến đích

Master gửi lộ trình (danh sách các ô) cho Slave

Slave di chuyển lần lượt theo các điểm trong lộ trình đến đích

⚙️ Thành phần hệ thống

🔹 Robot Master

Receiver: nhận vị trí từ Slave

Emitter: gửi đường đi

Thuật toán Dijkstra để tìm đường

🔹 Robot Slave

GPS: xác định vị trí

Compass: xác định hướng di chuyển

Emitter: gửi vị trí


Receiver: nhận lộ trình

2 động cơ: điều khiển di chuyển

🎯 Kết quả

Hệ thống xác định được vị trí của Slave trên bản đồ

Master tìm được đường đi hợp lệ tránh vật cản

Slave di chuyển theo lộ trình và đến đúng vị trí đích

🚀 Kết luận

Dự án giúp hiểu rõ: cách xây dựng bản đồ dạng lưới, cách áp dụng thuật toán tìm đường, cách giao tiếp giữa các robot, cách điều khiển robot trong môi trường mô phỏng

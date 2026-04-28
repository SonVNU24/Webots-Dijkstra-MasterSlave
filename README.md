# Hệ thống 2 Robot Master - Slave vận chuyển phân bón trên Webots

## 1. Giới thiệu

Đây là bài tập lớn môn **Robotics và Drone**, mô phỏng hệ thống hai robot hoạt động theo mô hình **Master - Slave** trong môi trường Webots.

Kịch bản mô phỏng gồm:

- **Robot 1 - Master**: đứng cố định tại góc bản đồ, không trực tiếp di chuyển.
- **Robot 2 - Slave**: robot thực hiện nhiệm vụ di chuyển đến vị trí cần bón phân.
- Master nhận vị trí hiện tại của Slave, chạy thuật toán **Dijkstra** để tìm đường đi ngắn nhất đến đích.
- Sau khi tính toán xong, Master gửi danh sách tọa độ đường đi, tức các **waypoints**, qua sóng radio cho Slave.
- Slave nhận mảng tọa độ và di chuyển lần lượt qua các điểm đó.

Mục tiêu của hệ thống là mô phỏng một mô hình robot nông nghiệp đơn giản, trong đó một robot trung tâm chịu trách nhiệm tính toán lộ trình, còn robot còn lại chỉ thực thi nhiệm vụ di chuyển.

## 2. Công nghệ sử dụng

- Webots
- Python Controller
- Emitter / Receiver
- GPS
- Compass
- Differential Wheel Motor
- Thuật toán Dijkstra
- Mô hình điều khiển Master - Slave

## 3. Cấu trúc hệ thống

```text
Master Robot
│
├── Nhận vị trí hiện tại của Slave
├── Chạy thuật toán Dijkstra
├── Tạo danh sách waypoint
└── Gửi waypoint qua Emitter

Slave Robot
│
├── Gửi vị trí hiện tại cho Master
├── Nhận waypoint qua Receiver
├── Chuyển tọa độ grid sang tọa độ Webots
└── Di chuyển lần lượt qua các checkpoint

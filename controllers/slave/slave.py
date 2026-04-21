from controller import Robot
import math

robot = Robot()
TIME_STEP = int(robot.getBasicTimeStep())

# --- 1. Khởi tạo thiết bị (Giữ nguyên của bạn) ---
emitter = robot.getDevice('emitter')
receiver = robot.getDevice('receiver')
receiver.enable(TIME_STEP)
gps = robot.getDevice('gps'); gps.enable(TIME_STEP)

# Kiểm tra Compass để tránh lỗi AttributeError
compass = robot.getDevice('compass')
if compass:
    compass.enable(TIME_STEP)
else:
    print("LỖI: Bạn chưa thêm thiết bị Compass vào Robot Slave trong Webots!")

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# --- 2. Cấu hình thông số ---
GRID_COUNT, CELL_SIZE, MAP_ORIGIN = 12, 0.25, -1.5
MAX_SPEED = 10.0  # Giới hạn vật lý của Webots

def world_to_grid(wx, wy):
    return int((wx - MAP_ORIGIN) / CELL_SIZE), int((wy - MAP_ORIGIN) / CELL_SIZE)

def grid_to_world(col, row):
    return (col * CELL_SIZE + MAP_ORIGIN + CELL_SIZE/2, 
            row * CELL_SIZE + MAP_ORIGIN + CELL_SIZE/2)

# Hệ trạng thái
STATE_IDLE, STATE_WAITING, STATE_MOVING = 0, 1, 2
current_state = STATE_IDLE
path_to_follow = []

print("--- SLAVE: Đang đứng yên ---")

while robot.step(TIME_STEP) != -1:
    pos = gps.getValues()
    
    if current_state == STATE_IDLE:
        c, r = world_to_grid(pos[0], pos[1])
        emitter.send(f"{c},{r}".encode('utf-8'))
        current_state = STATE_WAITING
        print(f"Slave: Đang ở ô ({c},{r}). Đã gửi yêu cầu đường đi...")

    elif current_state == STATE_WAITING:
        if receiver.getQueueLength() > 0:
            msg = receiver.getString()
            path_to_follow = [tuple(map(int, p.split(','))) for p in msg.split('|')]
            print(f"Slave: QUÃNG ĐƯỜNG SẮP CHẠY: {path_to_follow}")
            current_state = STATE_MOVING
            receiver.nextPacket()

    elif current_state == STATE_MOVING:
        if not path_to_follow:
            left_motor.setVelocity(0); right_motor.setVelocity(0)
            print("Slave: Đã đến đích (11,11). Dừng lại.")
            current_state = -1 
            continue

        target_grid = path_to_follow[0]
        tx, ty = grid_to_world(target_grid[0], target_grid[1])
        
        dx, dy = tx - pos[0], ty - pos[1]
        dist = math.sqrt(dx**2 + dy**2)
        
        if dist < 0.05:
            print(f"Slave: Checkpoint thành công ô {target_grid}")
            path_to_follow.pop(0)
        else:
            if not compass:
                continue # Không có la bàn thì không điều khiển hướng được

            # Điều khiển hướng
            bearing = math.atan2(dy, dx)
            com = compass.getValues()
            rad = math.atan2(com[0], com[1])
            
            angle_diff = bearing - rad
            while angle_diff > math.pi: angle_diff -= 2*math.pi
            while angle_diff < -math.pi: angle_diff += 2*math.pi
            
            # --- PHẦN SỬA LỖI WARNING VẬN TỐC ---
            base_speed = 4.0
            turn_speed = angle_diff * 5.0
            
            v_left = base_speed - turn_speed
            v_right = base_speed + turn_speed
            
            # Giới hạn vận tốc trong khoảng [-10, 10]
            v_left = max(-MAX_SPEED, min(MAX_SPEED, v_left))
            v_right = max(-MAX_SPEED, min(MAX_SPEED, v_right))
            
            left_motor.setVelocity(v_left)
            right_motor.setVelocity(v_right)
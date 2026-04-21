from controller import Robot

TIME_STEP = 64
MAX_SPEED = 6.28

robot = Robot()
timestep = int(robot.getBasicTimeStep())

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

gs = []
gsNames = ['gs0', 'gs1', 'gs2']
for i in range(3):
    sensor = robot.getDevice(gsNames[i])
    sensor.enable(timestep)
    gs.append(sensor)

# --- KHỞI TẠO BIẾN TRẠNG THÁI (FSM) ---
states = ['forward', 'turn_right', 'turn_left']
current_state = states[0]
counter = 0
COUNTER_MAX = 5

while robot.step(timestep) != -1:
    # 1. SEE (Doc cam bien)
    val_right = gs[0].getValue()
    val_left = gs[2].getValue()
    
    line_right = val_right > 600
    line_left = val_left > 600

    # 2. THINK (Logic may trang thai FSM)
    if current_state == 'forward':
        # TODO 1: Neu thay line ben phai -> chuyen current_state sang 'turn_right', reset counter ve 0
        if line_right:
            current_state = 'turn_right'
            counter = 0
        elif line_left:
            current_state = 'turn_left'
            counter = 0
        # TODO 2: Neu thay line ben trai -> chuyen current_state sang 'turn_left', reset counter ve 0
        pass
        
    elif current_state == 'turn_right':
        # TODO 3: Kiem tra neu counter == COUNTER_MAX thi chuyen current_state ve lai 'forward'
        if counter == COUNTER_MAX:
            current_state = 'forward'
        pass
    elif current_state == 'turn_left':
        # TODO 4: Kiem tra neu counter == COUNTER_MAX thi chuyen current_state ve lai 'forward'
        if counter == COUNTER_MAX:
            current_state = 'forward'
        pass

    # 3. ACT (Thuc thi hanh dong)
    if current_state == 'forward':
        leftSpeed = MAX_SPEED
        rightSpeed = MAX_SPEED
    elif current_state == 'turn_right':
        leftSpeed = 0.8 * MAX_SPEED
        rightSpeed = 0.4 * MAX_SPEED
    elif current_state == 'turn_left':
        leftSpeed = 0.4 * MAX_SPEED
        rightSpeed = 0.8 * MAX_SPEED

    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
    
    # Tang bo dem
    if current_state != 'forward':
        counter += 1
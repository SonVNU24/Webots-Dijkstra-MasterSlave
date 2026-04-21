from controller import Robot
import heapq

robot = Robot()
TIME_STEP = int(robot.getBasicTimeStep())

receiver = robot.getDevice('receiver')
receiver.enable(TIME_STEP)
emitter = robot.getDevice('emitter')

TARGET = (11, 11) # Đích đến
GRID_SIZE = 12
grid = [
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0], # Row 0
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], # Row 1
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], # Row 2
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], # Row 3
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], # Row 4
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], # Row 5
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0], # Row 6
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0], # Row 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # Row 8
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], # Row 9
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1], # Row 10
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]  # Row 11
]
def dijkstra(start, goal):
    queue = [(0, start, [])]
    seen = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in seen:
            path = path + [node]
            if node == goal: return path
            seen.add(node)
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]: # Di chuyển 4 hướng
                nx, ny = node[0] + dx, node[1] + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[ny][nx] == 0:
                    heapq.heappush(queue, (cost + 1, (nx, ny), path))
    return None

print("--- MASTER: Đang trực tuyến ---")

while robot.step(TIME_STEP) != -1:
    if receiver.getQueueLength() > 0:
        data = receiver.getString()
        start_node = tuple(map(int, data.split(',')))
        print(f"Master: Nhận vị trí Slave {start_node}. Đang tính đường đến {TARGET}...")
        
        path = dijkstra(start_node, TARGET)
        if path:
            path_str = "|".join([f"{c},{r}" for c, r in path])
            emitter.send(path_str.encode('utf-8'))
            print(f"Master: Lộ trình tìm được: {path}")
        else:
            print("Master: Không tìm thấy đường!")
        receiver.nextPacket()
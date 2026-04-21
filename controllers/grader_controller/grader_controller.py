from controller import Supervisor
import math
import sys

supervisor = Supervisor()
timestep = int(supervisor.getBasicTimeStep())
print("[GRADER] Start grading Lab 3 (Local FSM)...")

student_robot = supervisor.getFromDef("EPUCK_STUDENT")
target_node = supervisor.getFromDef("TARGET_ZONE")

if student_robot is None:
    print("[GRADER ERROR] Khong tim thay robot co DEF la 'EPUCK_STUDENT'.")
    print("[RESULT] FAILED_MISSING_ROBOT")
    supervisor.simulationQuit(1)
    sys.exit(1)

TARGET_X = 1.0
TARGET_Z = 0.5
if target_node:
    target_pos = target_node.getPosition()
    TARGET_X = target_pos[0]
    TARGET_Z = target_pos[2]

MAX_TIME = 60.0

while supervisor.step(timestep) != -1:
    try:
        current_time = supervisor.getTime()
        current_position = student_robot.getPosition()
        distance = math.sqrt(
            (current_position[0] - TARGET_X)**2 + (current_position[2] - TARGET_Z)**2)

        if distance < 0.1:
            print(f"[GRADER] Target reached in {current_time:.2f}s. Pass.")
            print("[RESULT] SUCCESS_LAB3_PASS")
            supervisor.simulationSetMode(supervisor.SIMULATION_MODE_PAUSE)
            break

        if current_time > MAX_TIME:
            print(
                f"[GRADER] Timeout ({MAX_TIME}s). Robot failed to follow the line.")
            print("[RESULT] FAILED_TIMEOUT")
            supervisor.simulationSetMode(supervisor.SIMULATION_MODE_PAUSE)
            break
    except Exception as e:
        print(f"[GRADER EXCEPTION] Lỗi: {e}")
        print("[RESULT] FAILED_GRADER_CRASH")
        supervisor.simulationSetMode(supervisor.SIMULATION_MODE_PAUSE)
        break

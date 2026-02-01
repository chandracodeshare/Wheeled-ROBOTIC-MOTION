"""
===========================================================
        STEP 4: EXECUTE ROBOT MOTION
===========================================================
Differential drive control:
- Straight motion
- Circular motion
- Custom trajectories
"""

import pybullet as p
import pybullet_data
import time
import os
import math

# -------------------------------
# 1. Initialize Simulation
# -------------------------------
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

plane_id = p.loadURDF("plane.urdf")
urdf_path = os.path.join(os.getcwd(), "wheeled_robot.urdf")
robot_id = p.loadURDF(urdf_path, [0, 0, 0.2])

# -------------------------------
# 2. Joint Index Mapping
# -------------------------------
LEFT_WHEEL = 0
RIGHT_WHEEL = 1
CASTER = 2

# Disable default motors
p.setJointMotorControl2(robot_id, LEFT_WHEEL,
                        p.VELOCITY_CONTROL, force=0)
p.setJointMotorControl2(robot_id, RIGHT_WHEEL,
                        p.VELOCITY_CONTROL, force=0)

# -------------------------------
# Utility function
# -------------------------------
def set_wheel_velocity(v_left, v_right):
    p.setJointMotorControl2(robot_id, LEFT_WHEEL,
                            p.VELOCITY_CONTROL,
                            targetVelocity=v_left,
                            force=5)

    p.setJointMotorControl2(robot_id, RIGHT_WHEEL,
                            p.VELOCITY_CONTROL,
                            targetVelocity=v_right,
                            force=5)

# -------------------------------
# a. Straight Line Motion
# -------------------------------
print("Straight line motion...")
for _ in range(240 * 3):  # 3 seconds
    set_wheel_velocity(10, 10)
    p.stepSimulation()
    time.sleep(1/240)

# Stop
set_wheel_velocity(0, 0)
time.sleep(1)

# -------------------------------
# b. Circular Motion
# -------------------------------
print("Circular motion...")
for _ in range(240 * 4):  # 4 seconds
    set_wheel_velocity(5, 10)  # different speeds
    p.stepSimulation()
    time.sleep(1/240)

# Stop
set_wheel_velocity(0, 0)
time.sleep(1)

# -------------------------------
# c1. Square Trajectory
# -------------------------------
print("Square trajectory...")
for i in range(4):
    # Move straight
    for _ in range(240 * 2):
        set_wheel_velocity(10, 10)
        p.stepSimulation()
        time.sleep(1/240)

    # Turn 90 degrees
    for _ in range(240):
        set_wheel_velocity(-5, 5)
        p.stepSimulation()
        time.sleep(1/240)

# Stop
set_wheel_velocity(0, 0)
time.sleep(1)

# -------------------------------
# c2. Zig-Zag Trajectory
# -------------------------------
print("Zig-zag trajectory...")
for i in range(6):
    for _ in range(240):
        set_wheel_velocity(8, 12)
        p.stepSimulation()
        time.sleep(1/240)
    for _ in range(240):
        set_wheel_velocity(12, 8)
        p.stepSimulation()
        time.sleep(1/240)

# Stop
set_wheel_velocity(0, 0)
time.sleep(1)

# -------------------------------
# c3. Figure-Eight Trajectory
# -------------------------------
print("Figure-eight trajectory...")
for t in range(240 * 6):
    v_left = 8 * math.sin(0.02 * t) + 10
    v_right = 8 * math.sin(0.02 * t + math.pi) + 10
    set_wheel_velocity(v_left, v_right)
    p.stepSimulation()
    time.sleep(1/240)

print("All trajectories executed.")
while True:
    p.stepSimulation()
    time.sleep(1/240)

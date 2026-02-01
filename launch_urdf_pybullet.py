import pybullet as p
import pybullet_data
import time
import os

# -------------------------------
# 1. Connect to PyBullet (GUI)
# -------------------------------
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# -------------------------------
# 2. Load Ground Plane
# -------------------------------
plane_id = p.loadURDF("plane.urdf")

# -------------------------------
# 3. Load Robot URDF
# -------------------------------
# Path to your URDF file
urdf_path = os.path.join(os.getcwd(), "wheeled_robot.urdf")

# Initial position (slightly above ground)
start_pos = [0, 0, 0.2]
start_ori = p.getQuaternionFromEuler([0, 0, 0])

robot_id = p.loadURDF(
    urdf_path,
    start_pos,
    start_ori,
    useFixedBase=False
)

print("Robot successfully loaded!")
print("Robot ID:", robot_id)

# -------------------------------
# 4. Simulation Loop
# -------------------------------
while True:
    p.stepSimulation()
    time.sleep(1.0 / 240.0)

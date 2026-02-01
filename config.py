"""
===========================================================
        STEP 3: CONFIGURE ROBOT PROPERTIES
===========================================================
This script configures gravity, friction,
and damping for realistic robot behavior.
"""

import pybullet as p
import pybullet_data
import time
import os

# -------------------------------
# 1. Connect to PyBullet
# -------------------------------
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# a. Set gravity
p.setGravity(0, 0, -9.81)

# -------------------------------
# 2. Load Ground and Robot
# -------------------------------
plane_id = p.loadURDF("plane.urdf")

urdf_path = os.path.join(os.getcwd(), "wheeled_robot.urdf")
robot_id = p.loadURDF(urdf_path, [0, 0, 0.2])

# -------------------------------
# 3. Identify Joints
# -------------------------------
num_joints = p.getNumJoints(robot_id)
print("Number of joints:", num_joints)

for i in range(num_joints):
    print("Joint", i, ":", p.getJointInfo(robot_id, i)[1])

# Convention (from URDF):
# Joint 0 -> left_wheel_joint
# Joint 1 -> right_wheel_joint
# Joint 2 -> caster_joint

LEFT_WHEEL = 0
RIGHT_WHEEL = 1
CASTER = 2

# -------------------------------
# 4. Configure Friction
# -------------------------------

# b. High friction for drive wheels
p.changeDynamics(robot_id, LEFT_WHEEL, lateralFriction=1.0)
p.changeDynamics(robot_id, RIGHT_WHEEL, lateralFriction=1.0)

# c. Low friction for caster wheel
p.changeDynamics(robot_id, CASTER, lateralFriction=0.05)

# e. Medium friction for base link
p.changeDynamics(robot_id, -1, lateralFriction=0.6)

# -------------------------------
# 5. Apply Damping
# -------------------------------

# d. Linear and angular damping
p.changeDynamics(robot_id, LEFT_WHEEL,
                 linearDamping=0.04,
                 angularDamping=0.04)

p.changeDynamics(robot_id, RIGHT_WHEEL,
                 linearDamping=0.04,
                 angularDamping=0.04)

# Optional: base damping
p.changeDynamics(robot_id, -1,
                 linearDamping=0.02,
                 angularDamping=0.02)

print("Robot dynamics configured successfully!")

# -------------------------------
# 6. Simulation Loop
# -------------------------------
while True:
    p.stepSimulation()
    time.sleep(1/240)

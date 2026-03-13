#!/usr/bin/env python3

import sys
import math
import rospy
import moveit_commander
import time

rospy.init_node("joint_move_test", anonymous=True)
moveit_commander.roscpp_initialize(sys.argv)

group = moveit_commander.MoveGroupCommander("arm")

#print()


def deg_to_rad_list(deg_list):
    return [math.radians(a) for a in deg_list]

# ---- Define START pose (degrees) ----
start_pose_deg = [4, 46, 12, -7, 35, 6]
#-19, 40, 60, 135, 27, -138
# ---- Define END pose (degrees) ----

end_pose_deg = [4, 46, 100, -7, 35, 6]

another_pose = [0, 0, 0, 0, 0, 0]
# Convert to radians
start_pose = deg_to_rad_list(start_pose_deg)
end_pose = deg_to_rad_list(end_pose_deg)

print("Point 1")
group.go(start_pose, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()


time.sleep(2)

print("Moving to END pose...")
group.go(end_pose, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()

time.sleep(2)

print("Going to third pose")
group.go(another_pose, wait = True)
pose = group.get_current_pose().pose
print(pose)
group.stop()



print("Motion complete.")

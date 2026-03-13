#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
from geometry_msgs.msg import Pose

rospy.init_node("cartesian_three_points")
moveit_commander.roscpp_initialize(sys.argv)

group = moveit_commander.MoveGroupCommander("arm")

waypoints = []

# Starting pose
#start_pose = group.get_current_pose().pose
#waypoints.append(start_pose)

x = 0.2
y = 0.2
z = 0.12 
delta = 0.05


# Point 1
pose1 = Pose()
pose1.position.x = x + delta
pose1.position.y = y - delta
pose1.position.z = z
pose1.orientation.w = 1.0
waypoints.append(pose1)

# Point 2
pose2 = Pose()
pose2.position.x = x
pose2.position.y = y - delta
pose2.position.z = z
pose2.orientation.w = 1.0
waypoints.append(pose2)

# Point 3
pose3 = Pose()
pose3.position.x = x - delta
pose3.position.y = y - delta
pose3.position.z = z
pose3.orientation.w = 1.0
waypoints.append(pose3)

# Point 4
pose4 = Pose()
pose4.position.x = x -delta
pose4.position.y = y
pose4.position.z = z
pose4.orientation.w = 1.0
waypoints.append(pose4)

# Point 5
pose5 = Pose()
pose5.position.x = x
pose5.position.y = y
pose5.position.z = z
pose5.orientation.w = 1.0
waypoints.append(pose5)

# Point 6
pose6 = Pose()
pose6.position.x = x + delta
pose6.position.y = y
pose6.position.z = z
pose6.orientation.w = 1.0
waypoints.append(pose6)

# Point 7
pose7 = Pose()
pose7.position.x = x + delta
pose7.position.y = y + delta
pose7.position.z = z
pose7.orientation.w = 1.0
waypoints.append(pose7)

# Point 8
pose8 = Pose()
pose8.position.x = x
pose8.position.y = y + delta
pose8.position.z = z
pose8.orientation.w = 1.0
waypoints.append(pose8)

# Point 9
pose9 = Pose()
pose9.position.x = x -delta
pose9.position.y = y + delta
pose9.position.z = z
pose9.orientation.w = 1.0
waypoints.append(pose9)

(plan, fraction) = group.compute_cartesian_path(
    waypoints,
    0.01,   # eef_step (resolution)
    True     # jump_threshold
)

print("Path fraction:", fraction)
group.execute(plan, wait=True)
group.stop()
group.clear_pose_targets()

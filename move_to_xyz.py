#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
from geometry_msgs.msg import Pose

rospy.init_node("move_to_xyz")

moveit_commander.roscpp_initialize(sys.argv)

group = moveit_commander.MoveGroupCommander("arm")  # check your group name

pose_target = Pose()
pose_target.position.x = 0.0
pose_target.position.y = 0.0
pose_target.position.z = 0.0

pose_target.orientation.w = 1.0  # simple neutral orientation

group.set_position_target([0.0, 0.0, 0.0])

plan = group.plan()

group.execute(plan[1], wait=True)

group.stop()
group.clear_pose_targets()

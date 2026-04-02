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
pose1 = [8.540842728689318e-06, 4.2816774547100073e-05, 7.374867866747081e-05,-5.396548612043262e-05, -3.339435439556838e-06,2.40082950796932e-05]
pose2 = [0.4059559630600211, 0.15936500569557888,-0.2932024688474439, -0.7767875203810728,0.5984212683206187, 0.2052249387260856]
pose3 = [0.7138221502786648 ,0.6153859951334111 ,-0.1717652049955217 ,-0.8853105761275242 ,1.0080278307242763, -0.3756290729073188]
pose4 = [ 0.9170507917582955 ,1.1857286848514048, 0.37735804702496534,-1.064857521271468, 1.1373039381148304, -0.7818545831540504]
pose5 = [0.7694527351449449, 1.1144534100874675, -0.006634948328747626, -0.8217795085576212, 1.2532430080941201, -1.2468028316370403]
pose6 = [0.8417469009428765, 0.9639793386557, -0.5620476371254508, -0.8422449402418639, 1.5409781670092424, -1.5374008979162717]
pose7 = [1.1041662169057256, 1.1333171957097652, 0.043153682367323046, -1.1507218719623968, 1.3612692844159369, -1.1349910335412003]
pose8 = [1.3670531717102792, 1.1162261152082393, -0.004790538841064279, -1.3868387191586322, 1.4827131813206207, -1.129150243875765]
pose9 = [1.1965704925853953, 0.9577467125036307, -0.7685343880253912, -1.2006815017485268, 1.6274354660044117, -1.7156791891106153]
#-19, 40, 60, 135, 27, -138
# ---- Define END pose (degrees) ----

#end_pose_deg = [4, 46, 100, -7, 35, 6]

#another_pose = [0, 0, 0, 0, 0, 0]
# Convert to radians
#start_pose = start_pose_deg
#end_pose = end_pose_deg

print("Point 1")
group.go(pose1, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()
time.sleep(2)

print("Point 2")
group.go(pose2, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()
time.sleep(2)

print("Point 3")
group.go(pose3, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()
time.sleep(2)

print("Point 4")
group.go(pose4, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()
time.sleep(2)

print("Point 5")
group.go(pose5, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()
time.sleep(2)

print("Point 6")
group.go(pose6, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()
time.sleep(2)

print("Point 7")
group.go(pose7, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()
time.sleep(2)

print("Point 8")
group.go(pose8, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()
time.sleep(2)

print("Point 9")
group.go(pose9, wait=True)
pose = group.get_current_pose().pose
print(pose)
group.stop()
time.sleep(2)

print("Motion complete.")

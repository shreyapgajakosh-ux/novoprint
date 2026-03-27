# novoprint

Terminal 1: 
source /opt/ros/noetic/setup.bash  
source ~/arctos_ws/devel/setup.bash   
roslaunch arctos_config demo.launch  

Wait until arm fully loads in Rviz   

Terminal 2: 
cd ~/arctos_ws/src/arctos_scripts/scripts
source /opt/ros/noetic/setup.bash
source ~/arctos_ws/devel/setup.bash 
chmod +x whateverfilename.py
rosrun arctos_scripts whateverfilename.py

My file oganization might be different.
cd is ./arctos_ws/src and this is my file organization

arctos_scripts  CMakeLists.txt  ROS

./arctos_scripts:
CMakeLists.txt  package.xml  scripts  src

./arctos_scripts/scripts:
block_i.py       joints_try.py     move_to_xyz.py        README.md
block_i.py.save  make_9_points.py  physical_9_points.py

./arctos_scripts/src:

./ROS:
arctos_config  arctos_urdf_description  moveit_screenshot.jpg
arctos_moveit  LICENSE                  README.md

./ROS/arctos_config:
CMakeLists.txt  config  launch  package.xml

./ROS/arctos_config/config:
arctos_urdf.srdf       fake_controllers.yaml  ompl_planning.yaml
cartesian_limits.yaml  joint_limits.yaml      ros_controllers.yaml
chomp_planning.yaml    kinematics.yaml        sensors_3d.yaml

./ROS/arctos_config/launch:
arctos_urdf_moveit_controller_manager.launch.xml
arctos_urdf_moveit_sensor_manager.launch.xml
chomp_planning_pipeline.launch.xml
default_warehouse_db.launch
demo_gazebo.launch
demo.launch
fake_moveit_controller_manager.launch.xml
gazebo.launch
joystick_control.launch
move_group.launch
moveit.rviz
moveit_rviz.launch
ompl_planning_pipeline.launch.xml
pilz_industrial_motion_planner_planning_pipeline.launch.xml
planning_context.launch
planning_pipeline.launch.xml
ros_controllers.launch
run_benchmark_ompl.launch
sensor_manager.launch.xml
setup_assistant.launch
trajectory_execution.launch.xml
warehouse.launch
warehouse_settings.launch.xml

./ROS/arctos_moveit:
arctos_moveit_arduino  CMakeLists.txt  msg  package.xml  scripts  src

./ROS/arctos_moveit/arctos_moveit_arduino:
arctos_moveit_arduino.ino

./ROS/arctos_moveit/msg:
ArmJointState.msg

./ROS/arctos_moveit/scripts:
interface.py               move_to_xyz.py  transform.py
moveo_objrec_publisher.py  README.md

./ROS/arctos_moveit/src:
move_group_interface_coor_1.cpp  moveit_convert.cpp

./ROS/arctos_urdf_description:
CMakeLists.txt  launch  LICENSE  meshes  package.xml  urdf

./ROS/arctos_urdf_description/launch:
controller.launch  controller.yaml  display.launch  gazebo.launch  urdf.rviz

./ROS/arctos_urdf_description/meshes:
base_link.stl  Left_jaw_1.stl  Link_2_1.stl  Link_4_1.stl  Link_6_1.stl
Gripper_1.stl  Link_1_1.stl    Link_3_1.stl  Link_5_1.stl  Right_jaw_1.stl

./ROS/arctos_urdf_description/urdf:
arctos.urdf         arctos_urdf.trans  materials.xacro
arctos_urdf.gazebo  arctos_urdf.xacro

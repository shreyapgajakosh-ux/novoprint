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
.
├── arctos_scripts
│   ├── CMakeLists.txt
│   ├── package.xml
│   ├── scripts
│   │   ├── block_i.py
│   │   ├── block_i.py.save
│   │   ├── joints_try.py
│   │   ├── make_9_points.py
│   │   ├── move_to_xyz.py
│   │   ├── physical_9_points.py
│   │   └── README.md
│   └── src
├── CMakeLists.txt -> /opt/ros/noetic/share/catkin/cmake/toplevel.cmake
└── ROS
    ├── arctos_config
    │   ├── CMakeLists.txt
    │   ├── config
    │   │   ├── arctos_urdf.srdf
    │   │   ├── cartesian_limits.yaml
    │   │   ├── chomp_planning.yaml
    │   │   ├── fake_controllers.yaml
    │   │   ├── joint_limits.yaml
    │   │   ├── kinematics.yaml
    │   │   ├── ompl_planning.yaml
    │   │   ├── ros_controllers.yaml
    │   │   └── sensors_3d.yaml
    │   ├── launch
    │   │   ├── arctos_urdf_moveit_controller_manager.launch.xml
    │   │   ├── arctos_urdf_moveit_sensor_manager.launch.xml
    │   │   ├── chomp_planning_pipeline.launch.xml
    │   │   ├── default_warehouse_db.launch
    │   │   ├── demo_gazebo.launch
    │   │   ├── demo.launch
    │   │   ├── fake_moveit_controller_manager.launch.xml
    │   │   ├── gazebo.launch
    │   │   ├── joystick_control.launch
    │   │   ├── move_group.launch
    │   │   ├── moveit.rviz
    │   │   ├── moveit_rviz.launch
    │   │   ├── ompl_planning_pipeline.launch.xml
    │   │   ├── pilz_industrial_motion_planner_planning_pipeline.launch.xml
    │   │   ├── planning_context.launch
    │   │   ├── planning_pipeline.launch.xml
    │   │   ├── ros_controllers.launch
    │   │   ├── run_benchmark_ompl.launch
    │   │   ├── sensor_manager.launch.xml
    │   │   ├── setup_assistant.launch
    │   │   ├── trajectory_execution.launch.xml
    │   │   ├── warehouse.launch
    │   │   └── warehouse_settings.launch.xml
    │   └── package.xml
    ├── arctos_moveit
    │   ├── arctos_moveit_arduino
    │   │   └── arctos_moveit_arduino.ino
    │   ├── CMakeLists.txt
    │   ├── msg
    │   │   └── ArmJointState.msg
    │   ├── package.xml
    │   ├── scripts
    │   │   ├── interface.py
    │   │   ├── moveo_objrec_publisher.py
    │   │   ├── move_to_xyz.py
    │   │   ├── README.md
    │   │   └── transform.py
    │   └── src
    │       ├── move_group_interface_coor_1.cpp
    │       └── moveit_convert.cpp
    ├── arctos_urdf_description
    │   ├── CMakeLists.txt
    │   ├── launch
    │   │   ├── controller.launch
    │   │   ├── controller.yaml
    │   │   ├── display.launch
    │   │   ├── gazebo.launch
    │   │   └── urdf.rviz
    │   ├── LICENSE
    │   ├── meshes
    │   │   ├── base_link.stl
    │   │   ├── Gripper_1.stl
    │   │   ├── Left_jaw_1.stl
    │   │   ├── Link_1_1.stl
    │   │   ├── Link_2_1.stl
    │   │   ├── Link_3_1.stl
    │   │   ├── Link_4_1.stl
    │   │   ├── Link_5_1.stl
    │   │   ├── Link_6_1.stl
    │   │   └── Right_jaw_1.stl
    │   ├── package.xml
    │   └── urdf
    │       ├── arctos.urdf
    │       ├── arctos_urdf.gazebo
    │       ├── arctos_urdf.trans
    │       ├── arctos_urdf.xacro
    │       └── materials.xacro
    ├── LICENSE
    ├── moveit_screenshot.jpg
    └── README.md





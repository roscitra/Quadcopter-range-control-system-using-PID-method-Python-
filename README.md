# Quadcopter-range-control-system-using-PID-method-Python-
I implemented this code in AR Drone 2.0 using the robot platform (ROS: Robot Operating System).

Note:
--
- ReadData.py: the code to subscribe the quadcopter sensor.
- PID.py: the algorithm PID code.
- PlantX.py and PlantY.py: system control code (Just run one of them).

*the input is range (you can change the input on PlantX.py or PlantY.py).
*ReadData and PID must be run first,then run PlantX or PlantY


--To run the code, make sure your code become node--

Make Workspace of your code (http://wiki.ros.org/ROS/Tutorials/CreatingPackage) 
- go to your simulator directory, cd ~/"yourdirectory_workspace"/src 
- catkin_create_pkg (nama package) std_msgs rospy roscpp - cd .. 
- catkin_make - source devel/setup.bash 
- rospack depends (nama package)

Coding your python/C++ program:
- Make your code bocome node python
- cd ~/"yourdirectory_workspace"/src/"your directory"
- chmod +x (file name)
- to make sure your code is node $ls and if your code colour is green, run code
- open new command line
- cd ~/"yourdirectory_workspace"/
- source devel/setup.bash
- rosrun script (file name)

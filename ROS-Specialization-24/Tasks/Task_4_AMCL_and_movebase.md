# ROS Navigation Stack
## What is this ROS Navigation stack??  
Here's what ROS wiki [says](http://wiki.ros.org/navigation).  
Let me say the same thing to you in absolute layman terms. 
- Basically the nav stack is just another [package](https://github.com/ros-planning/navigation) 
- Behind controlling every robot in a mapped environment, there are 3 things:
   1. **Localization** (estimate the position of the robot in its surrounding w.r.t to some global frame) with the help of various sensors like camera, Lidar, IMU, encoders(odometry)
   2. **A path planner** that claculates the path to follow from current position to the goal.
   3. A **controller** that gives the appropriate torque command to the wheels for the bot to follow its path.(You will probably learn more on this and planner part in the CnD Specialization, if you are interested feel free to check their stack, and explore.)
- The nav stack package does all of this for you. It takes in the Lidar scans and the odometry data and processes them all the time to constantly localize the bot.  
- It also has pre-written path planners like NavFn, TEB and DWA. 
- Further it also gives the final appropriate torque command to all the joints for the robot to follow the above path using the move_base package.  
- This is what you will be able to do after setting up nav stack. [working](https://www.youtube.com/watch?v=V32rff0pQy4)
- Basially once you have a map, you can command the bot to go anywhere in the map and it will take the **shortest path without any obstacles** and reach the goal.

clone navigation stack in your catkin_ws
```bash
~/catkin_ws/src $ git clone https://github.com/ros-planning/navigation.git
```
```bash
~/catkin_ws $ catkin build
```
# AMCL and Move Base

In the ROS (Robot Operating System) navigation stack, AMCL (Adaptive Monte Carlo Localization) and Move Base are two important components that work together to enable autonomous navigation for a robot. Let's explore each of them in more detail:

## AMCL (Adaptive Monte Carlo Localization):
AMCL is a localization algorithm used to estimate the robot's position (pose) within a known map. It is a probabilistic algorithm based on the Monte Carlo Localization (MCL) approach. AMCL uses a particle filter to represent the belief distribution of the robot's pose. It takes sensor measurements, such as laser scans or odometry, and updates the particles' weights based on their likelihood of being in the correct position. Over time, as the robot moves and receives new sensor measurements, the particle filter converges to a more accurate estimate of the robot's pose.

AMCL subscribes to sensor data topics, such as laser scans and odometry, and publishes the estimated robot pose on the amcl_pose topic. It provides the localization information required for navigation planning.

refer this for implementation in ros: [AMCL](https://www.youtube.com/watch?v=ZfQ30rfJb08)

## Move Base:
Move Base is responsible for path planning and controlling the robot's motion to reach a desired goal position. It combines the information from the global costmap (a 2D representation of the environment) and the local costmap (a smaller window around the robot) to plan a collision-free path. Move Base uses a planner algorithm, such as the Dijkstra or A* algorithm, to search for a path in the costmap from the current robot pose to the goal pose. It takes into account obstacles, known map information, and sensor data.

Once Move Base has planned a path, it generates velocity commands that are sent to the robot's low-level controllers (e.g., the motor controllers) to execute the desired motion. Move Base can adjust the robot's trajectory and update the path in real-time to handle dynamic obstacles or changes in the environment.

Move Base provides an action interface, allowing external components to send goal poses and monitor the status of the robot's motion. It publishes information about the planned path, goal status, and control commands.

refer this for implementation in ros: [Move_base](https://www.youtube.com/watch?v=oxDRuBgPOAo&t=4s)

Overall, AMCL and Move Base are crucial components in the ROS navigation stack. AMCL performs localization, estimating the robot's pose, while Move Base handles path planning and control to navigate the robot towards a goal position while avoiding obstacles. These components work together to enable autonomous navigation in ROS-based robotic systems.

# Task
## Task 1
For the map generated in the previous task , localize our Husky bot in that map by creating amcl_task.launch file.
- submit the a zip file of screenrecording of husky localizing in the map and amcl_task.launch file
  
## Task 2
After localizing the bot using amcl.launch create a move_base_task.launch to move husky to a goal point.
- submit the a zip file of screenrecording of husky navigating to the goal and move_base_task.launch file


**Phew!! That was a lot you learnt in the first two subparts. We are thrilled to see your hardwork and effort. :clap: :clap:** <br>
## Useful Resources  
- [The Construct](https://www.youtube.com/channel/UCt6Lag-vv25fTX3e11mVY1Q)  (Most useful channel for ROS, covers almost everytihng)
- [SLAM Map Building with TurtleBot](http://wiki.ros.org/turtlebot_navigation/Tutorials/Build%20a%20map%20with%20SLAM)
- [Autonomous Navigation of a Known Map with TurtleBot](http://wiki.ros.org/turtlebot_navigation/Tutorials/Autonomously%20navigate%20in%20a%20known%20map)

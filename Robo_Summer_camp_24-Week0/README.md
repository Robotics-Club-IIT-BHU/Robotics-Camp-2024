# Robo_Summer_camp_24-Week0
This is the Official GitHub repository for Summer Camp of Robotics Club IIT BHU

Hope you have dual-booted your PC with Ubuntu 20.04 !!

## ROS Installation Instruction

•	For Users with **Ubuntu 20.04 or Mac OS (Recommended)**
 
Install ROS Noetic from 
[Ubuntu install of ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)

Also, do check out this video demonstration to get an easier understanding of installation-
[ROS Noetic Installation and Path Sourcing](https://youtu.be/PowY8dV36DY)

## Creating a catkin workspace environment 
ROS uses workspaces that help you manage different packages without conflicting with other things that may disrupt your workflow.

[ROS WiKi Managing Environment](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)


**Commands to run in terminal:**

```bash
mkdir -p /catkin ws/src

cd catkin_ws/src/

catkin_init_workspace

sudo apt-get install python3-catkin-tools

cd /catkin ws/

catkin build

source devel/setup.bash
```



If you followed along till here, you will mostly have a file structure as follows


     ├── catkin_ws
         ├── build/
         |   ├── bin/
         |   ├── catkin/
         |   |   ...
         |   └── MakeFile
         ├── devel/
         |   ├── lib/
         |   ├── include/
         |   |   ...
         |   └── setup.bash
         └── src/
             ├── genpy/
             ├── packages1/
             |   ...
             └── CMakeLists.txt
           
**Moreover, try to use catkin build instead of catkin_make as it is standard,
more robust and supports multiple package type to be built together ( orocos, non-ros packages).**

For installing catkin tools on Ubuntu

```bash
$ sudo apt-get update
$ sudo apt-get install python3-catkin-tools
```
For others (depreciated)

```bash
$ sudo pip install -U catkin_tools
--or--
$ git clone https://github.com/catkin/catkin tools.git
$ cd catkin_tools
$ pip install -r requirements.txt --upgrade
$ python setup.py install --record install_manifest.txt
```


Finally

```bash
user@master: ~/catkin_ws$ catkin build
```
You will see build/ and devel/ are filled with new files built from your files from src.

## Installation Confirmation- The most awaited step


```bash
user@master: ~/$ roscore
... logging to /home/user/.ros/log/49745fac-d334-11eb-a534-809133531cbd/roslaunch-user-27006.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://localhost:33949/
ros_comm version 1.14.10


SUMMARY
========

PARAMETERS
 * /rosdistro: noetic
 * /rosversion: 1.14.10

NODES

auto-starting new master
process[master]: started with pid [27016]
ROS_MASTER_URI=http://localhost:11311/

setting /run_id to 49745fac-d334-11eb-a534-809133531cbd
process[rosout-1]: started with pid [27027]
started core service [/rosout]
```

If this shows in your terminal, then you are good to go.

Proceed to [TurtleBot.md](TurtleBot.md) 

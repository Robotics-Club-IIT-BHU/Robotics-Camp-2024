
# Gazebo

<p align="center"> <img src="https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/how_to_get_a_ros_robot_gazebo_model.png"/> <i><u>A Screen shot of Gazzebo</u></i>
</p

In this subpart we will learn about Gazebo. Gazebo is a 3D dynamic simulator with the ability to accurately and efficiently simulate populations of robots in complex indoor and outdoor environments. While similar to game engines, Gazebo offers physics simulation at a much higher degree of fidelity, a suite of sensors, and interfaces for both users and programs.

Typical uses of Gazebo include:

- testing robotics algorithms,
- designing robots,
- performing regression testing with realistic scenarios

A few key features of Gazebo include:

- multiple physics engines,
- a rich library of robot models and environments,
- a wide variety of sensors,
- convenient programmatic and graphical interfaces

Enough definitions in this subpart we will simulate a robot and move it gazebo. Excited?

<div align="center">
    <img src="https://media.tenor.com/images/28b60454008ba0a45bcd512264fb7c59/tenor.gif"/>
</div>

### Installation

```sh
curl -sSL http://get.gazebosim.org | sh
```

then check if installation worked. Running below command should open up gazebo window.

```sh
gazebo
```

Lets first create a package to learn how to use gazebo and ROS control. Use the following commands to create catkin package with required dependencies

```bash
~/catkin_ws/src $ catkin_create_pkg gazebo_demo roscpp rospy joint_state_controller robot_state_publisher
```

and then build the workspace

```bash
~/catkin_ws $ catkin_make
```
This will give error if you previously build your workspace by `catkin build` so in that case do 
```bash
~/catkin_ws $ catkin build
```

Now lets create all the required(launch, urdf, config, scripts) directories in package (notice the path in which you should run commands)

```bash
~/catkin_ws/src/gazebo_demo $ mkdir launch urdf config scripts
```

In order to simulate a bot we need a urdf of a bot, here we go [bot.urdf](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/bot.urdf). Download this file and place it in urdf (`~catkin_ws/src/gazebo_demo/urdf/`) directory which we created previously.

Now that we have a bot, we need to fire up gazebo and spawn the robot in it. Lets do that using launch files. Create a launch file `fire_up.launch` in launch directory which we created previously and paste following code in it. You can see comments to understand whats the use of each line in this launch file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<launch>
    <!-- This block of code is to call empty_world.launch file to fire up gazebo with
                empty world -->
    <include file="$(find gazebo_ros)/launch/empty_world.launch">
        <arg name="paused" value="false"/>
        <arg name="use_sim_time" value="true"/>
        <arg name="gui" value="true"/>
        <arg name="headless" value="false"/>
        <arg name="debug" value="false"/>
    </include>

    <!-- This line loads urdf data of out robot -->
    <param name="robot_description" command="cat '$(find gazebo_demo)/urdf/bot.urdf'" />

    <!-- Coordinates of bot which we need to spawn -->
    <arg name="x" default="0"/>
    <arg name="y" default="0"/>
    <arg name="z" default="0.5"/>

    <!-- Calling spawing node to spawn our robot -->
    <node name="mybot_spawn" pkg="gazebo_ros" type="spawn_model" output="screen"
          args="-urdf -param robot_description -model bot -x $(arg x) -y $(arg y) -z $(arg z)" />

</launch>
```

Now launch the file

```bash
~/catkin_ws $ roslaunch gazebo_demo fire_up.launch
```



You can see gazebo window and a bot spawned in it.

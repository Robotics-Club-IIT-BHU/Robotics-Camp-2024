# GMAPPING
## Follow-along Tasks

- We will be using the same package as before, just **add** [this](robo_world.world) robo_world.world file in **worlds** folder of [camp](camp) and we will make husky move in Gazebo.
- If you have checked the urdf you will find 4 joints one for each wheel, now there are two options-
   1. Configure each joint by specifying the PID constants for each joint and tune them.  
   2. The easy way - simply use the skid_steer_drive plugin. We go with this way for now.  
- Think of a plugin as reusable code which is available for you to use. Refer to [this](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins) for all the gazebo plugins available. 
- Now add the following lines to your urdf within the robot tags. 
```xml
<gazebo>
    <plugin name="skid_steer_drive_controller" filename="libgazebo_ros_skid_steer_drive.so">
      <updateRate>40.0</updateRate>
      <leftFrontJoint>husky_robot_model__front_left_wheel_joint</leftFrontJoint>  
      <rightFrontJoint>husky_robot_model__front_right_wheel_joint</rightFrontJoint>
      <leftRearJoint>husky_robot_model__rear_left_wheel_joint</leftRearJoint>
      <rightRearJoint>husky_robot_model__rear_right_wheel_joint</rightRearJoint>
      <wheelSeparation>0.57</wheelSeparation>
      <wheelDiameter>0.34</wheelDiameter>
      <robotBaseFrame>husky_robot_model__base_link</robotBaseFrame>
      <torque>60</torque>
      <topicName>cmd_vel</topicName>
      
      <commandTopic>cmd_vel</commandTopic>
      <odometryTopic>odom</odometryTopic>
      <odometryFrame>odom</odometryFrame>
      
      <broadcastTF>true</broadcastTF>
   </plugin>
</gazebo>
```
(go through the parameters carefully like joint names and topic names, you will know their use later)  

- Now to **add** the gazebo launch lines in the launch file [visualize.launch](camp/launch/visualize.launch). 
```xml
    <!-- This block of code is to call empty_world.launch file to fire up gazebo with
                empty world and then load world1 from our pkg -->
  <arg name="world" default="empty"/>
  <arg name="paused" default="false"/>
  <arg name="use_sim_time" default="true"/>
  <arg name="gui" default="true"/>
  <arg name="headless" default="false"/>
  <arg name="debug" default="false"/>
  
  <include file="$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="world_name" value="$(find camp)/worlds/robo_world.world"/>
    <arg name="paused" value="$(arg paused)"/>
    <arg name="use_sim_time" value="$(arg use_sim_time)"/>
    <arg name="gui" value="$(arg gui)"/>
    <arg name="headless" value="$(arg headless)"/>
    <arg name="debug" value="$(arg debug)"/>
  </include>

<!-- Coordinates of bot which we need to spawn -->
    <arg name="x" default="-8"/>
    <arg name="y" default="8"/>
    <arg name="z" default="0"/>
    <arg name="roll" value="0.0"/>
    <arg name="pitch" value="0.0"/>
    <arg name="yaw" value="0.0"/>
    
    <!-- Calling spawing node to spawn our robot in gazebo -->
   <node name="husky_spawn" pkg="gazebo_ros" type="spawn_model" output="screen" 
    args="-urdf -param robot_description -x $(arg x) -y $(arg y) -z $(arg z) -R $(arg roll) -P $(arg pitch) -Y $(arg yaw) -model husky" />
```
- Open up the bashrc in your home directory using
```bash
nano ~/.bashrc
# if you want you can edit this file without using nano.
```

At the end add the following line to **speed up loading the world** (do this step only once and make sure the path you enter below is the path of the worlds folder on your system)
```bash
export GAZEBO_MODEL_PATH=~/catkin_ws/src/camp/worlds
```  

- Now launch the file

```bash
~/catkin_ws $ roslaunch camp visualize.launch
```


You can see gazebo window and a bot spawned in it. Something similar to this.

<p align="center"><img src="media/Screenshot%20from%202023-06-10%2013-35-23.png"/></p>
<br>  

### If (you can see robot spawned) :
      then go ahead.
### Else:

<p align="center">
    <img src="https://c.tenor.com/pPKOYQpTO8AAAAAM/monkey-developer.gif" width=500/><br><b>Debug Time</b>
</p>
<br>  


- Now fire up another terminal and run the following command in it

```bash
 rostopic pub -r 1 /cmd_vel geometry_msgs/Twist "linear:
  x: 1.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0"
```
(PS: Use double tab after /cmd_vel to autocomplete)   

Now you can see the bot moving forward, similarly you can make it turn with the angular velocity z parameter. Go on and play.  
You can also try out the teleop_twist_keyboard with this 
```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```  
Note here that **cmd_vel** is the **topic** to which you are **publishing**, this value is intercepted by the skid_steer_plugin which does everything for you.  
In teleop_twist_keyboard, its the same, you publish to the cmd_vel topic, so if the urdf has some other topic name it won't work without changing the topic name in teleop_twist_keyboard.py.


#### Now we have to add the Lidar sensor to our husky. 
```xml
<gazebo reference="laser">
    <sensor type="ray" name="head_rplidar_sensor">
      <pose>0.424 0 0.327 0 0 0</pose>
      <visualize>true</visualize>
      <update_rate>40</update_rate>
      <ray>
        <scan>
          <horizontal>
            <samples>720</samples>
            <resolution>1</resolution>
            <min_angle>-2.35619</min_angle>
            <max_angle>2.35619</max_angle>
          </horizontal>
        </scan>
        <range>
          <min>0.5</min>
          <max>20.0</max>
          <resolution>0.01</resolution>
        </range>
        <noise>
          <type>gaussian</type>
          <mean>0.0</mean>
          <stddev>0.01</stddev>
        </noise>
      </ray>
      <plugin name="gazebo_ros_head_rplidar_controller" filename="libgazebo_ros_laser.so">
        <topicName>/laser/scan</topicName>
        <frameName>laser</frameName>
      </plugin>
    </sensor>
  </gazebo>
```
(this publishes laser scan data to /laser/scan topic and is bound to the "laser" link)  

- Now launch visualize.launch again and add the LaserScan topic under the add by topic option.

```bash
~/catkin_ws $ roslaunch camp visualize.launch
```

Now in gazebo you will see a blue 3 quarter circle. These are the laser rays projecting out from the lidar.   

<p align="center"><img src="media/Screenshot%20from%202023-06-10%2013-21-13.png"/><br><br></p>

And in Rviz you will see red dots, these are the objects reflecting back the laser rays. The red line is the wall in front.
 

### If (you are seeing something similar) :
      then go ahead.
### Else:

<p align="center">
    <img src="https://c.tenor.com/pPKOYQpTO8AAAAAM/monkey-developer.gif" width=500/><br><b>Debug Time</b>
</p>
<br> 

## SLAM GMAPPING

- [YouTube](https://youtu.be/MFqn9i68bfM)
- [ros_wiki](http://wiki.ros.org/gmapping)
```bash
$ rosrun gmapping slam_gmapping scan:=base_scan
```
- change scan topic according to rostopic list

# TASK
Using /scan topic of lidar data create a map of the gazebo environment same as you performed in week 2 

- submit a zip file of screen recording of creating a map and the map file.

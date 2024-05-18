# Install TurtleBot packages


During this Task, you will work with a simulated robot called **TurtleBot**, to apply the concepts of ROS. The following image is a picture of the robot you will work with. It is a differential drive robot, that has a Kinect sensor for environmental mapping, wheel encoders for position estimation.




Open application called **Terminator**, you can install it by running following command in the terminal:  
```bash
sudo apt-get install terminator
```

It's highly recommended to use this application instead of stock Terminal. You can have tabs or split windows into few terminals. 

 Now executute following command
 
 
`sudo apt-get install ros-noetic-turtlebot3-*`


After the installation:

```bash
cd ~
nano .bashrc
```

At the end of your .bashrc file add this line:

```bash
export TURTLEBOT3_MODEL=waffle
```


We have mentioned waffle here. You can use waffle_pi or burger also.

Now do things step-by-step in different terminals:
```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```







You should get something similar to the following.

![env](https://risc.readthedocs.io/_images/turtlebot-gazebo.png )

#### Move the robot


How can you move the Turtlebot?

The easiest way is by executing an existing ROS program to control the robot. A ROS program is executed by using some special files called **launch files**.
Since a previously-made ROS program already exists that allows you to move the robot using the keyboard, let's launch that ROS program to teleoperate the robot.

```bash

roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```


Read the instructions on the screen to know which keys to use to move the robot around, and start moving the robot!


Try it! When you're done, you can <kbd>CTRL</kbd>+<kbd>C</kbd> to stop the execution of the program.
you have to submit zip file of screen recording of you bot being controlled by teleopkey .

Hope you enjoyed playing with your bot you can change the world by changing the world parameter in launch file..

## Task1 - You have to submit the video of turtle bot 3 being controlled using keyboard in gazebo and a screenshot of rqt NodeGraph

#### What is a launch file ?


We've seen that ROS uses launch files in order to execute programs. when you use a command like roslaunch it just lunches a launch file so you were unknowingly launching a launch file  But... how do they work? Let's have a look.

lets  have a look at a launch file. Open the launch folder inside the ``turtlebot_teleop`` package and check the ``keyboard_teleop.launch`` file.

Open the turtle bot 3 package find launch folder inside it find teleop_key.launch open it  


You will see something like this

``` xml
<launch>
    <!-- turtlebot_teleop_key already has its own built in velocity smoother -->
    <node pkg="turtlebot_teleop" type="turtlebot_teleop_key" name="turtlebot_teleop_keyboard"  output="screen">
      <param name="scale_linear" value="0.5" type="double"/>
      <param name="scale_angular" value="1.5" type="double"/>
      <remap from="turtlebot_teleop_keyboard/cmd_vel" to="cmd_vel_mux/input/teleop"/>
    </node>
</launch>
```

In the launch file, you have some extra tags for setting parameters and remaps. For now, don't worry about those tags and focus on the node tag.

All launch files are contained within a ``<launch>`` tag. Inside that tag, you can see a ``<node>`` tag, where we specify the following parameters:

- pkg="``package_name``": Name of the package that contains the code of the ROS program to execute
- type="``python_file_name.py``" : Name of the program file that we want to execute
- name="``node_name``" : Name of the ROS node that will launch our Python file
- output="``type_of_output``" : Through which channel you will print the output of the Python file


## Task2 - Make a custom python script that will make turtle bot bot move in a Square.

***Key points to keep in mind.***

- While playing with your turtlebot you need to anaylse the node graph 
to identify the Topic which is responsible for movement of turtlebot
- You will have to publish msg to that topic using, the python script that will make the turtlebot move in a Square. 
- Dont feel demotivated if you are not able to figure out which topic you need to publish on. Here is a quick hint 
```
rostopic pub /cmd_vel geometry_msgs/Twist '{linear: {x: 0.1, y: 0, z: 0}, angular: {x: 0, y: 0, z: 0.1}}'
```

## Task3 (Bonus) - Load the TurtleBot into a custom world

Download the file [robo.world](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2024/blob/week-1/Robo_Summer_camp_24-Week1/subpart3/robo.world) from this directory

Create a new package with the necessary dependencies for TurleBot3 and Gazebo, and place the world inside this package. Now create a launch file to load this world in Gazebo. Submit a screen recording of a TurtleBot model spwaned inside this world.

It is suggested to poke around in the TurtleBot3 packages for figuring out how to proceed.

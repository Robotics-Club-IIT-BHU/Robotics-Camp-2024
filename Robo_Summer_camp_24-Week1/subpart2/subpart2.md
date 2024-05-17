<p align="center"><img src="https://answers.ros.org/upfiles/14554624266871161.png" width="60" height="60"> <b>R</b>obotic<b>O</b>perating<b>S</b>ystem 

<h1>Robotics-Summer-Camp 2024</h1> </p>

After reading through all that theory, let's apply it!

## Packages
In your workspace, there will be different groups of nodes performing similar tasks, or will be closely related to each other. They will be organised into packages for modularity. 
For a directory to be called a package, it must: 
- have metadata contained in a .xml file
- have instructions for catkin tools to build it

Thankfully the process of making these is handled by catkin tools. It is the convention to create packages within the src folder.
```bash
cd catkin_ws/src/
```
Your package will have some dependencies needing to be specified. 
```bash
catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
```
Your first package has been created!

Now you have to build the workspace and source the setup file.
```bash
cd ~/catkin_ws
catkin build #or catkin_make if you have used that before
source devel/setup.bash
```
You can do `rospack find beginner_tutorials` to check if everything has worked properly.
More information can be found [here](https://wiki.ros.org/ROS/Tutorials/CreatingPackage). Now onto the task.

## Task 1
Submit a video of your publisher and subscriber working together, with the code written in Python. You will have to develop the habit of reading documentation and following [this tutorial](https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29) is a good starting point. The message published has to be of the format "Communication is working smoothly! Ping no. %d", where %d is an integer incremented by 1 every ping.

## Task 1b (Bonus)
Perform Task 1 but with the nodes written in C++ this time and submit a video of their working.

*Tip*: For video submissions, you can use OBS Studio

<h1>Robotics-Summer-Camp 2024</h1> 

Hope you all have completed the ROS installation. And are familiar with what a workspace is and how to source your workspace. If not view [Week 0](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2024/tree/week-1/Robo_Summer_camp_24-Week0) of summer camp!

## Lets create your first package
To create your package first navigate to the workspace that you have created.
**Note:** If you named you workspace something other that catkin_ws then be sure to replace the name of your workspace.

```
cd ~/catkin_ws/src
```
This command is used to create a catkin package.
```
catkin_create_pkg $Your_pkg_name std_msgs rospy roscpp  # remember to replace the name to what_ever name you want
```
std_msgs, rospy and roscpp are all dependencies.

Now that you defined your package, you have to build it using catkin build, make sure that your working dir is you workspace.
```
cd ~/catkin_ws
catkin build
```

If there were no errors, Congrats you have successfully build the pkg, if not then it is debug time.
![DebugTime](Robo_Summer_camp_24-Week1/assests/serious.gif)

This is the general directry structure of workspace.
```
workspace_folder/        -- WORKSPACE
  src/                   -- SOURCE SPACE
    CMakeLists.txt       -- 'Toplevel' CMake file, provided by catkin
    package_1/
      CMakeLists.txt     -- CMakeLists.txt file for package_1
      package.xml        -- Package manifest for package_1
    ...
    package_n/
      CMakeLists.txt     -- CMakeLists.txt file for package_n
      package.xml        -- Package manifest for package_n
```
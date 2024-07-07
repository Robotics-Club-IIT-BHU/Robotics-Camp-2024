## Task1 (getting familiar with Rvizz)

Since you are familiar with building urdfs(Hope so if not then check week 2 of summer camp). In this task: 
- Download the folder [camp](camp) and inside this package you will see three folders launch, models, worlds.  
- Build the package and resolve the errors you might get. :)
- Now open up the models folder and under husky_robot_model you will find model.urdf, this is the urdf file you will be tweaking.  
- To visualize it run the visualize.launch file located in the launch folder using
``` 
roslaunch camp visualize.launch
```
(camp is the name of the package)  
- When Rviz opens up, change the fixed frame to husky_robot_model__base_link as this is the base link of the robot.  
- Now add the RobotModel using the Add button and now you should see be able to see the robot.  
<br>

### What you have to do (Task 1):  
- Add a **fixed box** to the top of the rod which will serve as the camera, by adding a new link and joint in the urdf file.  
<p align="center"><img src="media/Screenshot%20from%202022-07-09%2015-35-19.png" width="100%"><br><i>Something like this</i></p>

- Add the Tf modal using the Add button to see the frames as shown in the above picture.  
- Now instead of a fixed joint use a **revolute** joint to attach the box.  
- To check the movement of the joint go to the launch file and replace the joint_state_publisher line with this
 ``` 
 <node pkg="joint_state_publisher_gui" type="joint_state_publisher_gui" name="joint_state_publisher_gui" output="screen" />
 ```
- Relaunch Rviz and now you will see a gui panel with sliders using which you can check out your joint movements.
<p align="center"><img src="media/Screenshot%20from%202022-07-09%2015-44-14.png" width="100%"><br><i>joint_publisher_gui</i></p>
<br>

### Submission Instructions  
- A screenshot of the **modified** urdf with the camera in Rviz showing all the link frames.  
- The modified urdf file.
- A small screen recording of the camera box revolute joint moving using the joint_publisher_gui. 
- This is to just give you some hands on experience with Rviz. :)

### Useful Info
- [ ] You can use this link for reference [Visualising urdf tutorial from ROS for your urdf](http://wiki.ros.org/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch).  
- [ ] Don't get confused between robot_state_publisher and joint_state_publisher. **robot_state_publisher** is an inbuilt node which sets up the **TF tree of the urdf** for you while using **joint_state_publisher** you can **publish joint values** to the joints.
- [ ] Parameter "robot_description" stores the location of the urdf to load. There can only be one robot_description that can be viewed in Rviz at a time.

Happy `build`ing!!
